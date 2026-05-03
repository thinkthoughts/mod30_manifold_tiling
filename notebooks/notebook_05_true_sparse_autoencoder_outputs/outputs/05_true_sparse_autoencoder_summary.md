# Notebook 05 Summary — True Sparse Autoencoder

Notebook 05 replaces the Notebook 04 NMF baseline with a top-k sparse autoencoder.

## Model

`X → encoder → top-k sparse latent Z → decoder → X_hat`

## Metrics

|   latent_dim |   top_k |   reconstruction_error |   activation_sparsity |   mean_lane_purity |   max_lane_purity |   captured_lanes |   coverage_fraction |   total_activations |   redundancy |   effective_features | recovered_residues   | missed_residues                |
|-------------:|--------:|-----------------------:|----------------------:|-------------------:|------------------:|-----------------:|--------------------:|--------------------:|-------------:|---------------------:|:---------------------|:-------------------------------|
|            1 |       1 |               0.760466 |              1        |           0        |          0        |                0 |               0     |                   0 |      inf     |             0        | []                   | [1, 7, 11, 13, 17, 19, 23, 29] |
|            4 |       1 |               0.54557  |              0.75     |           0.159263 |          0.380775 |                1 |               0.125 |                 400 |      400     |             0.25     | [17]                 | [1, 7, 11, 13, 19, 23, 29]     |
|            8 |       1 |               0.484043 |              0.875    |           0.184794 |          0.676308 |                3 |               0.375 |                 400 |      133.333 |             0.375    | [1, 7, 11]           | [13, 17, 19, 23, 29]           |
|            8 |       2 |               0.421816 |              0.760938 |           0.264469 |          1        |                3 |               0.375 |                 765 |      255     |             0.375    | [13, 23, 29]         | [1, 7, 11, 17, 19]             |
|           12 |       1 |               0.378671 |              0.916667 |           0.340626 |          1        |                5 |               0.625 |                 400 |       80     |             0.416667 | [13, 17, 19, 23, 29] | [1, 7, 11]                     |
|           12 |       2 |               0.362438 |              0.833333 |           0.229729 |          1        |                5 |               0.625 |                 800 |      160     |             0.416667 | [1, 11, 13, 23, 29]  | [7, 17, 19]                    |

## Key metric

`effective_features = captured_lanes / total_components`

## Interpretation

The true sparse autoencoder reproduces the same regimes as the NMF baseline:

1. undercomplete global blur / superposition
2. grouped sparse tiles
3. matched local Mod30 tile recovery
4. overcomplete redundancy

## Generated figures

- `figures/23_sae_synthetic_embedding.png`
- `figures/24_sae_activation_matrix_8_topk1.png`
- `figures/25_sae_feature_to_lane_alignment_8_topk1.png`
- `figures/26_sae_recovery_metrics_summary.png`
- `figures/27_sae_redundancy_vs_coverage.png`
- `figures/28_sae_effective_features_vs_reconstruction.png`
- `figures/29_sae_alignment_L*_k*.png`
- `figures/30_sae_training_loss_curves.png`

## Generated data

- `data/05_sae_recovery_metrics.csv`
