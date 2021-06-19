option = input(
"""
Menu de opciones
1- Entrar
2- Salir
""")

if option == '1':
    user = input('Ingrese el usaurio: ')
    password = input('Ingrese la contraseña: ')
    
    if user == 'Admin2021' and password == 'Una contraseña':
        print('Exito')