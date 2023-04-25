from Save import save


def exit_func(users, candi, bahan_bangunan):
    isInputValid = False

    while not isInputValid:
        inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

        if (inp.upper() == "Y") or (inp.upper() == "N"):
            isInputValid = True

            if inp.upper() == "Y":
                save(users, candi, bahan_bangunan)
