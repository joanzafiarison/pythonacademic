#tuples , str immuables, list mutables


#str 
chaine ='abcdefghij'
seq = "hello"
seq2 = "world"
extrait_1 = chaine[3] # extrait 'd'
extrait_2 = chaine[4:] # extrait 'efghij' (à partir de , vers la fin)
extrait_3 = chaine[:5] # extrait 'abcde' (du début , jusqu'à 5-1=4)
extrait_4 = chaine[:] # extrait tout.
extrait_5 = chaine[-3:-1] # extrait 'hi' (de -3 à -1-1=-2)


print( seq + " " + seq2) # hello world
print( seq * 3) # hellohellohello
print( seq[-1]) # o


nouveau_texte = "b" + seq[1:]
print(nouveau_texte) # Affiche "bello"


#tuples
t = (3, 4, "badour")

#listes

L : list = ["Tintin", "Astérix", "Lucky Luke"]
M = L #variable M est une référence à la liste L, donc la modification de M modifie aussi L
M[0] = "Spirou" # liste M est une référence à la liste L, donc la modification de M modifie aussi L
print(L) # Affiche ['Spirou', 'Astérix', 'Lucky Luke']

V = [''] * len(L)
print(V) # Affiche ['', '', ''] (une liste de 3 éléments vides)

N = [] # liste vide
for k in range(len(L)):
    N = N + [L[k]] # on ajoute un élément à la liste N
N[1] = "Obélix" # on modifie la liste N, mais pas la liste L
print(N) # Affiche ['Spirou', 'Obélix', 'Lucky Luke


def insere_somme(L: list, indice: int, x: int, y: int)-> None:
    """Modifie la liste L en place en insérant la somme de x et y à l’indice spécifié."""
    L[indice] = x + y # Modification directe de la liste

# Définition de la liste
Valeurs = [5, 7, 9]

# Appel de la fonction
insere_somme(Valeurs, 1, 10, 10) #ajoute la somme de 10 et 10 à l’indice 1 de la liste Valeurs

# Affichage du résultat
print(f"La liste modifiée est {Valeurs}") # Affiche : La liste modifiée est [5, 20, 9]



#pythonic

def is_in_collection(val, col) -> bool : 
    return val in col 

def is_in_collection_proc(val, col):
    for i in range(len(col)): # parcourt de la collection élément par élément
        if col[i] == val: # test d’égalité
            return True # renvoie True et casse la boucle dès qu’un élément correpond
    return False

def is_in_collection_while(val, col):
    index :int = 0 
    while index < len(col): 
        if val == col[index] :
            return True 
        index= index + 1
    return False

#TODO EXO Modifier les données pour que cela apparaisse en vrai
phrase = "Ulysse le héros grec." # chaîne , objet de type str
Liste_mot = ["Ulysse" , "le" , "héros" , "grec."] # liste, objet de type list
mon_tuple = ("Ulysse" , "le" , "héros" , "grec.") #tuple, objet de type tuple

print(is_in_collection("U", phrase)) #True
print(is_in_collection("héros", Liste_mot )) #True
print(is_in_collection_proc("Ulysse", mon_tuple)) #True
print(is_in_collection_while("Tarzan", Liste_mot )) #False


#liste iteration and modification

nombres = ["2", "9", "5", "1", "6"]

def liste_carre ( nombres : list) -> list :
    carres = [int(valeur)**2 for valeur in nombres] 
    return carres

def liste_carre_proc ( nombres : list) -> list :
    carres : list = []
    for entier in nombres :
        carre = int(entier)**2
        carres =  carres + [carre]
    return carres

print(liste_carre(nombres))

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

from bases.fonctions import polynome

def couple_2_liste (liste1 :list , liste2 : list):
    produits = [(x,y) for x in liste1 for y in liste2]
    print(f"for sur liste1 avant for sur liste2 , produits = {produits}")

print(couple_2_liste(liste1, liste2))
print([polynome(x) for x in liste1]) #utilise la fonction polynome sur chaque element de la liste



v=[1,2,3,4,5,6]
pair = [ x for x in v if x%2 ==0 ]
print(f"Les nombres sont {pair}.")  #affiche : Les nombres sont [2, 4, 6]

# Exemple 4 : Extraire les voyelles d’une chaîne
mot = "comprehension"
voyelles = [lettre for lettre in mot if lettre in "aeiouy"]

print("voyelles", voyelles)


nombres = [-2, -1, 0, 1, 2]
resultat = ["négatif" if x < 0 else "positif" if x > 0 else "zéro"
 for x in nombres]
print(f"Le signes des nombres est {resultat}.")



def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nombres = [2, 3, 4, 5, 6, 7, 8, 9, 10]
premiers = [f"{x} est premier" if est_premier(x)
    else f"{x} n’est pas premier" for x in nombres]
print(f" {premiers}.")