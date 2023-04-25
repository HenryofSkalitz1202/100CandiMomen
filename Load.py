import argparse
import sys
import os
from ReadFile import read_user
from ReadFile import read_bahan
from ReadFile import read_candi


def load():
    class MyParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('Tidak ada nama folder yang diberikan!\n')
            self.print_usage()
            sys.exit(2)

    parser = MyParser()
    parser.add_argument("nama_folder", help='nama folder yang mau dicek', nargs=1)
    args = parser.parse_args()

    nama_foldernya = args.nama_folder[0]
    path = './save/' + nama_foldernya
    isExist = os.path.isdir(path)

    if isExist:
        path_user = f'{path}/user.csv'
        path_candi = f'{path}/candi.csv'
        path_bahan = f'{path}/bahan_bangunan.csv'

        data_user = read_user(path_user)
        data_candi = read_candi(path_candi)
        data_bahan = read_bahan(path_bahan)

        arr_result = [data_user, data_candi, data_bahan]
        return arr_result

    else:
        print(f'Folder "{nama_foldernya}" tidak ditemukan.')
        quit()
