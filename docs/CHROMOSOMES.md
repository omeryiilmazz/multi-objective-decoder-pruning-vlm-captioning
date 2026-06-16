# Chromosome Documentation

This directory contains selected chromosomes obtained from the genetic algorithm search.

## Encoding

Each chromosome is a Boolean list representing decoder block retention:

- `true`: block retained
- `false`: block pruned

Example:

```json
{
  "label": "mid",
  "index": 6,
  "param_drop_rate": 0.168,
  "proxy_cider": 1.048,
  "final_cider": 1.178,
  "chromosome": [true, true, true, false]
}
```

## Summary

| Model | Level | Blocks | Pruned blocks | Param. drop | Proxy CIDEr | Final CIDEr | Final BLEU-4 |
|---|---:|---:|---|---:|---:|---:|---:|
| BLIP-2 | high | 32 | 4 8 9 12 14 16 18 21 25 29 30 | 0.2311 | 0.9543 | 1.0918 | 0.3213 |
| BLIP-2 | low | 32 | 3 9 10 18 21 | 0.1050 | 1.1367 | 1.2832 | 0.3848 |
| BLIP-2 | mid | 32 | 4 12 14 16 18 21 29 30 | 0.1681 | 1.0485 | 1.1778 | 0.3498 |
| Florence-2 | high | 12 | 3 6 8 9 | 0.0865 | 0.8987 | 1.0798 | 0.3151 |
| Florence-2 | low | 12 | 2 8 | 0.0433 | 1.0469 | 1.3234 | 0.3760 |
| Florence-2 | mid | 12 | 3 4 8 | 0.0649 | 1.0190 | 1.2984 | 0.3711 |
| InstructBLIP | high | 24 | 3 9 11 14 15 20 23 | 0.1131 | 0.7553 | 0.8072 | 0.2338 |
| InstructBLIP | low | 24 | 11 20 | 0.0323 | 0.8722 | 1.0089 | 0.3043 |
| InstructBLIP | mid | 24 | 3 9 11 17 20 | 0.0808 | 0.7957 | 0.9295 | 0.2877 |
| PaliGemma | high | 18 | 2 7 9 10 | 0.1506 | 0.8697 | 1.3007 | 0.3896 |
| PaliGemma | low | 18 | 3 8 | 0.0753 | 0.9731 | 1.3844 | 0.4099 |
| PaliGemma | mid | 18 | 2 6 10 | 0.1130 | 0.9250 | 1.3469 | 0.4030 |

A machine-readable CSV version is available at:

```text
results/chromosome_summary.csv
```
