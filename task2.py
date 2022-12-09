# Создайте программу для игры в ""Крестики-нолики"".

fld = list(range(1,10))

winlines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
       [0, 3, 6], [1, 4, 7], [2, 5, 8],
       [0, 4, 8], [2, 4, 6]]

def lining(fld):
    print('-'*10)
    for i in range(3):
        print(fld[0+i*3], '|', fld[1+i*3], '|', fld[2+i*3])
        print('-'*10)

def wrt(n,sign):
    ind = fld.index(n)
    fld[ind] = sign

def chekwin():
    winner = ""

    for i in winlines:
        if fld[i[0]] == "X" and fld[i[1]] == "X" and fld[i[2]] == "X":
            winner = "Выиграл игрок Х"
        elif fld[i[0]] == "O" and fld[i[1]] == "O" and fld[i[2]] == "O":
            winner = "Выиграл игрок O"
    return winner

ending = False
p1 = True
while ending == False:
    lining(fld)

    if p1 == True:
        sign = "X"
        n = int(input("Ходит игрок Х: "))
    else:
        sign = "O"
        n = int(input("Ходит игрок O: "))

    wrt(n, sign)
    win = chekwin()
    if win != "":
        ending = True
    else:
        ending = False

    p1 = not(p1)

lining(fld)
print(win)