# Notebook 04 Summary — Mod30 SAE Toy Model

Notebook 04 converts exact Mod30 residue lanes into continuous synthetic embeddings
and tests whether a lightweight sparse factorization recovers local tile structure.

## Model

Nonnegative Matrix Factorization:

`X ≈ W H`

## Component grid

`[1, 4, 8, 12]`

## Metrics

|   n_components |   reconstruction_error |   activation_sparsity |   mean_lane_purity |   max_lane_purity |   captured_lanes |   coverage_fraction |   total_activations |   redundancy | recovered_residues     | missed_residues                |
|---------------:|-----------------------:|----------------------:|-------------------:|------------------:|-----------------:|--------------------:|--------------------:|-------------:|:-----------------------|:-------------------------------|
|              1 |               0.732004 |              0        |           0.180648 |          0.180648 |                0 |                0    |                 400 |      inf     | []                     | [1, 7, 11, 13, 17, 19, 23, 29] |
|              4 |               0.477987 |              0.52375  |           0.484292 |          0.542087 |                4 |                0.5  |                 762 |      190.5   | [7, 13, 19, 29]        | [1, 11, 17, 23]                |
|              8 |               0.371172 |              0.636875 |           0.475309 |          0.741072 |                6 |                0.75 |                1162 |      193.667 | [1, 7, 13, 17, 23, 29] | [11, 19]                       |
|             12 |               0.34603  |              0.693958 |           0.332355 |          0.75034  |                6 |                0.75 |                1469 |      244.833 | [1, 7, 13, 17, 23, 29] | [11, 19]                       |

## Interpretation

As feature count increases, learned sparse components shift from global blur toward local Mod30 tile recovery.

## Generated figures

- `figures/16_synthetic_embedding_residue_circle.png`
- `figures/17_ground_truth_tile_matrix.png`
- `figures/18_nmf_learned_activation_matrix.png`
- `figures/19_feature_to_lane_alignment.png`
- `figures/20_recovery_metrics_summary.png`
- `figures/21_reconstruction_error_vs_feature_count.png`
- `figures/22_alignment_matrix_{k}_components.png` for k in `[1, 4, 8, 12]`

## Generated data

- `data/04_nmf_recovery_metrics.csv`
