
a: int = -2
if a > 0: #Le programme teste la condition
    print(a, "est positif.")
elif a == 3 :
    print(a, "est égal à 3.")
else:
    print(a, "est négatif ou nul.")
    if a == 0 :
        print(a, "est nul.")


#Étape 1 : définition des variable (et description de leur type !)
phrase : str = "J’adore le chocolat."
nombre_o : int = 0 # initialisation du compteur pour le nombre de o trouvé.
indice : int = 0 # indice de position pour parcourir la chaine

#Étape 2
while indice < len(phrase) :
    if phrase[indice] == 'o': # test du caractère pour voir si il correspond à la recherche
        nombre_o = nombre_o + 1
    indice = indice + 1
#Étape 3
print(f" La phrase \"{phrase}\" contient {nombre_o} fois la lettre ’o’.")