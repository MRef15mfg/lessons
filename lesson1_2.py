import math
name = input("Enter yout name : ")
print(f"Hello {name}!")


w = input("Enter weight : ")
h = input("Enter height : ")

print(f"Площа прямокутника {w} та {h} = {float(w) * float(h)} см^2")

radius = float(input("radius : "))
print(f"Площа кола з радіусом {radius} = {math.pi * radius ** 2} см^2")


c = float(input("Введи температуру в Цельсіях: "))
f = c * 9 / 5 + 32
print("Температура в Фаренгейтах:", f)

