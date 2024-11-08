# Description: Given a list of n integers, determine if it is possible to obtain a strictly increasing sequence by removing no more than one element from the list.

cases = int(input())

for _ in range(cases):
    n = int(input())
    cadena = input()
    numeros = cadena.split()[:n]
    numeros = [int(x) for x in numeros]
    if n == 2:
        if (numeros[1] + 1 == numeros[0]) or (numeros[1] - 1 == numeros[0]) or (numeros[1] == numeros[0]):
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
