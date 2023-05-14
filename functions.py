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
            coordinates = input("Введите координаты ячейки (через двоеточие): ")
            coor_ls = list(map(lambda x: x.strip(), coordinates.split(":")))
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
            
def is_correct_coor(coordinates):
    x, y = coordinates
    if 0 < x < 4 and 0 < y < 4: return True
    else: return False
