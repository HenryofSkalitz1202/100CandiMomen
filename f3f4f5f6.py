import time
from load import load

arr_result = load()
users = arr_result[0]
candi = arr_result[1]
bahan_bangunan = arr_result[2]


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
            print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
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
    def geser_array(arr, index, range_idx):
        for k in range(index, range_idx-1):
            arr[k] = arr[k+1]

    def hapus_candi_jin(builder):
        isBersih = True

        for a in range(100):
            if candis[a][1] == builder:
                geser_array(candis, a, 100)
                candis[99] = ['100', 'builder', '0', '0', '0']
                isBersih = False
                break

        if not isBersih:
            hapus_candi_jin(builder)

    c = input('Masukkan username jin : ')
    temp = 0

    for i in range(2, 102):
        if user[i][0] == c:
            b = input(f'Apakah anda yakin ingin menghapus jin dengan username {c} (Y/N)? ')
            while b.upper() != 'Y' and b.upper() != 'N':
                b = input(f'Apakah anda yakin ingin menghapus jin dengan username {c} (Y/N)? ')

            if b.upper() == 'N':
                print(f'Jin {c} tidak jadi dihapus')
                break
            elif b.upper() == 'Y':
                for j in range(i, 101):
                    user[j] = user[j+1]
                user[101] = ['102', 'password102', 'role102']

                hapus_candi_jin(c)

                print('Jin telah dimusnahkan dari alam semesta')
                break
        else:
            temp += 1
    if temp == 100:
        print('Tidak ada jin dengan username tersebut')
    return user, candis


def ubahjin(arr):
    c = input('Masukkan username jin : ')
    temp = 0
    for i in range(2, 102):
        if arr[i][0] == c:
            if arr[i][2] == 'jin_pengumpul':
                pengumpul = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
                if pengumpul.upper() == 'N':
                    print('Jin tidak jadi diubah.')
                    break
                elif pengumpul.upper() == 'Y':
                    arr[i][2] = 'jin_pembangun'
                    print('Jin telah berhasil diubah.')
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


def bangun():
    from FungsiTambahan import matrix_csv, jml_rows
    matrix = matrix_csv()
    jml_rows=jml_rows()
    temp = 0
    list=[3,4,5] #Contoh List bahan bangunan
    for i in range(1,jml_rows):
        matrix[i][2] = int(matrix[i][2])
        if matrix[i][0] == 'pasir':
            if matrix[i][2]-list[0]<0:
                temp+=1
            else:
                matrix[i][2]-=list[0]
        elif matrix[i][0] == 'batu':
            if matrix[i][2]-list[1]<0:
                temp+=1
            else:
                matrix[i][2]-=list[1]
        elif matrix[i][0] == 'air':
            if matrix[i][2]-list[2]<0:
                temp+=1
            else:
                matrix[i][2]-=list[2]
    if temp!=0:
        print('Bahan bangunan tidak cukup')
        print('Candi tidak berhasil dibangun')
    else:
        print('Candi berhasil dibangun')
