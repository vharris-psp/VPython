from importlib import import_module
from importlib.metadata import distribution, version

import vpython


def test_package_imports() -> None:
    assert vpython.__doc__ == "VPython VT source library."


def test_installed_distribution_has_exact_sdk_linkage() -> None:
    requirements = distribution("vpython").requires or []
    sdk_requirements = [
        requirement
        for requirement in requirements
        if requirement.lower().startswith("vt-project-sdk")
    ]

    assert sdk_requirements == ["vt-project-sdk==1.9.0"]
    assert version("vt-project-sdk") == "1.9.0"
    assert import_module("vt_project_sdk").__name__ == "vt_project_sdk"
