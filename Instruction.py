from Login import login, logout, ambil_role, ambil_status_login, ambil_username
from Help import list_help
from Save import save
from Exit import exit_func
from Load import load
from KumpulBangun import bangun, kumpul
from FunctionBondo import summonjin, hapusjin, ubahjin, batch_kumpul, batch_bangun, laporan_candi, laporan_jin
from FunctionRoro import ayam_berkokok, hancurkan_candi

arr_result = load()
users = arr_result[0]
candi = arr_result[1]
bahan_bangunan = arr_result[2]


def instruction_umum():
    global users, candi, bahan_bangunan
    ins = input(">>> Instruksinya apa a?? : ")
    if ins == "login":
        login(users)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        list_help(ambil_role())
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "logout":
        logout()
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami a. Silakan diulang!\n")
        instruction(ambil_role())


def instruction_bondo(list_user, list_candi, list_bahan):
    global users, candi, bahan_bangunan
    ins = input(">>> Instruksinya apa do?? : ")
    if ins == "logout":
        logout()
        instruction(ambil_role())
    elif ins == "summonjin":
        users = summonjin(list_user)
        instruction(ambil_role())
    elif ins == "hapusjin":
        hasil = hapusjin(list_user, list_candi)
        users = hasil[0]
        candi = hasil[1]
        instruction(ambil_role())
    elif ins == "ubahjin":
        users = ubahjin(list_user)
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        list_help(ambil_role())
        instruction(ambil_role())
    elif ins == "laporancandi":
        laporan_candi(list_candi)
        instruction(ambil_role())
    elif ins == "laporanjin":
        laporan_jin(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "batchkumpul":
        bahan_bangunan = batch_kumpul(list_user, list_bahan)
        instruction(ambil_role())
    elif ins == "batchbangun":
        hasil_batch = batch_bangun(list_user, list_bahan, list_candi)
        candi = hasil_batch[0]
        bahan_bangunan = hasil_batch[1]
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami do. Silakan diulang!\n")
        instruction(ambil_role())


def instruction_roro(list_candi):
    global users, candi, bahan_bangunan
    ins = input(">>> Instruksinya apa ro?? : ")
    if ins == "logout":
        logout()
        instruction(ambil_role())
    elif ins == "hancurkancandi":
        candi = hancurkan_candi(list_candi)
        instruction(ambil_role())
    elif ins == "ayamberkokok":
        ayam_berkokok(candi)
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        list_help(ambil_role())
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami ro. Silakan diulang!\n")
        instruction(ambil_role())


def instruction_pengumpul(list_bahan):
    global users, candi, bahan_bangunan
    ins = input(">>> Instruksinya apa pul?? : ")
    if ins == "logout":
        logout()
        instruction(ambil_role())
    elif ins == "kumpul":
        bahan_bangunan = kumpul(list_bahan)
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        list_help(ambil_role())
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami pul. Silakan diulang!\n")
        instruction(ambil_role())


def instruction_pembangun(list_candi, list_bahan):
    global users, candi, bahan_bangunan
    ins = input(">>> Instruksinya apa ngun?? : ")
    if ins == "logout":
        logout()
        instruction(ambil_role())
    elif ins == "bangun":
        hasilbangun = bangun(list_candi, list_bahan, ambil_username())
        candi = hasilbangun[0]
        bahan_bangunan = hasilbangun[1]
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        list_help(ambil_role())
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami ngun. Silakan diulang!\n")
        instruction(ambil_role())


def instruction(role):
    global users, candi, bahan_bangunan
    if not ambil_status_login():
        instruction_umum()
    else:
        if role == "bandung_bondowoso":
            instruction_bondo(users, candi, bahan_bangunan)
        elif role == "roro_jonggrang":
            instruction_roro(candi)
        elif role == "jin_pengumpul":
            instruction_pengumpul(bahan_bangunan)
        elif role == "jin_pembangun":
            instruction_pembangun(candi, bahan_bangunan)
