import json
from pathlib import Path
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = REPO_ROOT / "data"
TRAIN_PUB_DIR = DATA_DIR / "TrainingPubText"
TRAIN_SDRF_DIR = DATA_DIR / "TrainingSDRFs"
TEST_PUB_DIR = DATA_DIR / "TestPubText"


def load_publication(json_path: Path) -> dict:
    with open(json_path, "r") as f:
        return json.load(f)


def extract_sdrf_from_text(pub: dict) -> dict:
    """
    Given a publication JSON, return a dict matching one SDRF row.
    For now, return empty values.
    """
    return {}

from collections import Counter

def analyze_sdrf_coverage(sdrf_dir: Path):
    counts = Counter()
    total_rows = 0

    for csv_path in sdrf_dir.glob("*.tsv"):
        df = pd.read_csv(csv_path, sep="\t")

        total_rows += len(df)

        for col in df.columns:
            if col in {"ID", "PXD"}:
                continue

            non_empty = df[col].notna() & (df[col].astype(str).str.strip() != "")
            counts[col] += non_empty.sum()

    return counts, total_rows

def main():
    counts, total_rows = analyze_sdrf_coverage(TRAIN_SDRF_DIR)

    coverage = [
        (col, count, count / total_rows)
        for col, count in counts.items()
    ]

    coverage.sort(key=lambda x: x[2], reverse=True)

    print(f"Total rows: {total_rows}\n")
    for col, count, frac in coverage[:40]:
        print(f"{col:40s} {count:6d}  ({frac:.2%})")


if __name__ == "__main__":
    main()