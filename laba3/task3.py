w = input("Введите слово: ")
for i in w:
    if (i=="Ф") or (i=="ф"):
        print("Ого! Вы ввели редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово...")
        break