numeros = [3.1, 2.8, 4.2, 4, 3.9, 2.78 ,3.2, 3.68, 4.01, 2.99]
lista = [5, 4, 6, 8, 9, 1, 7, 3, 6, 8, 5]
print(list(map(lambda numero: numero>3, numeros)))

print(list(map(lambda numero: 'par' if numero % 2 == 0 else 'impar', lista)))
print(list(map(lambda numero: numero if numero % 2 == 0 else numero+1, lista)))