#!/usr/bin/env python3
"""Validate chromosome JSON files and proxy COCO metadata."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate_chromosomes() -> None:
    files = sorted((ROOT / "chromosomes").glob("**/*.json"))
    if not files:
        raise SystemExit("No chromosome JSON files found.")

    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        chromosome = data.get("chromosome")
        if not isinstance(chromosome, list) or not chromosome:
            raise ValueError(f"Invalid chromosome in {path}")
        if not all(isinstance(x, bool) for x in chromosome):
            raise ValueError(f"Chromosome must contain booleans only: {path}")
    print(f"Validated {len(files)} chromosome files.")


def validate_proxy_data() -> None:
    manifest_path = ROOT / "data" / "proxy_coco_200" / "proxy_coco_200_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    missing = []
    for item in manifest["images"]:
        image_path = ROOT / item["relative_path"]
        if not image_path.exists():
            missing.append(str(image_path))
    if missing:
        raise FileNotFoundError("Missing proxy images:\n" + "\n".join(missing[:20]))
    print(f"Validated {len(manifest['images'])} proxy COCO images.")


if __name__ == "__main__":
    validate_chromosomes()
    validate_proxy_data()
