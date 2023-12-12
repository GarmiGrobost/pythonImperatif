#- Tant que l’utilisateur ne saisit de nombre compris entre 1 et 10 le programme
#redemande un nombre
# Si le nombre est bien entre 1 et 10, le programme LOGUE la table de multiplication de
#ce nombre puis s’arrête.
nombre = 0
while nombre < 1 or nombre > 10:
    nombre = int(input("Entrez un nombre entre 1 et 10: "))
for i in range(1, 11):
    print(f"{nombre} * {i} = {nombre * i}")
