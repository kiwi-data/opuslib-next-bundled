from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


def _load_loader_module():
    module_path = Path(__file__).resolve().parent.parent / "opuslib_next" / "_loader.py"
    spec = importlib.util.spec_from_file_location("opuslib_next__loader", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LoaderTest(unittest.TestCase):
    def test_loader_points_to_native_dir(self) -> None:
        loader_module = _load_loader_module()
        native_dir = Path(loader_module._NATIVE_DIR)
        self.assertEqual(native_dir.name, "_native")

    def test_bundled_library_filename_matches_platform(self) -> None:
        loader_module = _load_loader_module()
        filename = loader_module._library_filename()
        self.assertIn(filename, {"libopus.so", "libopus.dylib", "opus.dll"})
