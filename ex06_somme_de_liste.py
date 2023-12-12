liste1 = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
liste2 = [-1, 12, 17, 14, 5, -9, 0, 18, -6, 0, 4, -13, 5, 7, -2, 8, -1]
#Créer une liste resultat dont chaque élément est la somme des éléments des liste 1 et
#2 de même index.
#On cherche la liste avec la plus courte longueur pour boucler dessus
small_liste = []
if len(liste1) > len(liste2):
    small_liste = liste2
else:
    small_liste = liste1
#la liste de résultat doit être une copie de la liste la plus longue
liste_resultat = []
if len(liste1) > len(liste2):
    liste_resultat = liste1[:]
else:
    liste_resultat = liste2[:]
#//Pour chaque élément de la liste jusqu'à la fin de la petite liste, on incrémente la valeur d'index i dans notre
#liste de résultats à celle de l'élément à l'index i de la petite liste.
for i in range(len(small_liste)):
    liste_resultat[i] += small_liste[i]
print(liste_resultat)
