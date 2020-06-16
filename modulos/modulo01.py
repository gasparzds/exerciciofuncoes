def numero(n):
    for x in range(1, n + 1):
        contador = 1
        while True:
            print(x, end=' ')
            if contador == x:
                break
            contador = contador + 1
        print()