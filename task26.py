# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import random as r
def powerOfNumber(A, B):
    if (B==0):
        return 1
    else:
        return A*powerOfNumber(A,B-1)

a = int(input('Введите A '))
b = int(input('Введите B '))
print (powerOfNumber(a,b))
