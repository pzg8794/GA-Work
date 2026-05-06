#!/usr/bin/env python3
"""Build a combined "master-of-masters" dataset from per-paper master CSVs.

This script concatenates CSVs named like:
  Validated_Logs/Master_Dataset_paper<N>-<KEY>.csv

And writes:
  Validated_Logs/Master_Dataset_papers-<KEY>.csv

It appends two columns to each row:
  - paper: e.g. "paper7"
  - config_key: e.g. "4000_2000"

Usage:
  python Validated_Logs/build_master_dataset_papers.py --key 4000_2000

Notes:
  - This is intentionally standalone and does not depend on `state_analysis.py`.
  - It validates that all input files have identical headers before concatenating.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


_DEFAULT_VALIDATED_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class InputFile:
    paper_num: int
    path: Path


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--key",
        default="4000_2000",
        help="Config key used in the per-paper master filenames (default: 4000_2000).",
    )
    parser.add_argument(
        "--validated-dir",
        default=str(_DEFAULT_VALIDATED_DIR),
        help=(
            "Directory containing per-paper master CSVs. "
            "Default: the directory containing this script (Validated_Logs)."
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Output CSV path. Default: <validated-dir>/Master_Dataset_papers-<key>.csv"
        ),
    )
    parser.add_argument(
        "--papers",
        default=None,
        help=(
            "Optional comma-separated paper numbers to include (e.g., 2,7,8,12). "
            "Default: auto-detect from filenames."
        ),
    )
    return parser.parse_args()


def _discover_inputs(validated_dir: Path, *, key: str) -> list[InputFile]:
    pattern = re.compile(rf"^Master_Dataset_paper(?P<num>\d+)-{re.escape(key)}\.csv$")
    inputs: list[InputFile] = []

    for fp in validated_dir.glob(f"Master_Dataset_paper*-{key}.csv"):
        m = pattern.match(fp.name)
        if not m:
            continue
        inputs.append(InputFile(paper_num=int(m.group("num")), path=fp))

    inputs.sort(key=lambda i: i.paper_num)
    return inputs


def _filter_inputs(inputs: list[InputFile], *, papers: set[int] | None) -> list[InputFile]:
    if papers is None:
        return inputs
    filtered = [i for i in inputs if i.paper_num in papers]
    return sorted(filtered, key=lambda i: i.paper_num)


def build_master_of_masters(*, validated_dir: Path, key: str, output: Path, papers: set[int] | None) -> None:
    inputs = _discover_inputs(validated_dir, key=key)
    inputs = _filter_inputs(inputs, papers=papers)

    if not inputs:
        raise SystemExit(
            f"No inputs found in {validated_dir} matching Master_Dataset_paper<N>-{key}.csv"
        )

    print("Inputs:")
    for i in inputs:
        print(f"  paper{i.paper_num}: {i.path}")

    base_fieldnames: list[str] | None = None
    rows_written = 0

    per_paper_rows = Counter()

    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", newline="") as out_f:
        writer: csv.DictWriter | None = None

        for i in inputs:
            paper_label = f"paper{i.paper_num}"

            with i.path.open(newline="") as in_f:
                reader = csv.DictReader(in_f)
                if reader.fieldnames is None:
                    raise SystemExit(f"No header found in {i.path}")

                if base_fieldnames is None:
                    base_fieldnames = list(reader.fieldnames)
                    out_fieldnames = base_fieldnames + ["paper", "config_key"]
                    writer = csv.DictWriter(out_f, fieldnames=out_fieldnames)
                    writer.writeheader()
                else:
                    if list(reader.fieldnames) != base_fieldnames:
                        raise SystemExit(
                            "Header mismatch between input files.\n"
                            f"Expected: {base_fieldnames}\n"
                            f"Got from {i.path}: {list(reader.fieldnames)}"
                        )

                assert writer is not None

                for row in reader:
                    row["paper"] = paper_label
                    row["config_key"] = key
                    writer.writerow(row)
                    rows_written += 1
                    per_paper_rows[paper_label] += 1

    print(f"\nWrote {rows_written} rows -> {output}")
    print("Rows per paper:")
    for paper_label in sorted(per_paper_rows):
        print(f"  {paper_label}: {per_paper_rows[paper_label]}")


def main() -> None:
    args = _parse_args()
    validated_dir = Path(args.validated_dir)
    key = str(args.key)

    output = Path(args.output) if args.output else validated_dir / f"Master_Dataset_papers-{key}.csv"

    papers: set[int] | None
    if args.papers:
        papers = {int(x.strip()) for x in args.papers.split(",") if x.strip()}
    else:
        papers = None

    build_master_of_masters(validated_dir=validated_dir, key=key, output=output, papers=papers)


if __name__ == "__main__":
    main()
