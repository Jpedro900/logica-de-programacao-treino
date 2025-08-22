#Maximo de Tres

def max_three(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c
