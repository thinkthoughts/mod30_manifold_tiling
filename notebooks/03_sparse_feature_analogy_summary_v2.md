# Notebook 03 Summary v2 — Sparse Feature Analogy

Notebook 03 builds toy sparse-feature representations over Mod30 residue lanes.

## New v2 metric

`redundancy = total_activations / captured_lanes`

## Result

| representation            |   feature_count |   captured_lanes |   missed_lanes |   coverage_fraction |   mean_feature_activation |   active_rows_fraction |   dilution_index |   total_activations |   redundancy | captured_residues              | missed_residues             |
|:--------------------------|----------------:|-----------------:|---------------:|--------------------:|--------------------------:|-----------------------:|-----------------:|--------------------:|-------------:|:-------------------------------|:----------------------------|
| single global-style lane  |               1 |                1 |              7 |               0.125 |                 0.0333333 |              0.0333333 |              1   |                  10 |           10 | [1]                            | [7, 11, 13, 17, 19, 23, 29] |
| eight one-hot local tiles |               8 |                8 |              0 |               1     |                 0.0333333 |              0.266667  |              1   |                  80 |           10 | [1, 7, 11, 13, 17, 19, 23, 29] | []                          |
| four grouped local tiles  |               4 |                8 |              0 |               1     |                 0.0666667 |              0.266667  |              0.5 |                  80 |           10 | [1, 7, 11, 13, 17, 19, 23, 29] | []                          |

## Interpretation

One detector is sparse and readable but incomplete.
One-hot local tiles are fragmented but complete.
Grouped local tiles trade compactness for coverage.
Redundancy separates efficient incompleteness from complete overlap.

## Generated figures

- `figures/10_feature_matrix_single_global_v2.png`
- `figures/11_feature_matrix_one_hot_tiles_v2.png`
- `figures/12_feature_matrix_grouped_tiles_v2.png`
- `figures/13_coverage_sparsity_tradeoff_v2.png`
- `figures/14_fragmentation_dilution_redundancy_summary_v2.png`
- `figures/15_redundancy_vs_coverage_v2.png`

## Generated data

- `data/03_sparse_feature_representation_summary_v2.csv`
- `data/03_single_global_feature_matrix_v2.csv`
- `data/03_onehot_tile_feature_matrix_v2.csv`
- `data/03_grouped_tile_feature_matrix_v2.csv`
