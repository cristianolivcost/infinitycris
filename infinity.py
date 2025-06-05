def maior_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b 
    else:
        return c

print(maior_numero(10, 5, 7))  
print(maior_numero(3, 15, 9))  
print(maior_numero(2, 8, 20)) 