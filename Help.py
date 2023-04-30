from login import ambil_status_login


def help_umum():
    global username, password, login_status, username_status, password_status
    print("=========== HELP ===========")
    print("1. login")
    print("   Untuk masuk menggunakan akun")
    print("2. save")
    print("   Menyimpan data program ke folder save")
    print("3. exit")
    print("   Keluar dari program dan kembali ke terminal")


def help_bondowoso():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Keluar dari akun yang digunakan sekarang")
    print("2. summonjin")
    print("   Memanggil jin dari alam gaib")
    print("3. hilangkanjin ")
    print("   Menghapus jin dari alam gaib")
    print("4. ubahjin")
    print("   Mengubah tipe jin yang telah di-summon dari alam gaib")
    print("5. batchkumpul")
    print("   Seluruh jin dengan tipe pengumpul akan mengumpulkan bahan")
    print("6. batchbangun")
    print("   Seluruh jin dengan tipe pembangun akan membangun candi")
    print("7. laporanjin")
    print("   Menampilkan jumlah jin, jin terajin & termalas, dan jumlah bahan")
    print("8. laporancandi")
    print("   Menampilkan jumlah candi, jumlah bahan candi, dan ID candi termurah & termahal")
    print("9. save")
    print("   Menyimpan data program ke folder save")
    print("10. exit")
    print("   Keluar dari program dan kembali ke terminal")


def help_roro():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. hancurkancandi")
    print("   Untuk menghancurkan candi yang tersedia")
    print("3. ayamberkokok")
    print("   Roro mempunyai kemampuan untuk memalsukan pagi hari ")
    print("4. save")
    print("   Menyimpan data program ke folder save")
    print("5. exit")
    print("   Keluar dari program dan kembali ke terminal")


def help_pengumpul():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. kumpul")
    print("   Untuk mengumpulkan resource candi")
    print("3. save")
    print("   Menyimpan data program ke folder save")
    print("4. exit")
    print("   Keluar dari program dan kembali ke terminal")


def help_pembangun():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. bangun")
    print("   Untuk membangun candi")
    print("3. save")
    print("   Menyimpan data program ke folder save")
    print("4. exit")
    print("   Keluar dari program dan kembali ke terminal")


def list_help(role):
    if not ambil_status_login():
        help_umum()
    else:
        if role == "bandung_bondowoso":
            help_bondowoso()
        elif role == "roro_jonggrang":
            help_roro()
        elif role == "jin_pengumpul":
            help_pengumpul()
        elif role == "jin_pembangun":
            help_pembangun()
