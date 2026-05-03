# src/mod30.py

from math import gcd

# --- Base Mod30 (2 * 3 * 5) ---
MOD30 = 30
MOD30_RESIDUES = [1, 7, 11, 13, 17, 19, 23, 29]

# --- Future primorial extensions ---
# MOD210 = 2 * 3 * 5 * 7 = 210
# φ(210) = 48 residue lanes
# MOD2310 = 2 * 3 * 5 * 7 * 11 = 2310
# φ(2310) = 480 residue lanes

# Uncomment when needed:
# MOD210_RESIDUES = [r for r in range(1, 210) if gcd(r, 210) == 1]
# MOD2310_RESIDUES = [r for r in range(1, 2310) if gcd(r, 2310) == 1]


# --- Generic structure (scales to any modulus) ---
def mod_index(n, mod):
    return n % mod

def mod_mask(n, residues, mod):
    return mod_index(n, mod) in residues


# --- Mod30-specific helpers ---
def mod30_mask(n):
    return mod_mask(n, MOD30_RESIDUES, MOD30)

def mod30_residues(n_max):
    return [n for n in range(2, n_max) if mod30_mask(n)]


# --- Optional generator for future mods ---
def generate_coprime_residues(mod):
    return [r for r in range(1, mod) if gcd(r, mod) == 1]
