class CueLintError(Exception):
    """Base class for expected CueLint errors."""


class InputError(CueLintError):
    """Raised when input cannot be read or is empty."""


class OutputFormatError(CueLintError):
    """Raised when an unsupported output format is requested."""


class UnsupportedFormatError(OutputFormatError):
    """Backward-compatible name for unsupported output format errors."""
