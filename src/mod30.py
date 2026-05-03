# src/mod30.py

MOD30_RESIDUES = [1, 7, 11, 13, 17, 19, 23, 29]

def mod30_index(n):
    return n % 30

def mod30_mask(n):
    return mod30_index(n) in MOD30_RESIDUES

def mod30_residues(n_max):
    return [n for n in range(2, n_max) if mod30_mask(n)]
