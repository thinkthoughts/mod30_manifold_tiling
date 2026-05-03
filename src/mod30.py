def mod30_residues(n_max):
    residues = [1,7,11,13,17,19,23,29]
    return [n for n in range(2, n_max) if n % 30 in residues]
