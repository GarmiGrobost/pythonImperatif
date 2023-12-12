#Ecrire un programme qui demande 10 nombres à un utilisateur, puis affiche le plus grand de
#ces nombres.
nombres = []
for i in range(10):
    nombre = int(input(f"Entrez le nombre {i + 1}: "))
    nombres.append(nombre)
plus_grand = max(nombres)
print("Le plus grand nombre est:", plus_grand)
