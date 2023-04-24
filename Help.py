from login import ambil_status_login


def help_umum():
    global username, password, login_status, username_status, password_status
    print("=========== HELP ===========")
    print("1. login")
    print("   Untuk masuk menggunakan akun")
    print("2. exit")
    print("   Untuk keluar dari program dan kembali ke terminal")


def help_bondowoso():
    print("=========== HELP ===========")
    print("1. Logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. Summon jin")
    print("   Untuk memanggil jin dari alam gaib")
    print("3. Hilangkan jin ")
    print("   untuk menghapus jin dari alam gaib")
    print("4. Ubah Jin")
    print("   Mengubah tipe jin yang telah disummon dari alam gaib")


def help_roro():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. Hancurkan candi")
    print("   Untuk menghancurkan candi yang tersedia")
    print("3. Aktifkan Ayam berkokok")
    print("   Roro mempunyai kemampuan untuk memalsukan pagi hari ")


def help_pengumpul():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. kumpul")
    print("   Untuk mengumpulkan resource candi")


def help_pembangun():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. bangun")
    print("   Untuk membangun candi")


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
