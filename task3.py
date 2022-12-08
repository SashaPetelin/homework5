# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(line):
    count = 1
    result = ''
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            count += 1
        else:
            result = result + str(count) + line[i]
            count = 1
    if count > 1 or (line[len(line)-2] != line[-1]):
        result = result + str(count) + line[-1]
    return result

def reduction(line):
    number = ''
    result = ''
    for i in range(len(line)):
        if not line[i].isalpha():
            number += line[i]
        else:
            result = result + line[i] * int(number)
            number = ''
    return result

text = input("Введите текст: ")
print(f"Данные после сжатия: {compression(text)}")
print(f"Данные после восстановления: {reduction(compression(text))}")
