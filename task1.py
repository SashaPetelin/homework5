# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


# 1.ЧЕЛОВЕК ПРОТИВ ЧЕЛОВЕКА

import random

name1 = input("Введите имя первого игрока: ")
name2 = input("Введите имя второго игрока: ")

dict = {1: name1, 2: name2}

first_num = random.choice(list(dict.keys()))
first_name = dict.get(first_num)
print(f"Первым начинает игрок {first_num}:'{first_name}'")

amount = 2021
sum1 = 0
sum2 = 0
while amount>0:
    if first_num == 1:     # если начинает первый игрок
        if amount<=28:                                                         # Проводим проверку вводимого числа первого игрока
            print(f"Игрок '{name1}' вводит число от 1 до {amount}")       
            count1 = int(input())
            while (count1<1 or count1>amount):
                print(f"Число должно быть в промежутке от 1 до {amount}!")
                count1 = int(input())
        else:
            print(f"Игрок '{name1}' вводит число от 1 до 28")
            count1 = int(input())                                                            
            while (count1<1 or count1>28):                                       # Проводим проверку вводимого числа второго игрока            
                print("Число должно быть в промежутке от 1 до 28!")
                count1 = int(input())
        sum1 += count1
        amount -= count1
        if amount == 0:
            print(f"ИГРОК '{name1}' ПОБЕДИЛ С РЕЗУЛЬТАТОМ {sum1}! ПОЗДРАВЛЯЕМ!")
        else:
            print(f"Количество конфет у игрока '{name1}' {sum1} шт.")
            print("Остаток конфет = ", amount)
        print("-----------------------------------")

        if amount<=28:
            print(f"Игрок '{name2}' вводит число от 1 до {amount}")       
            count2 = int(input())
            while (count2<1 or count2>amount):
                print(f"Число должно быть в промежутке от 1 до {amount}!")
                count2 = int(input())
        else:       
            print(f"Игрок '{name2}' вводит число от 1 до 28")
            count2 = int(input())
            while (count2<1 or count2>28):
                print("Число должно быть в промежутке от 1 до 28!")
                count2 = int(input())
        sum2 += count2
        amount -= count2
        if amount == 0:
            print(f"ИГРОК '{name2}' ПОБЕДИЛ С РЕЗУЛЬТАТОМ {sum2}! ПОЗДРАВЛЯЕМ!")
        else:
            print(f"Количество конфет у игрока '{name2}' {sum2} шт.")
            print("Остаток конфет = ", amount)
        print("-----------------------------------")

    else:                                    # если начинает второй игрок
        if amount<=28:
            print(f"Игрок '{name2}' вводит число от 1 до {amount}")       
            count2 = int(input())
            while (count2<1 or count2>amount):
                print(f"Число должно быть в промежутке от 1 до {amount}!")
                count2 = int(input())
        else:
            print(f"Игрок '{name2}' вводит число от 1 до 28")
            count2 = int(input())
            while (count2<1 or count2>28):
                print("Число должно быть в промежутке от 1 до 28!")
                count2 = int(input())
        sum2 += count2
        amount -= count2
        if amount == 0:
            print(f"ИГРОК '{name2}' ПОБЕДИЛ С РЕЗУЛЬТАТОМ {sum2}! ПОЗДРАВЛЯЕМ!")
        else:
            print(f"Количество конфет у игрока '{name2}' {sum2} шт.")
            print("Остаток конфет = ", amount)
        print("-----------------------------------")

        if amount<=28:                                                         
            print(f"Игрок '{name1}' вводит число от 1 до {amount}")       
            count1 = int(input())
            while (count1<1 or count1>amount):
                print(f"Число должно быть в промежутке от 1 до {amount}!")
                count1 = int(input())
        else:
            print(f"Игрок '{name1}' вводит число от 1 до 28")
            count1 = int(input())
            while (count1<1 or count1>28):
                print("Число должно быть в промежутке от 1 до 28!")
                count1 = int(input())
        sum1 += count1
        amount -= count1
        if amount == 0:
            print(f"ИГРОК '{name1}' ПОБЕДИЛ С РЕЗУЛЬТАТОМ {sum1}! ПОЗДРАВЛЯЕМ!")
        else:
            print(f"Количество конфет у игрока '{name1}' {sum1} шт.")
            print("Остаток конфет = ", amount)
        print("-----------------------------------")
