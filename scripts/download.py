#!/usr/bin/env python3
"""
Download UK Biobank Synthetic Dataset files.

This script downloads specified HES_SimDates.tsv files from the UK Biobank
synthetic dataset repository.
"""

import hashlib
from pathlib import Path
from urllib.request import urlretrieve
from typing import List
import sys


BASE_URL = "https://biobank.ndph.ox.ac.uk/synthetic_dataset/tabular/"
OUTPUT_DIR = Path("data")

# Files to download
FILES = [
    "41260_HES_SimDates.tsv",
    "41262_HES_SimDates.tsv",
    "41263_HES_SimDates.tsv",
    "41280_HES_SimDates.tsv",
    "41281_HES_SimDates.tsv",
    "41282_HES_SimDates.tsv",
    "41283_HES_SimDates.tsv",
]

# MD5 checksums from the website
CHECKSUMS = {
    "41260_HES_SimDates.tsv": "4ff448b195ad417c3ae1324312782c30",
    "41262_HES_SimDates.tsv": "46aced37adea430907b81b8370f4718b",
    "41263_HES_SimDates.tsv": "5fc75c1d4d221d4e8366d4ce7920e7f8",
    "41280_HES_SimDates.tsv": "60007421300548e3a03c317e3392e5d1",
    "41281_HES_SimDates.tsv": "3b5a706c475050c5a64ad4359d224309",
    "41282_HES_SimDates.tsv": "7592c86dbb8502ca0630a763aa85be47",
    "41283_HES_SimDates.tsv": "5c35335d9e91f1eb4c0dca92213f6cb9",
}


def calculate_md5(filepath: Path) -> str:
    """Calculate MD5 checksum of a file."""
    md5_hash = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def download_file(filename: str, output_dir: Path) -> bool:
    """
    Download a file from the UK Biobank repository.
    
    Args:
        filename: Name of the file to download
        output_dir: Directory to save the file
        
    Returns:
        True if download and verification successful, False otherwise
    """
    url = BASE_URL + filename
    output_path = output_dir / filename
    
    print(f"Downloading {filename}...", end=" ", flush=True)
    
    try:
        urlretrieve(url, output_path)
        print("✓")
        
        # Verify checksum
        if filename in CHECKSUMS:
            print(f"  Verifying checksum...", end=" ", flush=True)
            calculated = calculate_md5(output_path)
            expected = CHECKSUMS[filename]
            
            if calculated == expected:
                print("✓")
                return True
            else:
                print(f"✗ (expected {expected}, got {calculated})")
                return False
        else:
            print("  Warning: No checksum available for verification")
            return True
            
    except Exception as e:
        print(f"✗\n  Error: {e}")
        return False


def main():
    """Main function to download all specified files."""
    # Create output directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"Downloading UK Biobank files to {OUTPUT_DIR.absolute()}\n")
    
    results = []
    for filename in FILES:
        success = download_file(filename, OUTPUT_DIR)
        results.append((filename, success))
        print()
    
    # Summary
    print("=" * 60)
    print("Download Summary:")
    print("=" * 60)
    
    successful = sum(1 for _, success in results if success)
    failed = len(results) - successful
    
    for filename, success in results:
        status = "✓ Success" if success else "✗ Failed"
        print(f"{status}: {filename}")
    
    print("=" * 60)
    print(f"Total: {successful}/{len(results)} files downloaded successfully")
    
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
