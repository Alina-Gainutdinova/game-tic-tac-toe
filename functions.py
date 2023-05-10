def cell_occupancy(k1, k2):
    """
    Вместо переменной 'table' будет переменная в основной программе и будет заменена другой (скорее всего)
    Функция проверяет является ли ячейка занятой
    """
    if table[k1 - 1][k2 - 1] == "X" or table[k1 - 1][k2 - 1] == "O":
        print("cell is occupied")  # ! True / False
    else:
        print("cell free")
