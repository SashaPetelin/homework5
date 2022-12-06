# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

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
while amount>=1:
    if first_num == 1:
        print(f"Игрок '{name1}' вводит число от 1 до 28\n")
        count1 = int(input())
        sum1 += count1
        amount -= count1
        print(f"Игрок '{name2}' вводит число от 1 до 28\n")
        count2 = int(input())
        sum2 += count2
        amount -= count2
    else:
        print(f"Игрок '{name2}' вводит число от 1 до 28\n")
        count2 = int(input())
        sum2 += count2
        amount -= count2
        print(f"Игрок '{name1}' вводит число от 1 до 28\n")
        count1 = int(input())
        sum1 += count1
        amount -= count1
