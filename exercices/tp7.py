
def evaluer_polynome(L : list , x : float) -> str : 

    P = ""
    for i in range(len(L)):
        #print(f"{L[i]} * {x}x^{i}")
        P = P + "1"
        
    return P


L = [-1,1,2]
M = [0,0,0,1]

print(evaluer_polynome(M,1))


#if L[i] != 0:
            #P = P + f" {x}^x{i}"