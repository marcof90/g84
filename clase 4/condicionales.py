edad = input('Digite la edad')
edad = int(edad)
if edad > 20:
    print('Categoria profesional')
elif edad >= 18:
    print('Categoria Sub 20')
elif edad >= 15:
    print('Categoria Juvenil')
elif edad >= 10:
    print('Categoria Infantil')
else:
    print('Edad invalida')