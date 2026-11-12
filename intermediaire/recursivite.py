
def affiche(debut,fin):
    an=debut
    while an<=fin :
        print(an)
        an=an+1


def affiche_rec (debut,fin) :
    if debut<=fin : # cas récursif : il reste au moins une année à afficher
        print(debut)
        affiche_rec(debut+1,fin) # appel récursif avec un paramètre plus petit
     #(le nombre d’années restant à afficher diminue)
    else : # le else n’est pas indispensable , par défaut la fonction se termine.
        return # renvoie None (c’est une procédure !)






def factoriel_rec(n : int) -> int :
    if n <= 1 :
        return 1
    else : 
        return n *factoriel_rec(n-1)





def U(n:int, u0 : int) -> float : 
    """
    U(n) =
    50, si n = 0 (cas d’arrêt)
    −0.5 × Un−1 + 1, sinon (relation de récurrence).
    """
    if n == 0 : 
        #print (f" U({n}) = {u0} ")
        return u0
    else : 
        
        appel = -0.5*U(n-1,u0)+1
        #print (f" U({n}) =  {appel:.4f}")
        return appel





#TODO PGCD récursive 180& 100 
def PGCD(nombre1 : int, nombre2 : int) -> int :
    pass


from intermediaire.bases_decimales import convert_base, hexaToDecimal , binaryToDecimal
#TODO changement de base d'un nombre voir décimales
def base_change(nombre : str, base1 : int ,base2 : int) -> str :
    #Hexa check si il y a un des caractères 0123456789ABCDEF
    #binary check si que 0 et 1 
    #hexa to decimal
    res : str = ""
    #10-2
    if base1 == 10 and base2 == 2 :
        #decimal_to_binary()
        res = convert_base(nombre, 2)

    if base1 == 10 and base2 == 16 :
        #decimal_to_binary()
        res = convert_base(nombre, 16)
    #2-10
    elif base1 == 2 and base2 == 10 :
        #binary_to_decimal()
        res = binaryToDecimal(nombre)
    #16-10
    elif base1 == 16 and base2 == 10:
        #hexadecimal_to_decimal()
        res = hexaToDecimal(nombre)
    else :
        #ow Exception("this conversion is not provided")
        res = ""
    
    return res

#print(base_change("20",10,2))

if __name__ == "main" :
    #affiche_rec(2020,2022)
    #print(f"factorielle de {n} : ",factoriel_rec(n))

    #u0 : int = 50
    #n : int =  5
    #print(f"suite récurrente avec n = {n} et u0 = {u0} : {U(n,u0)}") #


    #print(base_change("AF12",16,10))
    #print(base_change("44818",10,16))
    #print(base_change("101",2,10))
    #print(base_change("5",10,2))
