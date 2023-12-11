#Réalisez une fonction qui retourne la somme des nombres pairs d’une liste
def somme_nb_pairs(liste):
    somme = 0
    for i in liste:
        if i % 2 == 0:
            somme += i
    return somme

liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
print("La somme des nombres pairs :", somme_nb_pairs(liste))
#Réalisez une fonction qui retourne si oui ou non la chaine de caractères passée en
#paramètre est un palindrome
def is_palindrome(chaine):
    chaine_inverse = chaine[::-1]
    if chaine == chaine_inverse:
        return True
    else:
        return False
chaine = "ratar"
if is_palindrome(chaine):
    print(chaine, "est palindrome")
else:
    print(chaine, " n'est pas palindrome")
print("***********************************")

#Réalisez une fonction qui prend 3 paramètres : un min, un max et une liste
def recherche_min_max(min, max, liste):
    nouvelle_liste = []
    for element in liste:
        if min <= element <= max:
            nouvelle_liste.append(element)
    return nouvelle_liste
#Cette fonction retourne une seconde liste contenant tous les nombres de la liste
#d’origine compris entre le min et le max
min = 5
max = 15
nouvelle_liste = recherche_min_max(5, 15, liste)
print("La nouvelle liste est :", nouvelle_liste)
print("********************")
#Réalisez une fonction qui calcule la moyenne des éléments d’une liste
def calcul_moyenne(liste):
    somme = 0
    for num in liste:
        somme += num
    moyenne = somme // len(liste)
    return moyenne
print("La moyenne de la liste :", calcul_moyenne(liste))

