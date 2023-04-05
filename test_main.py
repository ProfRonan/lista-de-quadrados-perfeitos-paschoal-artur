import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("0", ""),
        ("1", "1"),
        ("2", "1\n4"),
        ("3", "1\n4\n9"),
        ("4", "1\n4\n9\n16"),
        ("5", "1\n4\n9\n16\n25"),
        ("6", "1\n4\n9\n16\n25\n36"),
    ],
)
def test_fizz(monkeypatch: MonkeyPatch, test_input: str, expected_output: str):
    mocked_input = lambda prompt="": test_input
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert expected_output in mocked_stdout.getvalue().strip()
