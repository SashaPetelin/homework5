# b) Попытка наделить бота ""интеллектом""

import random

n = int(input("Введите количество игроков от 1 до 2: "))

if n == 2:
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
        if first_num == 1:     
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
                break
            else:
                print(f"Количество конфет у игрока '{name1}' {sum1} шт.")
                print("Остаток конфет = ", amount)
            print("--------------------------------------")

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
                break
            else:
                print(f"Количество конфет у игрока '{name2}' {sum2} шт.")
                print("Остаток конфет = ", amount)
            print("---------------------------------------")

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
                break
            else:
                print(f"Количество конфет у игрока '{name2}' {sum2} шт.")
                print("Остаток конфет = ", amount)
            print("---------------------------------------")

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
                break
            else:
                print(f"Количество конфет у игрока '{name1}' {sum1} шт.")
                print("Остаток конфет = ", amount)
            print("---------------------------------------")

else:
    print("Против Вас играет бот Валера! Удачной игры!")
    print()
    name1 = input("Введите Ваше имя: ")
    name2 = "бот Валера"

    dict = {1: name1, 2: name2}

    first_num = random.choice(list(dict.keys()))
    first_name = dict.get(first_num)
    print(f"Первым начинает игрок {first_num}:'{first_name}'")

    amount = 2021
    sum1 = 0
    sum2 = 0
    while amount>0:
        if first_num == 1:     
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
                break
            else:
                print(f"Количество конфет у игрока '{name1}' {sum1} шт.")
                print("Остаток конфет = ", amount)
            print("--------------------------------------")

            if (29<amount<=58):                                         # от сюда попытались ввести "интеллект"
                count2 = amount-29
            elif amount<=28:
                print(f"'{name2}' вводит число от 1 до {amount}")       
                count2 = amount                                           # до сюда
            else:       
                print(f"'{name2}' вводит число от 1 до 28")
                count2 = random.randint(1,29)
            sum2 += count2
            amount -= count2
            if amount == 0:
                print(f"'{name2}' ПОБЕДИЛ С РЕЗУЛЬТАТОМ {sum2}!")
                break
            else:
                print(f"Количество конфет у игрока '{name2}' {sum2} шт.")
                print("Остаток конфет = ", amount)
            print("---------------------------------------")

        else:                                                # если начинает бот
            if (29<amount<=58):                                         
                count2 = amount-29                                    
            elif amount<=28:
                print(f"'{name2}' вводит число от 1 до {amount}")       
                count2 = amount
            else:
                print(f"'{name2}' вводит число от 1 до 28")
                count2 = random.randint(1,29)
            sum2 += count2
            amount -= count2
            if amount == 0:
                print(f"'{name2}' ПОБЕДИЛ С РЕЗУЛЬТАТОМ {sum2}!")
                break
            else:
                print(f"Количество конфет у игрока '{name2}' {sum2} шт.")
                print("Остаток конфет = ", amount)
            print("---------------------------------------")

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
                break
            else:
                print(f"Количество конфет у игрока '{name1}' {sum1} шт.")
                print("Остаток конфет = ", amount)
            print("---------------------------------------")