sesion = True
opciones = ['1', '2', '3', '4', '5', '6', '7']
#   indices  0    1    2    3    4    5    6
while sesion:
    print('Digita el numero de la opción')
    for opcion in opciones:
        print(f'Opción {opcion}')
    option = input()
    if option == '6':
        result = input('Cuanto es 5 + 7? ')
        if result == '12':
            opcion = input('Digite la opción que desea poner como favorita')
            if int(opcion) >= 1 and int(opcion) <= 5:
                opciones.remove(opcion)
                opciones.insert(0,opcion)
                print(opciones)
        else:
            sesion = False
    elif option == '7':        
        print('Nos fuimos')
        sesion = False
