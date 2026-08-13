from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP_PATH = ROOT / "skills" / "endeavor-protocol" / "scripts" / "bootstrap.py"
VALIDATE_PATH = ROOT / "skills" / "endeavor-protocol" / "scripts" / "validate.py"


def load_bootstrap():
    spec = importlib.util.spec_from_file_location("endeavor_bootstrap", BOOTSTRAP_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load bootstrap module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BootstrapTests(unittest.TestCase):
    def setUp(self) -> None:
        self.module = load_bootstrap()

    def test_initialize_creates_expected_state(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "project"
            target.mkdir()
            (target / "existing.txt").write_text("preserve me\n", encoding="utf-8")

            paths = self.module.initialize(
                target,
                project_name="Test Endeavor",
                profiles=["communications", "audit"],
                mode="auto",
            )

            self.assertTrue((target / ".endeavor" / "PROJECT.md").is_file())
            self.assertTrue((target / ".endeavor" / "config.json").is_file())
            self.assertEqual(
                (target / "existing.txt").read_text(encoding="utf-8"),
                "preserve me\n",
            )
            config = json.loads(
                (target / ".endeavor" / "config.json").read_text(encoding="utf-8")
            )
            self.assertEqual(config["project_name"], "Test Endeavor")
            self.assertEqual(config["profiles"], ["communications", "audit"])
            self.assertEqual(config["requested_mode"], "auto")
            self.assertEqual(len(paths), 10)
            self.assertNotIn("{{PROJECT_NAME}}", (target / ".endeavor" / "PROJECT.md").read_text(encoding="utf-8"))

    def test_second_initialize_refuses_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self.module.initialize(
                target,
                project_name="First",
                profiles=["delivery"],
                mode="solo",
            )
            with self.assertRaises(FileExistsError):
                self.module.initialize(
                    target,
                    project_name="Second",
                    profiles=["audit"],
                    mode="solo",
                )

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            paths = self.module.initialize(
                target,
                project_name="Preview",
                profiles=["discovery"],
                mode="delegated",
                dry_run=True,
            )
            self.assertEqual(len(paths), 10)
            self.assertFalse((target / ".endeavor").exists())

    def test_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATE_PATH)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
