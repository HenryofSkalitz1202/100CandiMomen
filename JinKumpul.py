import csv
import RNG as rand
#bahan = open("bahan_bangunan.csv", 'w') ##upd
#writer = csv.writer(bahan, delimiter=',')
bahanR = open("bahan_bangunan.csv", 'r') # bahan = read_bahan("bahan_bangunan.csv") ##upd
reader = csv.reader(bahanR, delimiter=',')
cols = ['nama', 'deskripsi', 'jumlah']

candi = open("candi.csv", 'r') # candi = read_candi("candi.csv") ##upd
readerC = csv.reader(candi, delimiter=',')
user = open("user.csv", 'r') # user = read_user("user.csv") ##upd
readerU = csv.reader(user, delimiter=',')

def kumpul(x) : # for kumpul biasa dan batch kumpul
    totJinkum = 0
    for i in range(102) : ##upd
        if user[2][i] == "jin_pengumpul" :
            totJinkum += 1 
    tempMat = [0,0,0] # utk nyimpen data pasir,batu,air sementara 
    for i in range(3) : 
        tempMat[i] = bahan[i][2] ##upd
    pasir_dari_csv = tempMat[0]
    batu_dari_csv = tempMat[1]
    air_dari_csv = tempMat[2]
    
    if x == "indiv" : # jin pengumpul indiv (kumpul biasa)
        pasir = rand() # note : function rand belum dikasih parameter
        batu = rand()
        air = rand()
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
        # isi file dalam csv bahan
        totMat = [["pasir", "p", str(pasir+pasir_dari_csv)], ["batu", "b",str(batu+batu_dari_csv)], ["air", "a", str(air+air_dari_csv)]]
        write_bahan(bahan_bangunan, totMat) ##upd
    else : # batch kumpul
        n = totJinkum # jumlah jin pengumpul
        if n > 0 : # ada jin pengumpul
            pasir = [0 for i in range(n)]
            batu = [0 for i in range(n)]
            air = [0 for i in range(n)]
            mat = [pasir,batu,air]
            for i in range(3) : 
                for j in range(n) :
                    mat[i][j] = rand() # note : function random belum dikasih parameter
            sumpas = 0 # sum pasir; sum batu; sum air
            sumbat = 0 
            sumair = 0
            for i in range(n) :
                sumpas += mat[0][j]
                sumbat += mat[1][j]
                sumair += mat[2][j]
            print(f"Mengerahkan {n} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan total {sumpas} pasir, {sumbat} batu, dan {sumair} air.")
            # isi dalam file csv bahan
            totMat = [["pasir", "p", str(sumpas+pasir_dari_csv)], ["batu", "b",str(sumbat+batu_dari_csv)], ["air", "a", str(sumair+air_dari_csv)]]
            write_bahan(bahan_bangunan, totMat) ##upd
        else : # tidak ada jin pengumpul
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def bangun() : 
    totJinban = 0
    rowU3 = next(readerU)
    while not EOP(rowU3) : 
        if rowU3[2] == "jin_pembangun" :
            totJinban += 1
    n = totJinban# jumlah jin pembangun
    if n > 0 : # jika ada jin pembangun
        pasir = [0 for i in range(n)]
        batu = [0 for i in range(n)]
        air = [0 for i in range(n)]
        mat = [pasir,batu,air]
        for i in range(3) : 
            for j in range(n) :
                mat[i][j] = rand()
        sumpas = 0
        sumbat = 0 
        sumair = 0
        for i in range(n) :
            sumpas += mat[0][j]
            sumbat += mat[1][j]
            sumair += mat[2][j]
        for row in csv.reader(bahanR) :
            tempMat = int(row[2])
        pasir_dari_csv = tempMat[0]
        batu_dari_csv = tempMat[1]
        air_dari_csv = tempMat[2]
        # check kesesuaian jumlah material dari csv file 
        if sumpas <= pasir_dari_csv and sumbat <= batu_dari_csv and sumair <= air_dari_csv :
            print(f"Mengerahkan {n} jin untuk membangun candi dengan total bahan {sumpas} pasir, {sumbat} batu, dan {sumair} air")
            print(f"Jin berhasil membangun total {n} candi")
            # kurangi material di csv bahan
            writer.writerow(['pasir', 'p', str(pasir_dari_csv - sumpas)])
            writer.writerow(['batu', 'b', str(batu_dari_csv - sumbat)])
            writer.writerow(['air', 'a', str(air_dari_csv - sumair)])
            # save candi yang udah dibangun di csv candi
        else : # jumlah material di csv tidak mencukupi
            print("Bangun gagal. Kurang ", end="")
            if sumpas > pasir_dari_csv and sumbat <= batu_dari_csv and sumair <= air_dari_csv : # cuma pasir yang kurang
                print(f"{sumpas-pasir_dari_csv} pasir.")
            elif sumbat > batu_dari_csv and sumpas <= pasir_dari_csv and sumair <= air_dari_csv : # cuma batu yang kurang
                print(f"{sumbat-batu_dari_csv} batu.")
            elif sumair > air_dari_csv and sumpas <= pasir_dari_csv and sumbat <= batu_dari_csv : # cuma air yang kurang
                print(f"{sumair-air_dari_csv} air.")
            elif sumpas > pasir_dari_csv and sumbat > batu_dari_csv and sumair <= air_dari_csv :  # pasir dan batu kurang
                print(f"{sumpas-pasir_dari_csv} pasir, dan {sumbat-batu_dari_csv} batu.")
            elif sumpas > pasir_dari_csv and sumair > air_dari_csv and sumbat <= batu_dari_csv : # pasir dan air kurang
                print(f"{sumpas-pasir_dari_csv} pasir, dan {sumair-air_dari_csv} air.")
            elif sumbat > batu_dari_csv and sumair > air_dari_csv and sumpas <= pasir_dari_csv : # batu dan air kurang
                print(f"{sumbat-batu_dari_csv} batu, dan {sumair-air_dari_csv} air.")
            else : # semua bahan kurang
                print(f"{sumpas-pasir_dari_csv} pasir, {sumbat-batu_dari_csv} batu, dan {sumair-air_dari_csv} air.")
    else : # tidak ada jin pembangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
            
