#petit module qui va effectuer des calculs et créer un fichier csv
#from gestion_fichier import readCsv 
from module.calculs import additionne

L=[ 4, 5, 6 ]
M=[ 33,44, 55 ]

def somme_liste(liste1 : list, liste2 : list) -> int : 
    somme : list = [0]*len(liste1)
    for i in range(len(liste1)) : 
        #somme = somme +  [additionne(liste1[i],liste2[i])]
        somme[i] = additionne(liste1[i],liste2[i])
    return somme


print(somme_liste(L,M))



#data = readCsv("etudiants.csv")

