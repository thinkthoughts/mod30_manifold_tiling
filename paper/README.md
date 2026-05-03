# Residue-Class Tiling as a Finite Analogue for Sparse Feature Recovery

## Abstract

We study feature recovery on a controlled finite system defined by Mod30 residue classes. Using a continuous embedding of integers constrained to residues coprime with 30, we compare two model classes: non-negative matrix factorization (NMF) and top-k sparse autoencoders (SAEs). We introduce metrics for structural recovery, including lane coverage, feature purity, redundancy, and effective feature utilization. While NMF achieves higher coverage and reconstruction efficiency, SAEs produce sparse and interpretable features but leave substantial latent capacity unused or redundant. These results demonstrate that sparsity-induced interpretability does not guarantee efficient representation, even in a system with known ground truth.

---

## 1. Introduction

Understanding how models recover structure from data is central to both machine learning and scientific modeling. In many real-world settings, ground truth structure is unknown, making evaluation difficult.

We instead construct a **finite, fully known system**:

* integers mapped under modulo 30
* filtered to residues coprime with 30
* forming 8 persistent residue classes

This provides a controlled environment where:

```text
true features = known residue lanes
```

We then embed this discrete system into a continuous space and test whether models can recover the underlying structure.

---

## 2. Mod30 Residue Manifold

Let:

```math
R = \{1, 7, 11, 13, 17, 19, 23, 29\}
```

These are the integers coprime with 30.

We define:

* input: integers ( n \in [1, N] )
* filter: ( n \mod 30 \in R )
* label: residue class ( r \in R )

This yields 8 persistent structural lanes.

---

## 3. Continuous Embedding

Each filtered integer is mapped to a continuous feature vector:

* circular coordinates:

  ```math
  (\cos(2\pi r/30), \sin(2\pi r/30))
  ```
* one-hot lane channels (with local overlap)
* additive noise

This produces a smooth manifold with local structure and controlled ambiguity.

---

## 4. Models

### 4.1 Non-Negative Matrix Factorization (NMF)

We factorize:

```math
X \approx W H
```

* ( W ): activations
* ( H ): components

NMF provides dense, linear decomposition.

---

### 4.2 Sparse Autoencoder (SAE)

We train a top-k sparse autoencoder:

```text
X → encoder → Z → top-k mask → decoder → X̂
```

* only k latent units active per sample
* enforces hard sparsity

---

## 5. Metrics

We evaluate both models using identical metrics.

### 5.1 Structural Recovery

* **coverage_fraction**

  ```text
  captured residue lanes / total lanes
  ```

* **mean_lane_purity**
  alignment of features with single residue classes

---

### 5.2 Reconstruction

* **reconstruction_error**
* **1 − reconstruction_error**

---

### 5.3 Capacity and Efficiency

* **redundancy**

  ```text
  total activations / captured lanes
  ```

* **effective_features**

  ```text
  captured_lanes / total_components
  ```

---

### 5.4 Feature Usage (SAE only)

We classify latent units:

```text
dead      = never active
useful    = active and lane-aligned
redundant = active but mixed
```

Metrics:

* dead_feature_fraction
* useful_feature_fraction
* redundant_feature_fraction

---

## 6. Results

### 6.1 NMF

* higher coverage
* strong reconstruction
* no dead features
* efficient use of components

### 6.2 SAE

* sparse activations
* interpretable features
* but:

  * dead latent units
  * redundant overlap
  * incomplete lane recovery

---

### 6.3 Key Comparison

| Property         | NMF    | SAE     |
| ---------------- | ------ | ------- |
| Coverage         | higher | lower   |
| Reconstruction   | better | worse   |
| Sparsity         | low    | high    |
| Dead features    | none   | many    |
| Redundancy       | low    | present |
| Interpretability | medium | high    |

---

## 7. Main Result

```text
Sparse constraints induce interpretability at the cost of capacity utilization.
```

More precisely:

```text
Dense factorization efficiently uses all components,
while sparse autoencoders leave significant latent capacity unused or redundant,
even when overcomplete.
```

---

## 8. Discussion

This system isolates a key tradeoff:

```text
efficiency vs interpretability
```

Even with known ground truth:

* increasing latent dimension does not guarantee recovery
* sparsity can prevent full utilization of capacity

This suggests caution when interpreting sparse models:

```text
interpretable ≠ complete
```

---

## 9. Conclusion

We introduced a finite Mod30 residue manifold as a controlled testbed for feature recovery.

We showed:

* NMF recovers structure efficiently
* SAEs produce interpretable but incomplete representations
* sparse models may fail to use available capacity

This provides a minimal setting where representation tradeoffs can be directly measured.

---

## 10. Reproducibility

All experiments are implemented as notebooks:

```text
01_mod30_residue_manifold.ipynb
02_local_tiling_vs_global_capture.ipynb
03_sparse_feature_analogy.ipynb
04_mod30_nmf_baseline.ipynb
05_true_sparse_autoencoder.ipynb
06_nmf_vs_sae_recovery_comparison.ipynb
```

---

## 11. Future Work

* extend to Mod210 and Mod2310
* analyze phase transitions in feature recovery
* study alternative sparsity constraints
* connect to high-dimensional feature learning

---
