# Method Summary

The study explores decoder block pruning for image captioning models using a multi-objective genetic algorithm approach.

## General Workflow

1. Run the baseline model on COCO and nocaps.
2. Define a chromosome representation over decoder blocks.
3. Use a proxy COCO subset to evaluate candidate pruning configurations.
4. Optimize for a trade-off between parameter reduction and captioning performance.
5. Select low, mid, and high pruning configurations from the Pareto front.
6. Evaluate selected pruned sub-models using full evaluation settings.

## Objective View

The pruning search balances two competing objectives:

- maximize captioning quality, primarily represented by CIDEr in the proxy search;
- maximize model reduction by pruning decoder blocks.

## Practical Interpretation

The chromosome files document the selected pruning configurations. The pruned notebooks show how these configurations are applied to each model family.
