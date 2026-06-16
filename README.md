# Multi-Objective Decoder Block Pruning for Image Captioning Across Vision-Language Models

This repository contains the reproducibility package for the study **"Multi-Objective Decoder Block Pruning for Image Captioning Across Vision-Language Models"**.

The project evaluates decoder block pruning for image captioning across four vision-language models. It includes baseline notebooks, genetic algorithm based pruned-model notebooks, selected pruning chromosomes, and a 200-image proxy COCO subset used during the search process. The pruned-model notebooks include the final evaluation workflows for both COCO and nocaps.

## Models

| Model | Backbone / checkpoint used in notebooks | Evaluation setting |
|---|---|---|
| BLIP-2 | `Salesforce/blip2-opt-2.7b` | COCO, nocaps |
| InstructBLIP | `Salesforce/instructblip-flan-t5-xl` | COCO, nocaps |
| Florence-2 | `microsoft/Florence-2-large` | COCO, nocaps |
| PaliGemma | `google/paligemma-3b-ft-cococap-448` | COCO, nocaps |

## Repository Structure

```text
.
├── notebooks/
│   ├── baselines/
│   │   ├── coco/
│   │   └── nocaps/
│   └── pruned/
│       └── final_evaluation/
├── chromosomes/
├── data/
│   └── proxy_coco_200/
├── docs/
├── results/
└── scripts/
```

## Contents

- `notebooks/baselines/coco/`: baseline COCO evaluation notebooks.
- `notebooks/baselines/nocaps/`: baseline nocaps evaluation notebooks.
- `notebooks/pruned/final_evaluation/`: GA chromosome-based pruned model notebooks.
- `chromosomes/`: selected low, mid, and high pruning chromosomes in JSON format.
- `data/proxy_coco_200/`: proxy COCO subset metadata, annotations, and images.
- `results/chromosome_summary.csv`: consolidated chromosome summary table.
- `docs/`: reproducibility, data, chromosome, and file-mapping documentation.

## Installation

Create an isolated environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

For Google Colab usage, run the installation cells inside the notebooks and authenticate to Hugging Face interactively when needed.

## Hugging Face Authentication

Some checkpoints may require a Hugging Face account or token. Do **not** hard-code tokens inside notebooks or scripts.

Recommended options:

```bash
huggingface-cli login
```

or, inside a notebook:

```python
from huggingface_hub import login
login()
```

## Data

The repository includes a small `proxy_coco_200` subset for reproducibility of the proxy search setup. Full COCO and nocaps datasets are not redistributed here. See [`docs/DATA.md`](docs/DATA.md) for expected directory layouts and data notes.

## Chromosomes

Selected pruning chromosomes are stored as JSON files under `chromosomes/`. In these files, `true` means the decoder block is retained and `false` means the decoder block is pruned.

A consolidated summary is available at:

```text
results/chromosome_summary.csv
```

## Reproducibility

Start with:

1. [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md)
2. [`docs/DATA.md`](docs/DATA.md)
3. [`docs/CHROMOSOMES.md`](docs/CHROMOSOMES.md)
4. [`docs/FILE_MAP.md`](docs/FILE_MAP.md)

## Security Note

The uploaded notebooks originally contained hard-coded Hugging Face tokens. They were removed in this GitHub-ready version. Never commit API tokens, private keys, local Drive paths containing personal information, or account-specific credentials.

## Citation

If you use this repository, please cite the associated manuscript and repository. See [`CITATION.cff`](CITATION.cff).

## License

Source code is released under the MIT License. Dataset images and annotations remain subject to their original dataset licenses and terms.
