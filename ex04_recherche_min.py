liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
#Recherchez le plus petit élément de la liste et AFFICHEZ le.
min = liste[0]
for i in liste:
    if i < min:
        min = i
print(min)
