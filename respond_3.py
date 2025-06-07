n = int(input("Введи тризначне число: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a)
print(b)
print(c)
print(a + b + c)

print("__________________________")
deposit = float(input("Введи суму вкладу: "))
rate = float(input("Введи відсоткову ставку (наприклад, 5 для 5%): ")) / 100

year1 = deposit * (1 + rate)
year2 = year1 * (1 + rate)
year3 = year2 * (1 + rate)
year4 = year3 * (1 + rate)
year5 = year4 * (1 + rate)

print(f"Рік 1: {year1}")
print(f"Рік 2: {year2}")
print(f"Рік 3: {year3}")
print(f"Рік 4: {year4}")
print(f"Рік 5: {year5}")
