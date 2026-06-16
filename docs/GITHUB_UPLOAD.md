# GitHub Upload Guide

## Recommended Repository Name

```text
vlm-decoder-pruning-captioning
```

Alternative:

```text
multi-objective-decoder-pruning-vlm-captioning
```

## Recommended Repository Description

```text
Reproducibility package for multi-objective decoder block pruning in vision-language models for image captioning.
```

## Before Uploading

1. Review `README.md`.
2. Update `CITATION.cff` and replace `<username>` with your GitHub username.
3. Confirm the license choice in `LICENSE`.
4. Revoke any Hugging Face token that was previously stored in notebooks.
5. Run validation:

```bash
python scripts/validate_repository.py
```

## Upload from Terminal

From inside the repository folder:

```bash
git init
git add .
git commit -m "Initial reproducibility package"
git branch -M main
git remote add origin https://github.com/<username>/vlm-decoder-pruning-captioning.git
git push -u origin main
```

## Good GitHub Topics

Add these topics on GitHub:

```text
image-captioning
vision-language-models
decoder-pruning
multi-objective-optimization
genetic-algorithm
blip-2
instructblip
florence-2
paligemma
coco-dataset
nocaps
```

## Suggested Visibility

Start as a private repository if the manuscript is still under review. Make it public after checking:

- license choice,
- dataset redistribution permissions,
- removed credentials,
- final paper citation information.
