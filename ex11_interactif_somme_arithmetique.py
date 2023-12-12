#Ecrire un programme qui demande un nombre à l’utilisateur puis calcule la somme de tous les
#entiers compris entre 1 et ce nombre inclus.
nombre = int(input("Entrez un nombre: "))
somme = 0
for i in range(1, nombre+1):
    somme += i
print(nombre)
print(somme)
