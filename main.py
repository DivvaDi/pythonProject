nomer = int(input("Введите номер места: "))
nm = 1 <= nomer <= 54
vm = (nomer % 2) == 0
mm = 37 <= nomer <= 54
if not nm:
    print("Неверные данные!")
else:
    print("Информация о месте: ")
    if vm and mm:
        print("Верхнее боковое")
    if vm and not mm:
        print("Верхнее купе")
    if not vm and mm:
        print("Нижнее боковое")
    if not vm and not mm:
        print("Нижнее купе")
