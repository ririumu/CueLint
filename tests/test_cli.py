import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from cuelint.cli import main, parse_args, read_input
from cuelint.errors import InputError
from cuelint.models import CliOptions


class CliTests(unittest.TestCase):
    def test_parse_args_defaults_to_json(self):
        options = parse_args([])

        self.assertIsNone(options.input_path)
        self.assertEqual(options.output_format, "json")

    def test_read_input_from_stdin(self):
        self.assertEqual(read_input(CliOptions(input_path=None), io.StringIO("I cannot.")), "I cannot.")

    def test_read_input_rejects_empty_stdin(self):
        with self.assertRaisesRegex(InputError, "empty"):
            read_input(CliOptions(input_path=None), io.StringIO("  \n"))

    def test_cli_stdin_json(self):
        old_stdin = sys.stdin
        sys.stdin = io.StringIO("I cannot guarantee that.")
        stdout = io.StringIO()
        try:
            with redirect_stdout(stdout):
                self.assertEqual(main([]), 0)
        finally:
            sys.stdin = old_stdin
        output = json.loads(stdout.getvalue())
        self.assertGreaterEqual(output["summary"]["evidence_count"], 2)

    def test_cli_file_input(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_file = Path(tmpdir) / "response.txt"
            input_file.write_text("This does not mean failure.", encoding="utf-8")
            stdout = io.StringIO()

            with redirect_stdout(stdout):
                self.assertEqual(main([str(input_file)]), 0)
            output = json.loads(stdout.getvalue())
            self.assertTrue(output["evidence"])

    def test_cli_missing_file_returns_nonzero(self):
        stderr = io.StringIO()

        with redirect_stderr(stderr):
            self.assertEqual(main(["missing.txt"]), 2)
        self.assertIn("not found", stderr.getvalue())

    def test_cli_markdown_option(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_file = Path(tmpdir) / "response.txt"
            input_file.write_text("Not X but Y.", encoding="utf-8")
            stdout = io.StringIO()

            with redirect_stdout(stdout):
                self.assertEqual(main([str(input_file), "--format", "markdown"]), 0)
            self.assertIn("# CueLint Report", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
