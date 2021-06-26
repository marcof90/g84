def palindromo(word):
    word = word.lower().replace(' ','')
    if word == word[::-1]:
        return f'{word} es palindromo'
    else:
        return f'{word} no es palindromo'

es_palindromo = lambda word: 'Si es' if word.lower().replace(' ','') == word.lower().replace(' ','')[::-1] else 'No es'

print(es_palindromo('La tele letal'))