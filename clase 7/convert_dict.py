tripulantes = ['Sergio', 'David', 'Eider', 'Lina']

tripulantes_dict = { tripulante : '5' for tripulante in tripulantes }
tripulantes_dict = dict.fromkeys(tripulantes, 5)
tripulantes_dict = dict(zip(tripulantes, range(0,len(tripulantes))))
tripulantes_dict = dict(zip(tripulantes, tripulantes))

print(list(tripulantes_dict.keys()))
print(tripulantes_dict.values())