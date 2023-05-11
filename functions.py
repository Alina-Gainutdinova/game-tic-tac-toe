def cell_occupancy(k1, k2):
    """
    Вместо переменной 'table' будет переменная в основной программе и будет заменена другой (скорее всего)
    Функция проверяет является ли ячейка занятой
    """
    if table[k1 - 1][k2 - 1] == "X" or table[k1 - 1][k2 - 1] == "O":
        print("cell is occupied")  # ! True / False
    else:
        print("cell free")


def coor_input():
    while True:
        try:
            player_1 = input("Введите координаты ячейки (через двоеточие): ")
            coor_ls = list(map(lambda x: x.strip(), player_1.split(":")))
            assert len(coor_ls) == 2, "Введите только два значения"
        except AssertionError as msg:
            print(msg)
        except:
            print("Ошибка")
        else:
            try:
                x, y = coor_ls
                assert x.isdigit() and y.isdigit(), "Введите число"
            except AssertionError as msg:
                print(msg)
            else:
                return x, y
