"""Run all tests and re-record the golden data."""

import argparse
import os
import pathlib
import platform
import shutil
import subprocess
import sys


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.parse_args()

    repo_root = pathlib.Path(os.path.realpath(__file__)).parent.parent

    for path in (repo_root / "test_data").iterdir():
        if path.is_dir() and path.name not in ["Json", "Xml"]:
            print(f"Deleting {path} ...")
            shutil.rmtree(path)

    env = os.environ.copy()
    env["AAS_CORE3_1_TYPESCRIPT_TEST_RECORD_MODE"] = "1"
    env["AAS_CORE3_1_TYPESCRIPT_TEST_DATA_DIR"] = str(repo_root / "test_data")

    # See: https://stackoverflow.com/questions/14680733/how-to-install-npm-package-from-python-script/50045443#50045443
    npm = "npm.cmd" if platform.system() == "Windows" else "npm"

    print("Running and re-recording all tests...")
    subprocess.check_call([npm, "run", "test"], env=env, cwd=repo_root)
    print("Re-recorded.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
