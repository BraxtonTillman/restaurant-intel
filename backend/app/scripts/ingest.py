# app/scripts/ingest.py
import sys
from pathlib import Path

from app.services.ingestion.ingest_csv import ingest_csv

REPO_ROOT = Path(__file__).resolve().parents[3]  # restaurant-intel/


def main():
    if len(sys.argv) >= 2:
        p = Path(sys.argv[1])
        file_path = p if p.is_absolute() else (REPO_ROOT / p)
    else:
        file_path = REPO_ROOT / ".data" / "sample_sales.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"CSV not found: {file_path}")

    ingest_csv(str(file_path))


if __name__ == "__main__":
    main()
