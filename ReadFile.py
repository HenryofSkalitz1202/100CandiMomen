from FungsiTambahan import my_split


def read_user(path):
    global arr_login
    f = open(path, 'r')
    arr_login = [[x, f'password{x}', f'role{x}'] for x in range(102)]
    f.readline()

    for i in range(102):
        line = f.readline()
        if not line:
            break

        arr_login[i] = my_split(line, ';')

    f.close()
    return arr_login


def read_bahan(path):
    global arr_bahan
    f = open(path, 'r')
    arr_bahan = [['pasir', 'kilogram', '0'], ['batu', 'kilogram', '0'], ['air', 'liter', '0']]
    f.readline()

    for i in range(3):
        line = f.readline()
        if not line:
            break

        arr_bahan[i] = my_split(line, ';')

    f.close()
    return arr_bahan


def read_candi(path):
    global arr_candi
    f = open(path, 'r')
    arr_candi = [[x, f'builder{x}', '0', '0', '0'] for x in range(100)]
    f.readline()

    for i in range(100):
        line = f.readline()
        if not line:
            break

        arr_candi[i] = my_split(line, ';')

    f.close()
    return arr_candi
