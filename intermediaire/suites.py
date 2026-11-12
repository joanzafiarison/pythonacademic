def suite_rec (n : int) -> int:
    """Renvoie le n-ième terme de la suite définie par :
    u_0 = 1
    u_n = 2 * u_(n-1) + 1 pour n >= 1
    """
    if n == 0:
        return 1
    else:
        return 2 * suite_rec(n - 1) + 1





