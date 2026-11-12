def additionne (p :int , q : int ) -> int :
    """ Cette fonctions très compliquée renvoie la somme
    3 de deux entiers """

    return p+q


#quand le programme est appelé directement on peut voir ce qui suit
if __name__ == "main" :

    a : int =3
    b : int = 5
    print(f"Le test de la fonction additionne({a},{b}) "
    f"permet d’obtenir : {a} + {b} = {additionne(a,b)}.")
    assert additionne(1,1)==2