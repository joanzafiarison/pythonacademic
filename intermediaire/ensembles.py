ens = {1, 2, 3, 1, 2} # Ni répétition   Résultat : {1, 2, 3}
print({1, 2, 3} == {3, 1, 2}) # ni ordre
# Résultat : True

print({False,"bleu", 2, "bleu"} == {2, False, "bleu", 2, 2})


print(type({}))
print(type(set()))


#Ensemble En mathématiques, A est inclus dans B est équivalent à : tout élément de A appartient à B :
#A ⊆ B ≡ ∀x ∈ A, x ∈ B

A = {22, "Salut"}
B = {22, 31.2, "Salut", True}
print(31.2 in A, 31.2 in B)

#A inclus dans B
def inclusion(A, B):
    for x in A:
        if not (x in B):
            return False
    return True

A = {22, "Salut"}
B = {22, 31.2, "Salut", True}
print(inclusion(A, B)) # Résultat : True
print(inclusion(B, A)) # Résultat : False
print(inclusion(A, A)) # Résultat : True

ens_rep = {2, 2, 1, 1, 3, 3, 2, 1, 2, 3}
# cardinal = nombre d'éléments d'un ensemble
def cardinal(E):
    c = 0
    for x in E: # tous les éléments sont parcourus
        c = c + 1
    return c

print(f" nombre d'element unique dans ens_rep {cardinal(ens_rep)}") # Résultat : 3
print(ens_rep) # Résultat : {1, 2, 3}
print(f"nombre d'element dans une ensemble vide {cardinal(set())}")


#construire un ensemble 

print([ x % 10 for x in range(100) if x%6 == 0  ]) #récupérer les x en récupérant le reste d'une division par 10 de tous les multiples de 6 dans la range 1-100
print({ x % 10 for x in range(100) if x%6 == 0  }) #avec un ensemble on récupère uniquement les valeurs uniques


# ajouter des éléments à un ensemble
E = {1, 2, 3}
E.add(12)
print(E) # Résultat : {1, 2, 3, 12}
E.add(1)
print(E) # pas de changement
E.remove(3)
print(E)



def union(A, B):
    E = set() # ensemble vide
    for x in A:
        E.add(x)
    for x in B:
        E.add(x)
    return E

A = {1, 2, 3, 4}
B = {2, 4, 6, 8}

print(union(A, B))


print(A | B) # Résultat : {1, 2, 3, 4, 6, 8}
print(A & B) # Résultat : {2, 4}
print(A - B) # Résultat : {1, 3}

{"123", "abc"} # Résultat : {’123’, ’abc’}
{(1, 2, 3), ('a', 'b', 'c')} # Tuple : immuable Résultat : {(1, 2, 3), (’a’, ’b’, ’c’)}
#{[1, 2, 3], ['a', 'b', 'c']} # TypeError: unhashable type: ’list’ (list est mutable)
#{{1, 2, 3}, {'a', 'b', 'c'}} # TypeError: unhashable type: ’set’ (set est mutable)




#dico
partiel = {"Alice": 15, "Bob": 13, "Charline": 9}
#print(partiel["Gustave"]) # KeyError: ’Gustave’
print("Gustave" in partiel) # Résultat : False

def has_note(student : str) -> str :
    if  student in partiel :
        return str(partiel[student])
    else :
        return "ABS"
student = "Alice"
student2 = "Gustave"
print(f" l'élève {student} a eu {has_note(student)}")
print(f"l élève {student2} a été {has_note(student2)}")


print(partiel.get("Alice", "ABS")) # Résultat : 15 car la clé "Alice" existe
print(partiel.get("Gustave", "ABS"))
partiel["Gustave"] = "10" #add a key with note
partiel.pop("Bob")
print(partiel)


def parcours(dico):
    for k in dico:
        v = dico[k]
        print(f"{k} ({v})")

mousquetaires = dict()
mousquetaires["Athos"] = 1615
mousquetaires["Porthos"] = 1617
mousquetaires["Aramis"] = 1620
mousquetaires["d’Artagnan"] = 1615


print(parcours(mousquetaires))