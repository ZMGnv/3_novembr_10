import math
# Ievade
a = float(input("Ievadi a: "))
b = float(input("Ievadi b: "))
c = float(input("Ievadi c: ")

# Diskriminants
D = b**2 - 4*a*c

# Sakņu aprēķins
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x = (-b - math.sqrt(D)) / (2*a)
    print(f"D = {D}, divas saknes: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(fD = {D}, viena sakne: x = {x}")
else:
    print(f"D = {D}, nav reālu sakņu.")
