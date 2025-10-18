def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

count = 0
num = 2
primos = []
while count < 10:
    if es_primo(num):
        primos.append(num)
        count += 1
    num += 1
for p in primos:
    print(p)
