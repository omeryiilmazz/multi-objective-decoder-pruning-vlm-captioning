#!/usr/bin/env python3
"""Regenerate proxy_coco_200_manifest.json and proxy_coco_200_image_ids.txt."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "proxy_coco_200"
ANN_PATH = DATA_DIR / "proxy_coco_200_annotations.json"


def main() -> None:
    annotations = json.loads(ANN_PATH.read_text(encoding="utf-8"))
    records = []
    for image in annotations.get("images", []):
        image_id = int(image.get("image_id", image.get("id")))
        file_name = image.get("filename", image.get("file_name", f"COCO_val2014_{image_id:012d}.jpg"))
        records.append({
            "image_id": image_id,
            "file_name": file_name,
            "relative_path": f"data/proxy_coco_200/images/{file_name}",
            "num_reference_captions": len(image.get("captions", [])),
        })
    records.sort(key=lambda item: item["image_id"])

    (DATA_DIR / "proxy_coco_200_manifest.json").write_text(
        json.dumps({
            "name": "proxy_coco_200",
            "source": "COCO val2014 subset",
            "n_images": len(records),
            "seed": annotations.get("seed"),
            "images": records,
        }, indent=2),
        encoding="utf-8",
    )
    (DATA_DIR / "proxy_coco_200_image_ids.txt").write_text(
        "\n".join(str(item["image_id"]) for item in records) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote manifest for {len(records)} images.")


if __name__ == "__main__":
    main()
