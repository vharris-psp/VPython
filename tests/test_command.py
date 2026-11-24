from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


def test_example_command_uses_library_source() -> None:
    root = Path(__file__).parents[1]
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(root / "src")

    result = subprocess.run(
        [sys.executable, root / ".vt" / "commands" / "example.py", "tested"],
        cwd=root,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "VPython VT source library. tested"
