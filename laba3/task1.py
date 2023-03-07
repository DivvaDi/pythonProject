N = int(input("Введите количество слов: "))
res = ""
for i in range(0, N):
    w = input("Введите слово: ")
    res = res+w
    if i != N-1:
        res = res+" "
print("Результат: ", res)