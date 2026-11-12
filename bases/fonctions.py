
def polynome_custom (x: float) -> float:
    """Calcul le polynome 3x^2 + 2x + 1"""
    return 3 * x ** 2 + 2 * x + 1

def polynome(x :int)-> int :
    return x**2

def cube (x:float) -> float:
    """Calcul le cube d'un nombre"""
    return x ** 3

def volumeSphere (r: float) -> float:
    """Calcul le volume d'une sphere de rayon r"""
    pi :float = 3.14159
    rCube : float = cube(r)
    return 4/3 * pi * rCube

print(polynome_custom(2)) # 17
print(">>>>")
print(cube(2)) # 8
print(">>>>")
print(volumeSphere(2)) # 33.51032163876007