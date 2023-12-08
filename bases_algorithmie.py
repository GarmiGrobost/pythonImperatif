#Combinez une boucle for et un if afin d’afficher tous les nombres entiers pairs compris entre 0
#et 10 inclus.
for i in range(10):
    if i % 2 == 0:
        print(i)

#Combinez une boucle for et un if afin d’afficher tous les nombres entiers impairs compris
#entre 0 et 10 inclus.
print("**************************")
for i in range(10):
    if i % 2 != 0:
        print(i)
print("**************************")
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
#Affichez tous les éléments de cette liste grâce à une boucle
for l in liste:
    print(l)
print("**************************")
#Affichez uniquement les éléments positifs grâce à une boucle combinée à un if.
for l in liste:
    if l > 0:
        print(l)

#Trouvez un moyen de calculer le nombre d’éléments positifs et d’afficher ce nombre.
pos_count, neg_count = 0, 0
for l in liste:
    if l > 0:
        pos_count += 1
    else:
        neg_count += 1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)
