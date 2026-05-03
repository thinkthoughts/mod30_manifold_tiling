# Notebook 06 Summary — NMF vs SAE Recovery Comparison

Notebook 06 compares NMF and top-k sparse autoencoder recovery on the same Mod30 continuous embedding benchmark.

## Combined metrics

| model   | setting    |   total_components |   reconstruction_error |   activation_sparsity |   mean_lane_purity |   max_lane_purity |   captured_lanes |   coverage_fraction |   total_activations |   redundancy |   effective_features |   active_features |   dead_features |   useful_features |   redundant_features |   active_feature_fraction |   dead_feature_fraction |   useful_feature_fraction |   redundant_feature_fraction | recovered_residues     | missed_residues                |
|:--------|:-----------|-------------------:|-----------------------:|----------------------:|-------------------:|------------------:|-----------------:|--------------------:|--------------------:|-------------:|---------------------:|------------------:|----------------:|------------------:|---------------------:|--------------------------:|------------------------:|--------------------------:|-----------------------------:|:-----------------------|:-------------------------------|
| NMF     | NMF-1      |                  1 |               0.732005 |              0        |           0.180648 |          0.180648 |                0 |               0     |                 400 |      inf     |             0        |                 1 |               0 |                 0 |                    1 |                  1        |                0        |                  0        |                    1         | []                     | [1, 7, 11, 13, 17, 19, 23, 29] |
| NMF     | NMF-4      |                  4 |               0.477987 |              0.52375  |           0.484292 |          0.542087 |                4 |               0.5   |                 762 |      190.5   |             1        |                 4 |               0 |                 4 |                    0 |                  1        |                0        |                  1        |                    0         | [7, 13, 19, 29]        | [1, 11, 17, 23]                |
| NMF     | NMF-8      |                  8 |               0.371172 |              0.636875 |           0.47531  |          0.741074 |                6 |               0.75  |                1162 |      193.667 |             0.75     |                 6 |               2 |                 6 |                    0 |                  0.75     |                0.25     |                  0.75     |                    0         | [1, 7, 13, 17, 23, 29] | [11, 19]                       |
| NMF     | NMF-12     |                 12 |               0.34603  |              0.693958 |           0.332351 |          0.750302 |                6 |               0.75  |                1469 |      244.833 |             0.5      |                 7 |               5 |                 6 |                    1 |                  0.583333 |                0.416667 |                  0.5      |                    0.0833333 | [1, 7, 13, 17, 23, 29] | [11, 19]                       |
| SAE     | SAE-L1-k1  |                  1 |               0.760466 |              1        |           0        |          0        |                0 |               0     |                   0 |      inf     |             0        |                 0 |               1 |                 0 |                    0 |                  0        |                1        |                  0        |                    0         | []                     | [1, 7, 11, 13, 17, 19, 23, 29] |
| SAE     | SAE-L4-k1  |                  4 |               0.54557  |              0.75     |           0.159263 |          0.380775 |                1 |               0.125 |                 400 |      400     |             0.25     |                 2 |               2 |                 1 |                    1 |                  0.5      |                0.5      |                  0.25     |                    0.25      | [17]                   | [1, 7, 11, 13, 19, 23, 29]     |
| SAE     | SAE-L8-k1  |                  8 |               0.484043 |              0.875    |           0.184794 |          0.676308 |                3 |               0.375 |                 400 |      133.333 |             0.375    |                 3 |               5 |                 3 |                    0 |                  0.375    |                0.625    |                  0.375    |                    0         | [1, 7, 11]             | [13, 17, 19, 23, 29]           |
| SAE     | SAE-L8-k2  |                  8 |               0.421816 |              0.760938 |           0.264469 |          1        |                3 |               0.375 |                 765 |      255     |             0.375    |                 4 |               4 |                 3 |                    1 |                  0.5      |                0.5      |                  0.375    |                    0.125     | [13, 23, 29]           | [1, 7, 11, 17, 19]             |
| SAE     | SAE-L12-k1 |                 12 |               0.378671 |              0.916667 |           0.340626 |          1        |                5 |               0.625 |                 400 |       80     |             0.416667 |                 5 |               7 |                 5 |                    0 |                  0.416667 |                0.583333 |                  0.416667 |                    0         | [13, 17, 19, 23, 29]   | [1, 7, 11]                     |
| SAE     | SAE-L12-k2 |                 12 |               0.362438 |              0.833333 |           0.229729 |          1        |                5 |               0.625 |                 800 |      160     |             0.416667 |                 5 |               7 |                 5 |                    0 |                  0.416667 |                0.583333 |                  0.416667 |                    0         | [1, 11, 13, 23, 29]    | [7, 17, 19]                    |

## Best settings by model

| model   | setting    |   total_components |   reconstruction_error |   activation_sparsity |   mean_lane_purity |   max_lane_purity |   captured_lanes |   coverage_fraction |   total_activations |   redundancy |   effective_features |   active_features |   dead_features |   useful_features |   redundant_features |   active_feature_fraction |   dead_feature_fraction |   useful_feature_fraction |   redundant_feature_fraction | recovered_residues     | missed_residues   |   score |
|:--------|:-----------|-------------------:|-----------------------:|----------------------:|-------------------:|------------------:|-----------------:|--------------------:|--------------------:|-------------:|---------------------:|------------------:|----------------:|------------------:|---------------------:|--------------------------:|------------------------:|--------------------------:|-----------------------------:|:-----------------------|:------------------|--------:|
| NMF     | NMF-8      |                  8 |               0.371172 |              0.636875 |           0.47531  |          0.741074 |                6 |               0.75  |                1162 |      193.667 |             0.75     |                 6 |               2 |                 6 |                    0 |                  0.75     |                0.25     |                  0.75     |                            0 | [1, 7, 13, 17, 23, 29] | [11, 19]          | 1.79164 |
| SAE     | SAE-L12-k1 |                 12 |               0.378671 |              0.916667 |           0.340626 |          1        |                5 |               0.625 |                 400 |       80     |             0.416667 |                 5 |               7 |                 5 |                    0 |                  0.416667 |                0.583333 |                  0.416667 |                            0 | [13, 17, 19, 23, 29]   | [1, 7, 11]        | 1.44112 |

## Interpretation

NMF and SAE recover Mod30 residue-tile structure differently.

- NMF: dense linear factorization, smooth recovery, no explicit top-k sparsity.
- SAE: sparse latent activations, useful interpretability, but dead and redundant capacity can appear.

## Generated figures

- `figures/35_shared_mod30_embedding.png`
- `figures/36_nmf_vs_sae_coverage_vs_reconstruction.png`
- `figures/37_nmf_vs_sae_sparsity_vs_coverage.png`
- `figures/38_nmf_vs_sae_effective_dead_redundant.png`
- `figures/39_nmf_vs_sae_redundancy_vs_coverage.png`
- `figures/40_nmf_alignment_8_components.png`
- `figures/41_sae_alignment_L8_k1.png`
- `figures/42_nmf_activation_matrix_8.png`
- `figures/43_sae_activation_matrix_L8_k1.png`

## Generated data

- `data/06_nmf_vs_sae_combined_metrics.csv`
- `data/06_best_settings_by_model.csv`
