"""Update to the latest meta-model and the latest test data."""

import argparse
import os
import pathlib
import platform
import subprocess
import sys


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.parse_args()

    repo_root = pathlib.Path(os.path.realpath(__file__)).parent.parent

    print("Downloading the latest meta-model...")
    subprocess.check_call(
        [
            sys.executable,
            str(repo_root / "dev_scripts" / "download_aas_core_meta_model.py"),
        ],
        cwd=str(repo_root),
    )

    print("Generating the code...")
    subprocess.check_call(
        [
            sys.executable,
            str(repo_root / "dev_scripts" / "regenerate_code.py"),
        ],
        cwd=str(repo_root),
    )

    # See: https://stackoverflow.com/questions/14680733/how-to-install-npm-package-from-python-script/50045443#50045443
    npm = "npm.cmd" if platform.system() == "Windows" else "npm"

    print("Re-formatting the code...")
    subprocess.run([npm, "run", "format"], cwd=repo_root, check=True)

    print("Downloading the latest test data...")
    subprocess.check_call(
        [
            sys.executable,
            str(repo_root / "dev_scripts" / "download_latest_test_data.py"),
        ],
        cwd=str(repo_root),
    )

    print("Re-recording the test data...")
    subprocess.check_call(
        [sys.executable, str(repo_root / "dev_scripts" / "rerecord_tests.py")],
        cwd=str(repo_root),
    )

    print("Running the pre-commit to check that everything worked...")
    subprocess.check_call([npm, "run", "build"], cwd=repo_root)
    subprocess.check_call([npm, "run", "lint"], cwd=repo_root)
    subprocess.check_call([npm, "run", "test"], cwd=repo_root)

    return 0


if __name__ == "__main__":
    sys.exit(main())
