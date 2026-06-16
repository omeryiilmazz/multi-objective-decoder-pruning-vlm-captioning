# Data Documentation

## Proxy COCO 200

The `data/proxy_coco_200/` directory contains a 200-image proxy subset derived from COCO val2014. This subset was used during the genetic algorithm search process to estimate captioning performance under decoder block pruning.

Directory layout:

```text
data/proxy_coco_200/
├── images/
├── proxy_coco_200_annotations.json
├── proxy_coco_200_gt_pycocotools.json
├── proxy_coco_200_manifest.json
└── proxy_coco_200_image_ids.txt
```

Files:

- `proxy_coco_200_annotations.json`: proxy subset metadata and reference captions.
- `proxy_coco_200_gt_pycocotools.json`: pycocotools-compatible ground-truth format.
- `proxy_coco_200_manifest.json`: generated manifest with image IDs, filenames, and relative paths.
- `proxy_coco_200_image_ids.txt`: plain-text list of COCO image IDs.

## Full COCO Evaluation

The baseline and pruned notebooks may expect COCO-style data such as:

```text
datasets/coco2014/
├── val2014/
├── annotations/
├── coco_karpathy_test.json
└── coco_karpathy_test_gt.json
```

Update notebook paths according to your local or Colab Drive environment.

## nocaps Evaluation

The nocaps notebooks expect nocaps validation images and a ground-truth file prepared in the format used by the evaluation cells. Update the following paths inside notebooks as needed:

```text
nocaps_val_4500_captions_domain_norm.json
nocaps validation image directory
```

## License and Redistribution Notice

This repository is intended for academic reproducibility. COCO and nocaps/Open Images data are governed by their respective dataset licenses and terms. Do not assume that model code licensing automatically covers dataset images.
