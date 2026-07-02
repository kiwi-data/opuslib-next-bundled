from __future__ import annotations

from pathlib import Path


def pytest_ignore_collect(collection_path: Path) -> bool:
    if collection_path.name in {"conftest.py", "test_loader.py"}:
        return False

    bundled_dir = Path(__file__).resolve().parent.parent / "opuslib_next" / "_native"
    bundled_names = ("libopus.so", "libopus.dylib", "opus.dll")
    has_bundled_lib = any((bundled_dir / filename).exists() for filename in bundled_names)
    return not has_bundled_lib
