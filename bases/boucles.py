a : str = "choucroute"
indice : int = 0

while indice < len(a) :
    #print("s[", indice, "] =", a[indice])
    indice += 1

print("fin du code")

def binaryConversion(n : int) -> str: 
    """Convertit un nombre entier en binaire"""
    binaire : str = ""
    if n == 0:
        return "0"
    while n != 0:
        reste : int = n % 2
        binaire  = str(reste) + binaire
        n = n //2 #on divise n par 2 et on garde le quotient pour la prochaine itération

    return binaire

decimal : int = 4
binary : str = binaryConversion(decimal) # 1010
print(f"Le nombre {decimal} en binaire est {binary}")


def print_ranges():
    print(list(range(5))) # 0,1,2,3,4
    print(list(range(1,5))) # 1,2,3,4
    print(list(range(10,1,-2))) # 10,8,6,4,2
    for entier  in range(1, 10 , 2): # de 1 à 10 inclus à pas de 2
        print(entier, "au carré =", entier ** 2)





def for_continue_break():
    for x in range(1, 11):
        if x == 5:
            break # ou continue , dans ce cas on skip l'itération et on passe à la suivante
        print(x, end=" ")
    print("La suite ...")


def tableau_nombre():

    for ligne in range(5):
        for colonne in range(10):
            print(ligne, colonne, sep='', end=" ")
        print()

def tableau_nombre_inverse():
    for colonne in range(10):
        for ligne in range(5):
            print(ligne, colonne, sep='', end=" ")
        print()

def affiche_ligne(ligne: int):
    for colonne in range(10):
        nombre : int = ligne *10 +colonne
        print(f"{nombre:02d}", end=" ")


def tableau_nombre_avec_fonction(): #utilisation d'une fonction pour afficher une ligne
    for ligne in range(5):
        affiche_ligne(ligne)
        print()

#tableau_nombre()
#tableau_nombre_inverse()

tableau_nombre_avec_fonction()