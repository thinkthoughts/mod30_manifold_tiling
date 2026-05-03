# Notebook 05 Summary v2 — Sparse Autoencoder Feature Usage

Notebook 05 v2 trains a top-k sparse autoencoder and measures feature usage.

## Model

`X → encoder → top-k sparse latent Z → decoder → X_hat`

## New v2 diagnostics

- `dead_feature_fraction`
- `active_feature_fraction`
- `useful_feature_fraction`
- `redundant_feature_fraction`
- feature-level status: dead / redundant / useful

## Metrics

|   latent_dim |   top_k |   reconstruction_error |   activation_sparsity |   mean_lane_purity |   max_lane_purity |   captured_lanes |   coverage_fraction |   total_activations |   redundancy |   effective_features |   active_features |   dead_features |   useful_features |   redundant_features |   active_feature_fraction |   dead_feature_fraction |   useful_feature_fraction |   redundant_feature_fraction | recovered_residues   | missed_residues                |
|-------------:|--------:|-----------------------:|----------------------:|-------------------:|------------------:|-----------------:|--------------------:|--------------------:|-------------:|---------------------:|------------------:|----------------:|------------------:|---------------------:|--------------------------:|------------------------:|--------------------------:|-----------------------------:|:---------------------|:-------------------------------|
|            1 |       1 |               0.760466 |              1        |           0        |          0        |                0 |               0     |                   0 |      inf     |             0        |                 0 |               1 |                 0 |                    0 |                  0        |                1        |                  0        |                        0     | []                   | [1, 7, 11, 13, 17, 19, 23, 29] |
|            4 |       1 |               0.54557  |              0.75     |           0.159263 |          0.380775 |                1 |               0.125 |                 400 |      400     |             0.25     |                 2 |               2 |                 1 |                    1 |                  0.5      |                0.5      |                  0.25     |                        0.25  | [17]                 | [1, 7, 11, 13, 19, 23, 29]     |
|            8 |       1 |               0.484043 |              0.875    |           0.184794 |          0.676308 |                3 |               0.375 |                 400 |      133.333 |             0.375    |                 3 |               5 |                 3 |                    0 |                  0.375    |                0.625    |                  0.375    |                        0     | [1, 7, 11]           | [13, 17, 19, 23, 29]           |
|            8 |       2 |               0.421816 |              0.760938 |           0.264469 |          1        |                3 |               0.375 |                 765 |      255     |             0.375    |                 4 |               4 |                 3 |                    1 |                  0.5      |                0.5      |                  0.375    |                        0.125 | [13, 23, 29]         | [1, 7, 11, 17, 19]             |
|           12 |       1 |               0.378671 |              0.916667 |           0.340626 |          1        |                5 |               0.625 |                 400 |       80     |             0.416667 |                 5 |               7 |                 5 |                    0 |                  0.416667 |                0.583333 |                  0.416667 |                        0     | [13, 17, 19, 23, 29] | [1, 7, 11]                     |
|           12 |       2 |               0.362438 |              0.833333 |           0.229729 |          1        |                5 |               0.625 |                 800 |      160     |             0.416667 |                 5 |               7 |                 5 |                    0 |                  0.416667 |                0.583333 |                  0.416667 |                        0     | [1, 11, 13, 23, 29]  | [7, 17, 19]                    |

## Feature status summary

| setting   |   dead |   redundant |   useful |
|:----------|-------:|------------:|---------:|
| L1-k1     |      1 |           0 |        0 |
| L12-k1    |      7 |           0 |        5 |
| L12-k2    |      7 |           0 |        5 |
| L4-k1     |      2 |           1 |        1 |
| L8-k1     |      5 |           0 |        3 |
| L8-k2     |      4 |           1 |        3 |

## Interpretation

Sparse autoencoder capacity is not automatically useful capacity.
Some features are dead, some are redundant, and some align with persisting Mod30 lanes.

## Generated data

- `data/05_sae_recovery_metrics_v2.csv`
- `data/05_sae_feature_usage_v2.csv`
- `data/05_sae_feature_status_summary_v2.csv`
