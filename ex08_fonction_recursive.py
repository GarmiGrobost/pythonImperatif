liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
#Ecrire une fonction récursive qui retourne le nombre d’entiers dans la liste.
def compter_entiers(liste):
    total = 0
    for element in liste:
        if isinstance(element, int):
            total += 1
        elif isinstance(element, list):
            total += compter_entiers(element)
    return total
print(compter_entiers(liste))
