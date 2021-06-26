def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def operar(operacion, num1, num2):
    return operacion(num1, num2)

def funcion_superior(funcion_param):
    return funcion_param()

def decir_hola():
    return 'hola'

def decir_mundo():
    return 'mundo'

#print(funcion_superior(decir_hola))
funcion_superior(decir_mundo)