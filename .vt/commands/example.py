from __future__ import annotations

import argparse

import vpython


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the VPython project command example.")
    parser.add_argument("message", nargs="?", default="ready")
    args = parser.parse_args()
    print(f"{vpython.__doc__} {args.message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
