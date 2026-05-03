import matplotlib.pyplot as plt

def plot_residue_distribution(density_dict):
    x = list(density_dict.keys())
    y = list(density_dict.values())
    plt.bar(x, y)
    plt.xlabel("Residue class")
    plt.ylabel("Density")
    plt.title("Mod30 residue density")
    plt.show()
