table = [['', '', ''],
         ['', '', ''],
         ['', '', '',]]
def cell_occupancy(k1, k2):
    if table[k1][k2] == 'X' or table[k1][k2] == 'O':
        print('cell is occupied')
    else:
        print('cell free')
        



def head():
    krdn_1 = int(input('Enter str: '))
    krdn_2 = int(input('Enter column: '))
    print(f'{cell_occupancy(krdn_1, krdn_2)}')
head()