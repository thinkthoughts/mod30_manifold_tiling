# Mod30 Manifold Tiling  
### Residue-Class Feature Recovery (NMF vs Sparse Autoencoders)

This repository provides a **controlled finite benchmark** for studying feature recovery in representation learning.

We construct a synthetic system where the **ground truth structure is known**:
> persistent residue classes modulo 30.

We then evaluate how different models recover this structure.

---

## 🔗 Paper

📄 Full paper:  
`paper/paper.pdf`

---

## 🧠 Core Idea

integers → mod 30 → coprime residues → 8 lanes

true features = residue lanes

---

## 📊 Key Result

Sparsity ⇒ interpretability  
but NOT necessarily efficient capacity.

- NMF → efficient, high coverage  
- SAE → sparse, interpretable, but often incomplete or redundant

---

## 📁 Repository Structure

notebooks/
src/
figures/
paper/

---

## ▶️ Running the Code

### Colab
https://colab.research.google.com/github/thinkthoughts/mod30_manifold_tiling

### Local
pip install -r requirements.txt

---

## 📈 Metrics

- Coverage  
- Purity  
- Reconstruction error  
- Redundancy  
- Effective features  

---

## 🔬 Notebooks

01–06 progressively build experiments from structure → SAE → comparison

---

## 🔁 Reproducibility

Run notebooks 01 → 06 to regenerate figures.

---

## 📚 References

See `paper/references.bib`

---

## 👤 Author

Dan Hawkley
