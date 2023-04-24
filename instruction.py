from login import login, logout, ambil_role, ambil_status_login
from Help import list_help
from save import save
from exit import exit_func
from load import load
from f3f4f5f6 import summonjin
from f3f4f5f6 import hapusjin
from f3f4f5f6 import ubahjin
from f3f4f5f6 import bangun

arr_result = load()
users = arr_result[0]
candi = arr_result[1]
bahan_bangunan = arr_result[2]


def instruction_umum():
    global users
    ins = input("Instruksinya apa a?? : ")
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


def instruction_bondo(list_user, list_candi):
    global users, candi
    ins = input("Instruksinya apa do?? : ")
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
        help(ambil_role())
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami do. Silakan diulang!\n")
        instruction(ambil_role())


def instruction_roro():
    global users
    ins = input("Instruksinya apa ro?? : ")
    if ins == "logout":
        logout()
        instruction(ambil_role())
    elif ins == "hancurkancandi":
        print("fitur coming soon yak ro")
        instruction(ambil_role())
    elif ins == "ayamberkokok":
        print("fitur coming soon yak ro")
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        help(ambil_role())
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami ro. Silakan diulang!\n")
        instruction(ambil_role())


def instruction_pengumpul():
    global users
    ins = input("Instruksinya apa pul?? : ")
    if ins == "logout":
        logout()
        instruction(ambil_role())
    elif ins == "kumpul":
        print("fitur coming soon pul")
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        help(ambil_role())
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami pul. Silakan diulang!\n")
        instruction(ambil_role())


def instruction_pembangun():
    global users
    ins = input("Instruksinya apa ngun?? : ")
    if ins == "logout":
        logout()
        instruction(ambil_role())
    elif ins == "bangun":
        bangun()
        instruction(ambil_role())
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction(ambil_role())
    elif ins == "exit":
        exit_func(users, candi, bahan_bangunan)
        quit()
    elif ins == "help":
        help(ambil_role())
        instruction(ambil_role())
    else:
        print("Instruksi kurang dapat dipahami ngun. Silakan diulang!\n")
        instruction(ambil_role())


def instruction(role):
    global users
    if not ambil_status_login():
        instruction_umum()
    else:
        if role == "bandung_bondowoso":
            instruction_bondo(users, candi)
        elif role == "roro_jonggrang":
            instruction_roro()
        elif role == "jin_pengumpul":
            instruction_pengumpul()
        elif role == "jin_pembangun":
            instruction_pembangun()
