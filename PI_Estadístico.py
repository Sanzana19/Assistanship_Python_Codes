import random
import math

n = int(input('Ingrese el número de evaluaciones:\n'))

in_circle = 0

for i in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if math.sqrt((x**2)+(y**2)) < 1:
        in_circle += 1

print(4*(in_circle/n))
