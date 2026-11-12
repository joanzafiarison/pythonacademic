

def codage_cesar( texte : str , k : int) -> str :
    """Renvoie le texte codé avec le code de César avec un décalage de k lettres"""
    texte_code : str = ""
    for lettre in texte : 
        if ord(lettre) >= ord("A") and ord(lettre)  <= ord("Z") : # si la lettre est une majuscule
            #texte_code += chr((ord(lettre) - ord("A") + k) % 26 + ord("A") 
            code = ord(lettre) - ord("A")
            code = (code +k ) % 26 
            texte_code += chr(code + ord("A"))
        elif lettre == " " : # si la lettre est un espace
            texte_code += " "
        else : # si la lettre est une minuscule
            texte_code += chr((ord(lettre) - ord("a") + k) % 26 + ord("a"))
    return texte_code


texte : str = "J'adore Le Chocolat."
k : int = 3

print(f"Le texte \"{texte}\" codé avec un décalage de {k} lettres est : \"{codage_cesar(texte, k)}\"")