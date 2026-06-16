# Notebooks

The notebooks are organized by experiment type. Baseline notebooks are separated by dataset; pruned notebooks are grouped as final-evaluation notebooks because each file contains both COCO and nocaps final evaluation workflows.

```text
notebooks/
├── baselines/
│   ├── coco/
│   └── nocaps/
└── pruned/
    └── final_evaluation/
```

Notebook outputs have been cleared for a clean Git history. The original uploaded filenames are documented in `docs/FILE_MAP.md`.

Before running, check dataset paths and Hugging Face authentication cells.
