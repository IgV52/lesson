print("__Введение__Задание.")
print("Привет мир!")
print("Привет программист!")
print(2 + 2)
print(10 / 3)
print()
print("__Переменные__Задание.")
name = "Ivan"
print(name)
print()
print("__Простые типы данных__Практика: числа.")
v = int(input("Введите число от 1 до 10: "))
print(v+10)
print("__Простые типы данных__Практика: строки.")
name_a = input("Введите ваше имя: ")
print(f"Привет, {name_a}! Как дела?")
print("__Простые типы данных__Практика: приведение типов.")
print(float("1.0"))
print(int("2"))
print(bool(1))
print(bool(""))
print(bool(0))
print()
print("__Списки__Задание.")
num = [3,5,7,9,10.5]
print(num)
num.append("Python")
print(len(num))
print()
print("__Словари__Задание.")
info_temp = {"city" : "Москва", "temperature" : 20}
print(info_temp["city"])
info_temp["temperature"] = info_temp["temperature"] - 5
print(info_temp)
print(info_temp.get("country", "Россия"))
info_temp["date"] = "27.05.2019" 
print(len(info_temp))
print()
print("__Функции__Задание.")
def get_summ(one, two, delimiter="&"):
    temp = one + delimiter + two
    return temp.upper()
print(get_summ("Learn", "Python"))
print()
def format_price(price):
    price = round(price)
    return f"Цена: {price} руб."
print(format_price(56.24))