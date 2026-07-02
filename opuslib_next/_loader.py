from __future__ import annotations

import ctypes
import os
import platform
from pathlib import Path
from typing import Final

from ctypes.util import find_library

_PACKAGE_DIR: Final[Path] = Path(__file__).resolve().parent
_NATIVE_DIR: Final[Path] = _PACKAGE_DIR / "_native"
_SYSTEM_LIB_ENV: Final[str] = "OPUSLIB_NEXT_USE_SYSTEM_LIB"


class OpusLibraryNotFoundError(RuntimeError):
    """Raised when no usable libopus binary can be found."""


def _library_filename() -> str:
    system_name = platform.system()
    if system_name == "Darwin":
        return "libopus.dylib"
    if system_name == "Linux":
        return "libopus.so"
    if system_name == "Windows":
        return "opus.dll"
    raise OpusLibraryNotFoundError(f"Unsupported operating system: {system_name}")


def _bundled_library_path() -> Path:
    return _NATIVE_DIR / _library_filename()


def _system_library_name() -> str:
    system_name = platform.system()
    if system_name == "Windows":
        return "opus"
    return "opus"


def _load_bundled_library() -> ctypes.CDLL:
    library_path = _bundled_library_path()
    if not library_path.exists():
        raise OpusLibraryNotFoundError(f"Bundled Opus library not found: {library_path}")
    return ctypes.CDLL(os.fspath(library_path))


def _load_system_library() -> ctypes.CDLL:
    system_path = find_library(_system_library_name())
    if system_path is None:
        raise OpusLibraryNotFoundError("System libopus could not be found")
    return ctypes.CDLL(system_path)


def load_libopus() -> ctypes.CDLL:
    if os.environ.get(_SYSTEM_LIB_ENV) == "1":
        return _load_system_library()
    return _load_bundled_library()
