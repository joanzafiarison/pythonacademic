from math import cos, abs



### BASES
x : int = 3 
y : float = 3.142
z : str = "Hello, World!"
personne : str = "John"
age : int = 33

print(x == 3) # True
print(y == 3.142) # True
print(f"une valeur approchée de pi est {y:2f}") # une valeur approchée de pi est 3.14
print(z == "Hello, World!") # True 
print(f"Voici {personne}, il a {age} ans") # Voici John, tu as 33 ans


print(x ** 3) # 27 3 puissance 3 
print( 27 // 5) # 5 27 divisé par 5 = 5 reste 2

print(cos(3.14159)) # -1.0

print(abs(5 - 10) < 10**-6) # True




### chaines de caractèress
mot : str = "Hello, World!"
print (mot[0]) # H
# mot[0] ="h" Erreur



###PORTEES DES VARIABLES 


#built-in fourni par Python
#globale dans le module
#locale dans une fonction
i : int = 7
def multiplicateurRandom (a :int) : 
    global i # on indique que l'on veut utiliser la variable globale 'i' dans la fonction
    from random import randint
    b : int = randint(1,10) # variable locale à la fonction
    return a * b + i # on utilise la variable globale 'i' et la variable locale 'b' dans le calcul

a : int = 5 # variable globale dans le module
print(multiplicateurRandom(a)) # utilise la variable globale 'a' et une variable locale 'b' dans la fonction
