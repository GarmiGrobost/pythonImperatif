#Ecrire un programme qui demande un nombre à l’utilisateur
#puis AFFICHEZ les 10 nombres qui suivent celui saisi par l’utilisateur
nombre = int(input("Entrez un nombre: "))
for i in range(nombre + 1, nombre + 11):
    print(i)
