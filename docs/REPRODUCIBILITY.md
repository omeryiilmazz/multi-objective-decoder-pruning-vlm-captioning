# Reproducibility Guide

This repository is notebook-oriented because the original experiments were executed in Google Colab with GPU acceleration.

## 1. Environment

Install the dependencies:

```bash
pip install -r requirements.txt
```

Recommended hardware:

- CUDA-enabled GPU
- At least 16 GB GPU memory for smaller runs
- More memory for large checkpoints such as BLIP-2 OPT-2.7B, InstructBLIP FLAN-T5-XL, Florence-2 Large, and PaliGemma 3B

## 2. Authentication

Some Hugging Face checkpoints may require authentication.

Do not write tokens directly in notebooks.

Use:

```bash
huggingface-cli login
```

or:

```python
from huggingface_hub import login
login()
```

## 3. Data Setup

The proxy COCO subset is already organized under:

```text
data/proxy_coco_200/
```

For full COCO and nocaps evaluations, download and prepare the datasets separately, then update the path variables inside the notebooks.

## 4. Baseline Runs

Run the notebooks in:

```text
notebooks/baselines/coco/
notebooks/baselines/nocaps/
```

Each notebook loads the corresponding model, generates captions, and evaluates the outputs using captioning metrics such as BLEU, METEOR, ROUGE-L, and CIDEr where available.

## 5. GA / Pruned Runs

Run the notebooks in:

```text
notebooks/pruned/final_evaluation/
```

These notebooks implement chromosome-based decoder block pruning and include the final evaluation workflows for both COCO and nocaps. The selected chromosomes are stored in:

```text
chromosomes/
```

## 6. Chromosome Interpretation

In chromosome JSON files:

- `true`: decoder block is retained
- `false`: decoder block is pruned

The consolidated summary is available in:

```text
results/chromosome_summary.csv
```

## 7. Known Practical Notes

- Some notebooks still contain Colab-specific path logic such as Google Drive mounting. Adjust paths before local execution.
- Notebook outputs were intentionally cleared before publication to avoid committing large outputs, account metadata, and stale execution artifacts.
- The code is preserved as an academic reproducibility package, not as a production inference library.
