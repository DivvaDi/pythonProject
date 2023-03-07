res = ""
while True:
    w = input("Введите слово: ")
    if w == "stop":
        break
    res = res + w + " "
print("Результат: ", res.strip())