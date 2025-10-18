def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for x in range(1, 51):
    if es_primo(x):
        print(x)
