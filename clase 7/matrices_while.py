lista = [5, 4, 6, 8]

matriz = [lista, lista, lista]
#indices    0      1      2

matriz = [[5, 7, 6, 9], [3, 4, 2, 8], [7, 9, 6, 1]]
lista1 = matriz[0]
lista2 = matriz[1]
lista3 = matriz[2]
# matriz[1] = lista1
# print(matriz[0])
# print(matriz[0][0])
# print(matriz[1][0])
# matriz[-1][-1] = 5
# print(matriz[-1][-1])
# print(matriz)

i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        if matriz[i][j] > 4:
            print(matriz[i][j])
        j+=1    
    i+=1
