def concentration(n, V):
    """
    Calcule la concentration molaire.

    n : quantité de matière (mol)
    V : volume de solution (L)
    """
    return n / V


# Exemple d'utilisation
n = 0.25   # mol
V = 0.50   # L

C = concentration(n, V)

print(f"Concentration : {C:.2f} mol/L")