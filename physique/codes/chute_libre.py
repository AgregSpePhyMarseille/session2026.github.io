import math

def chute_libre(h):
    g = 9.81  # accélération due à la gravité (m/s²)
    t = math.sqrt(2 * h / g)
    return t

hauteur = 10  # en mètres
temps = chute_libre(hauteur)
print(f"Temps de chute pour {hauteur}m : {temps:.2f} secondes")