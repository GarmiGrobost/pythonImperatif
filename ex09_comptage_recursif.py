#Réalisez une seconde fonction un peu adaptée par rapport à la précédente qui est
#capable de compter le nombre d’éléments qui sont compris entre un min et max
#donné.
liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
min = 10
max = 15
def compter_elements(liste, min, max):
    total = 0
    for elt in liste:
        if isinstance(elt, int) and min <= elt <= max:
            total += 1
        elif isinstance(elt, list):
            total += compter_elements(elt, min, max)
    return total
print(compter_elements(liste, min, max))
