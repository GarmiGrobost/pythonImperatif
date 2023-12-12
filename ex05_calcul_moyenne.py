liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
#Calculez et AFFICHEZ la moyenne des valeurs de la liste
moyenne = sum(liste) / len(liste)
print(moyenne)
print("------------------------------------------------")
#Calculez et AFFICHEZ la moyenne des valeurs positives de la liste uniquement.
somme = 0
for i in liste:
    if i >= 0:
        somme += i
moyenne_vp = somme / len(liste)
print(moyenne_vp)

