Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3


s= int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
d = s **2 - 4 * p
if s < 0 or p <= 0:
    print('Должны быть натуральные числа')
else:
    if d < 0:
        print(f'Не существует такой пары чисел')
    else:
        a = (s - (s ** 2 - 4 * p) ** 0.5) / 2
        b = (s + (s ** 2 - 4 * p) ** 0.5) / 2
        if a > 1000 or b > 1000:
            print('Числа должны быть меньше 1000')
        else:
            x = a - int(a)
            y = b - int(b)
            if x == 0 and y == 0:
                print(f'{s} {p} -> {int(a), int(b)}')
            else:
                print(f'Такой пары чисел нет')
