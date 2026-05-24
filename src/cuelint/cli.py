from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import TextIO

from cuelint.errors import CueLintError, InputError
from cuelint.formatter import format_report
from cuelint.models import CliOptions
from cuelint.service import audit_text


def parse_args(argv: list[str] | None) -> CliOptions:
    parser = argparse.ArgumentParser(prog="cuelint", description="Audit one assistant response for deterministic cue patterns.")
    parser.add_argument("input_path", nargs="?", help="UTF-8 text file to audit. Reads stdin when omitted.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json", help="Output format. Defaults to JSON.")
    args = parser.parse_args(argv)
    return CliOptions(input_path=args.input_path, output_format=args.format)


def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise InputError(f"input file not found: {path}") from exc
    except OSError as exc:
        raise InputError(f"unable to read input file: {path}") from exc


def validate_non_empty(text: str) -> str:
    if not text.strip():
        raise InputError("input is empty")
    return text


def read_input(options: CliOptions, stdin: TextIO) -> str:
    if options.input_path:
        return validate_non_empty(read_file(options.input_path))
    return validate_non_empty(stdin.read())


def main(argv: list[str] | None = None) -> int:
    try:
        options = parse_args(argv)
        text = read_input(options, sys.stdin)
        sys.stdout.write(format_report(audit_text(text), options.output_format))
        return 0
    except CueLintError as exc:
        sys.stderr.write(f"cuelint: {exc}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
