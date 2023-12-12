liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
#Recherchez le plus grand élément de la liste et AFFICHEZ le
max = liste[0]
for i in liste:
    if i > max:
        max = i
print(max)
