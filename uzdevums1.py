import math
# Ievade
a = float(input("Ievadi a: "))
b = float(input("Ievadi b: "))
c = float(input("Ievadi c: ")) # pietrūkst iekava

# Diskriminants
D = b**2 - 4*a*c

# Sakņu aprēķins
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2= (-b - math.sqrt(D)) / (2*a) # x2
    print("D = {D}, divas saknes: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"D = {D}, viena sakne: x = {x}")  # pēdiņas
else:
    print(f"D = {D}, nav reālu sakņu.")
