username_status = False
password_status = False
login_status = False
role = None


def cek_login(arr):
    global username_status, password_status, temp, role
    for i in range(102):
        temp = arr[i]
        if username == temp[0]:
            username_status = True
            if password == temp[1]:
                password_status = True
                role = temp[2]
            break


def login(arr):
    global username, password, login_status, username_status, password_status
    if not login_status:
        username = input("\nUsername: ")
        password = input("Password: ")
        cek_login(arr)

        if username_status:
            if password_status:
                login_status = True
                print(f'\nSelamat datang, {username}!')
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                print('')
            else:
                print("Password salah!")
                username_status = False
                password_status = False
                print('')
        else:
            print("Username tidak terdaftar!")
            username_status = False
            password_status = False
            print('')
    else:
        print('Login gagal!')
        print(f'Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.'
              )
        print('')


def logout():
    global login_status, username_status, password_status, role
    if login_status:
        username_status = False
        password_status = False
        login_status = False
        role = None
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')


def ambil_status_login():
    return login_status


def ambil_username():
    return username


def ambil_role():
    return role
