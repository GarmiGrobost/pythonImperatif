#Ecrire un programme qui demande un nombre à l’utilisateur qui doit être obligatoirement
#compris entre 1 et 10
nombre = 0
while nombre < 1 or nombre > 10:
    nombre = int(input("Entrez un nombre entre 1 et 10: "))
print("Le nombre saisi est:", nombre)
