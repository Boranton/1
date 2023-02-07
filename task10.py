Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2


from random import randint

n = int(input("Введите количество монеток: "))
list = []
orel = 0
reshka = 0

def ListGenerate(n):
    for i in range(n):
        if i < n:
            list.append(randint(0, 1))
    return list

def ChangePositionMonedas(list, orel, reshka):
    for i in range(len(list)):
        if list[i] == 1:
            orel += 1
    print("Минимальное количество перекладываний:"
          , orel if orel < len(list) - orel else (len(list)) - orel)

print("Список перевернутых и неперевернутых монеток:", ListGenerate(n))
ChangePositionMonedas(list, orel, reshka)
