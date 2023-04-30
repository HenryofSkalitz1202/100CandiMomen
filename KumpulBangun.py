from FungsiTambahan import linearCongruentialMethod
from datetime import datetime


def bangun(arr_candi, arr_bahan, builder):
    list_random = [f'el-{x}' for x in range(7)]
    list_random_filtered = [f'el-{x}' for x in range(5)]
    id_candi = None

    for x in range(100):
        arr_candi[x][0] = f'{x}'

    if arr_candi[0][2] == '0':
        jmlh_candi = 0
    else:
        jmlh_candi = 1

    for i in range(1, 100):
        if arr_candi[i][2] != '0':
            jmlh_candi += 1

    for x in range(100):
        if arr_candi[x][2] == '0':
            id_candi = int(arr_candi[x][0])
            break

    linearCongruentialMethod(id_candi, 7, 3, 2, list_random, 7)

    idx = 0
    if id_candi <= 5:
        for x in range(5):
            list_random_filtered[x] = list_random[x]
    else:
        for x in range(7):
            if (int(list_random[x]) > 0) and (int(list_random[x]) <= 5):
                list_random_filtered[idx] = list_random[x]
                idx += 1

            if idx == 5:
                break

    pasir = list_random_filtered[0]
    batu = list_random_filtered[2]
    air = list_random_filtered[4]

    if int(pasir) <= int(arr_bahan[0][2]):
        if int(batu) <= int(arr_bahan[1][2]):
            if int(air) <= int(arr_bahan[2][2]):
                arr_bahan[0][2] = int(arr_bahan[0][2]) - int(pasir)
                arr_bahan[1][2] = int(arr_bahan[1][2]) - int(batu)
                arr_bahan[2][2] = int(arr_bahan[2][2]) - int(air)

                arr_candi[id_candi] = [f'{id_candi}', f'{builder}', f'{pasir}', f'{batu}', f'{air}']

                print("Candi berhasil dibangun")

                if jmlh_candi >= 100:
                    sisa_candi = 0
                else:
                    sisa_candi = 100 - jmlh_candi
                print(f"Sisa candi yang perlu dibangun: {sisa_candi}.")

            else:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun!")
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    return arr_candi, arr_bahan


def kumpul(arr_bahan):
    list1 = [f'e-{x}'for x in range(6)]
    list2 = [f'e-{x}' for x in range(6)]
    list3 = [f'e-{x}' for x in range(6)]
    linearCongruentialMethod(3, 7, 3, 2, list1, 6)
    linearCongruentialMethod(2, 7, 3, 2, list2, 6)
    linearCongruentialMethod(5, 7, 3, 2, list3, 6)

    now = datetime.now()
    pasir_random = list1[now.second % 6]
    batu_random = list2[now.second % 6]
    air_random = list3[now.second % 6]

    arr_bahan[0][2] = int(arr_bahan[0][2]) + int(pasir_random)
    arr_bahan[1][2] = int(arr_bahan[1][2]) + int(batu_random)
    arr_bahan[2][2] = int(arr_bahan[2][2]) + int(air_random)

    print(f'Jin menemukan {pasir_random} pasir, {batu_random} batu, dan {air_random} air.\n')
    return arr_bahan
