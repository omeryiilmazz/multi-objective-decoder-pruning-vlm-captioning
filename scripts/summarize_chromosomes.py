#!/usr/bin/env python3
"""Generate results/chromosome_summary.csv from chromosome JSON files."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "chromosome_summary.csv"

MODEL_NAMES = {
    "blip2": "BLIP-2",
    "florence2": "Florence-2",
    "instructblip": "InstructBLIP",
    "paligemma": "PaliGemma",
}


def main() -> None:
    rows = []
    for model_dir, model_name in MODEL_NAMES.items():
        for path in sorted((ROOT / "chromosomes" / model_dir).glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            chromosome = data.get("chromosome", [])
            pruned = [idx for idx, keep in enumerate(chromosome) if keep is False]
            retained = [idx for idx, keep in enumerate(chromosome) if keep is True]
            rows.append({
                "model": model_name,
                "file": str(path.relative_to(ROOT)),
                "label": data.get("label", ""),
                "index": data.get("index", ""),
                "num_blocks": len(chromosome),
                "retained_blocks": " ".join(map(str, retained)),
                "pruned_blocks": " ".join(map(str, pruned)),
                "num_pruned_blocks": len(pruned),
                "param_drop_rate": data.get("param_drop_rate", ""),
                "proxy_cider": data.get("proxy_cider", ""),
                "final_cider": data.get("final_cider", ""),
                "final_bleu4": data.get("final_bleu4", ""),
                "final_meteor": data.get("final_meteor", ""),
                "final_rouge_l": data.get("final_rouge_l", ""),
            })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
