n = input('Ingrese un número para saber si es feliz o no:\n')
used = []
while n not in used:
    addend = 0
    for i in range(len(n)):
        addend += int(n[i])**2
    used.append(n)
    n = str(addend)
if n == '1':
    print('Es un número felíz')
else:
    print('No es un número felíz')
