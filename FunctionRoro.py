def ayam_berkokok(arr):
    print("Kukuruyuk.. Kukuruyuk..\n")

    jumlah_candi = 0
    for i in range(100):
        if arr[i][2] != '0':
            jumlah_candi += 1
    print(f"Jumlah candi: {jumlah_candi}\n")

    if jumlah_candi == 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        quit()
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        quit()


def hancurkan_candi(arr):
    id_candi = int(input("Masukkan ID candi: "))

    if int(arr[id_candi][2]) == 0:
        print("Tidak ada candi dengan ID tersebut.\n")
    else:
        conf = input(f"Apakah Anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
        if conf.upper() == "Y":
            arr[id_candi] = [f'{id_candi}', f'builder{id_candi}', '0', '0', '0']
            print("Candi telah berhasil dihancurkan.\n")
        elif conf.upper() == "N":
            print(f"Candi ID {id_candi} tidak jadi dihancurkan\n")
    return arr
