import time
from datetime import datetime
from FungsiTambahan import sort_array_candi, my_split, linearCongruentialMethod


def summonjin(arr):
    def validasi_nama_jin(user, nama_jin):
        for x in range(2, 102):
            if user[x][0] == nama_jin:
                print(f'Username “{nama_jin}” sudah diambil!')
                return False
        return True

    print('''\nJenis jin yang dapat dipanggil:
    (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
    (2) Pembangun - Bertugas membangun candi''')
    e = ''

    b = int(input('Masukkan nomor jenis jin yang ingin dipanggil : '))
    while b != 1 and b != 2:
        print(f'Tidak ada jenis jin bernomor "{b}"!\n')
        b = int(input('\nMasukkan nomor jenis jin yang ingin dipanggil : '))
    else:
        if b == 1:
            print('Memilih jin "Pengumpul".\n')
            e = 'jin_pengumpul'
        elif b == 2:
            print('Memilih jin "Pembangun".\n')
            e = 'jin_pembangun'
        c = input('Masukkan username jin : ')

        while not validasi_nama_jin(arr, c):
            c = input('\nMasukkan username jin : ')

        d = input('Masukkan password jin : ')

        while len(d) < 5 or len(d) > 15:
            print('Password panjangnya harus 5-25 karakter!')
            d = input('\nMasukkan password jin : ')

        print('\nMengumpulkan sesajen...')
        time.sleep(1)
        print('Menyerahkan sesajen...')
        time.sleep(1)
        print('Membacakan mantra...')
        time.sleep(1)

        if arr[101][0] != '101':
            print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu\n')
        else:
            for i in range(2, 102):
                if arr[i][0] == f'{i}':
                    arr[i][0] = c
                    arr[i][1] = d
                    arr[i][2] = e
                    print(f'Jin {c} berhasil dipanggil!\n')
                    break

        return arr


def hapusjin(user, candis):
    c = input('Masukkan username jin : ')
    temp = 0

    for i in range(2, 102):
        if user[i][0] == c:
            b = input(f'Apakah anda yakin ingin menghapus jin dengan username {c} (Y/N)? ')
            while b.upper() != 'Y' and b.upper() != 'N':
                b = input(f'Apakah anda yakin ingin menghapus jin dengan username {c} (Y/N)? ')

            if b.upper() == 'N':
                print(f'Jin {c} tidak jadi dihapus\n')
                break
            elif b.upper() == 'Y':
                user[i] = [i, f'password{i}', f'role{i}']

                for j in range(100):
                    if candis[j][1] == c:
                        candis[j] = [f'{j}', f'builder{j}', '0', '0', '0']

                print('Jin telah dimusnahkan dari alam semesta\n')
                break
        else:
            temp += 1
    if temp == 100:
        print('Tidak ada jin dengan username tersebut\n')
    return user, candis


def ubahjin(arr):
    c = input('Masukkan username jin : ')
    temp = 0
    for i in range(2, 102):
        if arr[i][0] == c:
            if arr[i][2] == 'jin_pengumpul':
                pengumpul = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
                if pengumpul.upper() == 'N':
                    print(f'Jin {c} tidak jadi diubah.\n')
                    break
                elif pengumpul.upper() == 'Y':
                    arr[i][2] = 'jin_pembangun'
                    print('Jin telah berhasil diubah.\n')
            elif arr[i][2] == 'jin_pembangun':
                pembangun = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ')
                if pembangun.upper() == 'N':
                    print('Jin tidak jadi diubah.')
                    break
                elif pembangun.upper() == 'Y':
                    arr[i][2] = 'jin_pengumpul'
                    print('Jin telah berhasil diubah.')
            break

        else:
            temp += 1
            if temp == 100:
                print('Tidak ada jin dengan username tersebut.')
    return arr


def batch_kumpul(arr_jin, arr_bahan):
    list1 = [f'e-{x}' for x in range(6)]
    list2 = [f'e-{x}' for x in range(6)]
    list3 = [f'e-{x}' for x in range(6)]
    linearCongruentialMethod(3, 7, 3, 2, list1, 6)
    linearCongruentialMethod(2, 7, 3, 2, list2, 6)
    linearCongruentialMethod(5, 7, 3, 2, list3, 6)

    now = datetime.now()
    pasir_random = list1[now.microsecond % 6]
    batu_random = list2[now.microsecond % 6]
    air_random = list3[now.microsecond % 6]
    total_jin_pengumpul = 0
    total_pasir = 0
    total_batu = 0
    total_air = 0

    for i in range(2, 102):
        if arr_jin[i][2] == 'jin_pengumpul':
            total_jin_pengumpul += 1

    if total_jin_pengumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print(f'Mengerahkan {total_jin_pengumpul} jin untuk mengumpulkan bahan.')
        for i in range(total_jin_pengumpul):
            total_pasir += int(pasir_random)
            total_batu += int(batu_random)
            total_air += int(air_random)
            time.sleep(0.1)
            now = datetime.now()
            pasir_random = list1[now.microsecond % 6]
            batu_random = list2[now.microsecond % 6]
            air_random = list3[now.microsecond % 6]

        arr_bahan[0][2] = int(arr_bahan[0][2]) + int(total_pasir)
        arr_bahan[1][2] = int(arr_bahan[1][2]) + int(total_batu)
        arr_bahan[2][2] = int(arr_bahan[2][2]) + int(total_air)
        print(f'Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.')

    return arr_bahan


def batch_bangun(arr_jin, arr_bahan, arr_candi):
    def bangun_single(arr_of_candi, builder):
        list_random = [f'el-{x}' for x in range(7)]
        list_random_filtered = [f'el-{x}' for x in range(5)]
        id_candi = None

        for x in range(100):
            if arr_of_candi[x][2] == '0':
                id_candi = int(arr_of_candi[x][0])
                break

        linearCongruentialMethod(id_candi, 7, 3, 2, list_random, 7)

        index = 0
        if id_candi <= 5:
            for x in range(5):
                list_random_filtered[x] = list_random[x]
        else:
            for x in range(7):
                if (int(list_random[x]) > 0) and (int(list_random[x]) <= 5):
                    list_random_filtered[index] = list_random[x]
                    index += 1

                if index == 5:
                    break

        pasir = list_random_filtered[0]
        batu = list_random_filtered[2]
        air = list_random_filtered[4]

        arr_of_candi[id_candi] = [f'{id_candi}', f'{builder}', f'{pasir}', f'{batu}', f'{air}']

        return arr_of_candi, pasir, batu, air, id_candi

    total_jin_pembangun = 0

    for i in range(2, 102):
        if arr_jin[i][2] == 'jin_pembangun':
            total_jin_pembangun += 1

    if total_jin_pembangun == 0:
        print("Kumpul gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        arr_pembangun = [f'builder-{x}' for x in range(total_jin_pembangun)]
        idx = 0

        for i in range(2, 102):
            if arr_jin[i][2] == 'jin_pembangun':
                arr_pembangun[idx] = arr_jin[i][0]
                idx += 1

                if idx == total_jin_pembangun:
                    break

        arr_id = [f'id-{x}' for x in range(total_jin_pembangun)]
        temp_arr_candi = arr_candi
        total_pasir = 0
        total_batu = 0
        total_air = 0
        for i in range(total_jin_pembangun):
            temp = bangun_single(temp_arr_candi, arr_pembangun[i])
            temp_arr_candi = temp[0]
            total_pasir += int(temp[1])
            total_batu += int(temp[2])
            total_air += int(temp[3])
            arr_id[i] = str(temp[4])

        print(f"Mengerahkan {total_jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir,"
              f"{total_batu} batu, dan {total_air} air.")

        kurang_pasir = 0
        kurang_batu = 0
        kurang_air = 0
        if int(total_pasir) <= int(arr_bahan[0][2]):
            isPasirCukup = True
        else:
            isPasirCukup = False
            kurang_pasir += total_pasir - int(arr_bahan[0][2])

        if int(total_batu) <= int(arr_bahan[1][2]):
            isBatuCukup = True
        else:
            isBatuCukup = False
            kurang_batu += total_batu - int(arr_bahan[1][2])

        if int(total_air) <= int(arr_bahan[2][2]):
            isAirCukup = True
        else:
            isAirCukup = False
            kurang_air += total_air - int(arr_bahan[2][2])

        if isPasirCukup and isBatuCukup and isAirCukup:
            arr_bahan[0][2] = int(arr_bahan[0][2]) - int(total_pasir)
            arr_bahan[1][2] = int(arr_bahan[1][2]) - int(total_batu)
            arr_bahan[2][2] = int(arr_bahan[2][2]) - int(total_air)
            print(f"Jin berhasil membangun {total_jin_pembangun} candi")
            return temp_arr_candi, arr_bahan
        else:
            if not isPasirCukup and not isBatuCukup and not isAirCukup:
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")
            elif not isPasirCukup and not isBatuCukup and isAirCukup:
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_batu} batu.")
            elif not isPasirCukup and isBatuCukup and not isAirCukup:
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_air} air.")
            elif not isPasirCukup and isBatuCukup and isAirCukup:
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir.")
            elif isPasirCukup and not isBatuCukup and not isAirCukup:
                print(f"Bangun gagal. Kurang {kurang_batu} batu dan {kurang_air} air.")
            elif isPasirCukup and not isBatuCukup and isAirCukup:
                print(f"Bangun gagal. Kurang {kurang_batu} batu.")
            elif isPasirCukup and isBatuCukup and not isAirCukup:
                print(f"Bangun gagal. Kurang {kurang_air} air.")
            return arr_candi, arr_bahan


def laporan_candi(arr):
    pasir = int(arr[0][2])
    batu = int(arr[0][3])
    air = int(arr[0][4])
    temp_harga = 10000 * pasir + 15000 * batu + 7500 * air
    maks = [arr[0][0], temp_harga]
    minimal = ['', 0]

    if arr[0][2] == '0':
        jmlh_candi = 0
    else:
        jmlh_candi = 1

    for i in range(1, 100):
        if arr[i][2] != '0':
            jmlh_candi += 1
            pasir += int(arr[i][2])
            batu += int(arr[i][3])
            air += int(arr[i][4])

            temp_harga = 10000 * int(arr[i][2]) + 15000 * int(arr[i][3]) + 7500 * int(arr[i][4])
            if temp_harga > maks[1]:
                maks = [arr[i][0], temp_harga]

            if minimal[1] == 0:
                minimal = [arr[i][0], temp_harga]
            else:
                if temp_harga < minimal[1]:
                    minimal = [arr[i][0], temp_harga]
    print(f'\n> Total Candi: {jmlh_candi}')
    print(f'> Total Pasir yang digunakan: {pasir}')
    print(f'> Total Batu yang digunakan: {batu}')
    print(f'> Total Air yang digunakan: {air}')
    if jmlh_candi == 0:
        print(f'> ID Candi Termahal: -')
        print(f'> ID Candi Termurah: -')
    else:
        print(f'> ID Candi Termahal: {maks[0]} (Rp {maks[1]})')
        print(f'> ID Candi Termurah: {minimal[0]} (Rp {minimal[1]})\n')


def laporan_jin(arr_jin, arr_candi, arr_bahan):
    total_jin = 0
    total_jin_pengumpul = 0
    total_jin_pembangun = 0
    string_pembangun = ''

    for i in range(2, 102):
        if arr_jin[i][0] != f'{i}':
            total_jin += 1
            if arr_jin[i][2] == 'jin_pembangun':
                total_jin_pembangun += 1
                if string_pembangun == '':
                    string_pembangun += arr_jin[i][0]
                else:
                    string_pembangun += f';{arr_jin[i][0]}'
            elif arr_jin[i][2] == 'jin_pengumpul':
                total_jin_pengumpul += 1

    print(f'> Total Jin: {total_jin}')
    print(f'> Total Jin Pengumpul: {total_jin_pengumpul}')
    print(f'> Total Jin Pembangun: {total_jin_pembangun}')

    if total_jin_pembangun == 0:
        print("Jin Terajin: -")
        print("Jin Termalas: -")
    else:
        temp_arr_candi = sort_array_candi(arr_candi)
        string_pembangun += "\n"
        temp_arr_pembangun = my_split(string_pembangun, ';')
        temp_count = 0
        count_rajin = 0
        count_malas = 0
        terajin = ''
        termalas = temp_arr_pembangun[0]

        for i in range(total_jin_pembangun):
            for j in range(100):
                if temp_arr_pembangun[i] == temp_arr_candi[j][1]:
                    temp_count += 1

            if temp_count > count_rajin:
                terajin = temp_arr_pembangun[i]

            if i == 0:
                count_malas = temp_count
            else:
                if temp_count <= count_malas:
                    termalas = temp_arr_pembangun[i]

            temp_count = 0

        print(f"> Jin Terajin: {terajin}")
        print(f"> Jin Termalas: {termalas}")

        jmlh_pasir = arr_bahan[0][2]
        jmlh_batu = arr_bahan[1][2]
        jmlh_air = arr_bahan[2][2]
        print(f'> Jumlah Pasir: {jmlh_pasir} unit')
        print(f'> Jumlah Batu: {jmlh_batu} unit')
        print(f'> Jumlah Air: {jmlh_air} unit\n')
