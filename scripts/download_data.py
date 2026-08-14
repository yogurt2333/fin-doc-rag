"""Download the Compliance-to-Code dataset (CC BY-NC 4.0) into data/raw/.

Source: https://github.com/AlexJJJChen/Compliance-to-Code
Dataset paper: Li et al., "Compliance-to-Code: Enhancing Financial Compliance
Checking via Code Generation", arXiv:2505.19804.
Underlying documents: public regulations of the Beijing Stock Exchange (BSE).

License note: CC BY-NC 4.0 (non-commercial). This project is a personal
portfolio demo. The dataset is NOT committed to this repo; run this script
to fetch it locally.
"""
import urllib.request
from pathlib import Path

BASE = (
    "https://raw.githubusercontent.com/AlexJJJChen/Compliance-to-Code/main/"
    "Compliance-to-Code-DatasetAndBenchmark/"
)
FILES = ["BSE08_BSE10_sft.json", "BSE08_BSE10_sft_no_think.json"]
OUT = Path(__file__).resolve().parent.parent / "data" / "raw"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        url = BASE + name
        dest = OUT / name
        print(f"downloading {url}")
        urllib.request.urlretrieve(url, dest)
        size = dest.stat().st_size
        print(f"  -> {dest} ({size:,} bytes)")
    print("done. explore data/raw/*.json next.")


if __name__ == "__main__":
    main()
