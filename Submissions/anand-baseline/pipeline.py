import json
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
TRAIN_PUB_DIR = Path("data/TrainingPubText")
TRAIN_SDRF_DIR = Path("data/TrainingSDRFs")
TEST_PUB_DIR = Path("data/TestPubText")


def load_publication(json_path: Path) -> dict:
    with open(json_path, "r") as f:
        return json.load(f)


def extract_sdrf_from_text(pub: dict) -> dict:
    """
    Given a publication JSON, return a dict matching one SDRF row.
    For now, return empty values.
    """
    return {}


def main():
    # sanity check: load one paper
    pub_files = sorted(TRAIN_PUB_DIR.glob("*.json"))
    if not pub_files:
        raise RuntimeError("No training publication files found")

    pub = load_publication(pub_files[0])
    print("Loaded publication:", pub_files[0].name)

    row = extract_sdrf_from_text(pub)
    print("Extracted row:", row)


if __name__ == "__main__":
    main()