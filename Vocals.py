word = input('Escribe la palabra a evaluar:\n')

vocals = set()

for i in range(len(word)):
    if word[i] == 'A' or word[i] == 'a' or word[i] == 'Á' or word[i] == 'á':
        vocals.add('a')
    if word[i] == 'E' or word[i] == 'e' or word[i] == 'É' or word[i] == 'é':
        vocals.add('e')
    if word[i] == 'I' or word[i] == 'i' or word[i] == 'Í' or word[i] == 'í':
        vocals.add('i')
    if word[i] == 'O' or word[i] == 'o' or word[i] == 'Ó' or word[i] == 'ó':
        vocals.add('o')
    if word[i] == 'U' or word[i] == 'u' or word[i] == 'Ú' or word[i] == 'ú':
        vocals.add('u')

if len(vocals) == 5:
    print('\nLa palabra contiene todas las vocales.')
else:
    print('\nLa palabra no contiene todas las vocales.')