#!/usr/bin/env python3

import argparse
from pathlib import Path

import nltk


def download_packages(target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)

    # Keep the list in sync with nltk.download calls in scripts.
    packages = ["punkt", "punkt_tab"]

    for package in packages:
        print(f"Downloading '{package}' into {target_dir} ...")
        nltk.download(package, download_dir=str(target_dir))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Pre-download NLTK assets used by RULER.")
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path(__file__).resolve().parent / "nltk_data",
        help="Destination directory for the downloaded resources.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    download_packages(args.dest)

    print("\nDone.")
    print(
        "Set the NLTK_DATA environment variable to this directory when running offline, e.g.\n"
        f'  export NLTK_DATA="{args.dest}"'
    )


if __name__ == "__main__":
    main()
