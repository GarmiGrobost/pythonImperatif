liste1 = [1, 15, -3, 8, 7, 4, -2, 28, -1, 17, 2, 3, 0, 14, -4]
liste2 = [3, -8, 17, 5, -1, 4, 0, 6, 2, 11, -5, -4, 8]
#AFFICHEZ le nombre de valeurs communes aux 2 listes. On peut déjà voir que les
#valeurs 3 et 8 sont communes aux 2 listes, mais combien y en a-t-il au total ?
valeurs_communes = []
for i in range(len(liste1)):
    if liste2.__contains__(liste1[i]):
        valeurs_communes.append(liste1[i])
print(valeurs_communes)
nombre_val = len(valeurs_communes)
print(nombre_val)
