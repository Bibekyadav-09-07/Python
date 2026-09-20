import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
diameter = 2 * radius

print("Area:", area)
print("Circumference:", circumference)
print("Diameter:", diameter)

print("Area rounded to 2 decimal places:", round(area, 2))
print("Circumference rounded to 2 decimal places:", round(circumference, 2))
