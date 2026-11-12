#TODO Bases décimales conversion binary ->  decimal OK /  hexa to decimal OK
# decimal to hexa OK , decimal to binary OK



def hexConversion(nombre : int) -> str : 

    hex_string = '0123456789ABCDEF'
    return hex_string[nombre]

def decimalConversion(character : str) -> int :
    hex_string = '0123456789ABCDEF'
    i = hex_string.index(character)
    return i

def convert_base(n : str, base : int) -> str : 
    """convertis un nombre en base 10 en base 2, 8 ou 16"""
    """1789 base 10  = 1*10^3 + 7*10^2 + 8*10^1 + 9*10^0 = 1*16^2 + 6*16^1 + 13*16^0 = 6*8^2 + 5*8^1 + 5*8^0 = 11011110101 base 2"""
    """approche récursive : on divise le nombre par la base et on récupère le reste, puis on recommence avec le quotient jusqu'à ce que le quotient soit 0"""
    #print(n)
    if int(n)//base == 0:
        res = int(n) % base
        
        if int(n) >= 10 :
            #print(hexConversion(res))
            return hexConversion(res)
        else :
            return str(res)

    #print (str(int(n)//base))
    reste = str(int(n) % base)
    if base == 16 : 
          reste = hexConversion(int(n) % base)
    acc = convert_base(str(int(n)//base),base) + reste #quotient + reste
    
    return acc 


def hexaToDecimal(hexa :str) -> str :
    """
        Convert hexaToDecimal
        AF ==> A ->  10 x16^1 ... F -> 15x16^0
    """
    res: int = 0
    n = len(hexa)
    for k in range(n) : 
        #int(decimalConversion(hexa[k]))
        #print(hexa[k])
        #print(decimalConversion(hexa[k]))
        #print(16**(n-k-1))
        hex_pow = 16**(n-k-1)
        res = res + decimalConversion(hexa[k])*hex_pow
    return res

def binaryToDecimal(binary_str : str) -> str : 
    """
        Convert binary to decimal
        101 => 1*2^2+0*2^1*2^0 => 4 + 1
    """
    res : int = 0 
    n : int = len(binary_str)
    for k in range(n):
        res = res + int(binary_str[k])*(2**(n-k-1))
    return res

# modulo = reste division euclidienne
# // division entière = quotient division euclidienne
""" on résoud d'abord 
    convert_base("789", 2)
    convert_base("394", 2) + "1"
    convert_base("197", 2) + "0" + "1"
    ...........................
    convert_base("3", 2) + "0" + "0" + "1" + "0" + "1" + "0" + "1"
    La pile 'remonte' et on rajoute str(int(n) % base) à chaque fois, ce qui donne 1100010101
"""


if __name__ == "main" :

    assert( convert_base("789", 2) == "1100010101")
    assert(convert_base("1789", 10) == "1789")
    assert(convert_base("9", 2) == "1001")
    # bin(9)  # '0b1001' decimal to binary

    #assert("0o"+convert_base("111",8) == oct(111))
    #print("0o"+convert_base("111",8))
    #print(oct(111))
    #assert(convert_base("20",16) == hex(20))
    #assert(convert_base("FA12", 16) == "64018")
    print(convert_base("44818",16))
    print(convert_base("175",16))
    print(hexaToDecimal("AF12"))
    #print(int ("AF12",16)) # 175  hexadecimal to decimal AF12 --- 44818


    #hex(20)  # '0x14' decimal to hexadecimal
    #print(convert_base("20",16)) 
    #bin (int("AF",16)) # '0b10101111'  hexadecimal to binary
    print(int("101",2)) #5 binary to decimal
    print(binaryToDecimal("101")) #5
