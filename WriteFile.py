def write_user(path, arr):
    f = open(path, 'w')
    f.write('username;password;role\n')

    for i in range(102):
        arr_sekrg = arr[i]
        str_input = f'{arr_sekrg[0]};{arr_sekrg[1]};{arr_sekrg[2]}\n'
        f.write(str_input)


def write_candi(path, arr):
    f = open(path, 'w')
    f.write('id;pembuat;pasir;batu;air\n')

    for i in range(100):
        arr_sekrg = arr[i]
        str_input = f'{arr_sekrg[0]};{arr_sekrg[1]};{arr_sekrg[2]};{arr_sekrg[3]};{arr_sekrg[4]}\n'
        f.write(str_input)


def write_bahan(path, arr):
    f = open(path, 'w')
    f.write('nama;deskripsi;jumlah\n')

    for i in range(3):
        arr_sekrg = arr[i]
        str_input = f'{arr_sekrg[0]};{arr_sekrg[1]};{arr_sekrg[2]}\n'
        f.write(str_input)
