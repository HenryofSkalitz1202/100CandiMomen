bahan = read_bahan("bahan_bangunan.csv")
candi = read_candi("candi.csv")
user = read_user("user.csv")

def laporanjin() : 
    # total jin : ...
    totJin = 0 
    for i in range(102) : 
        if user[i][0] != "Bondowoso" or user[i][0] != "Roro" or user[i][0] != "": # cek username di idx ke-i apakah ada isi (selain roro dan bondowoso)
            totJin += 1
    print("Total Jin: " + str(totJin)) # output total jin

    # total jin pengumpul : ...
    totJinkum = 0
    for i in range(102) : 
        if user[i][2] == "jin_pengumpul" :
            totJinkum += 1 
    print("Total Jin Pengumpul: " + str(totJinkum))
    
    # total jin pembangun : ...
    totJinban = 0
    for i in range(102) : ##upd
        if user[i][2] == "jin_pembangun" :
            totJinban += 1 
    print("Total Jin Pembangun: " + str(totJinban))
    
    # nama jin terajin : ...
    listCan = [[""] for i in range(totJinban)]
    idx = 0
    for i in range(100) : 
        if candi[i][1] != "" :
            listCan[idx] = candi[i][1]
            idx += 1
    uniqname = [[""] for i in range(idx)] ##wip : list of unique names ; number of unique occurrences
    uniqocc = 0
    for i in range(idx) : 
        for j in range(i+1, idx) : 
            if listCan[i] != ""  and:
                if 
    freqMat = [["", 0] for i in range(uniqocc)] ##wip : traversal freqMat[i][1] max and min
    for i in range(totJinban) : 
        
    
    # nama jin termalas : ...
    
    
    # baca jumlah pasir, batu, dan air dari csv
    for i in range(3) : 
        tempMat[i] = bahan[i][2]
    pasir = tempMat[0]
    air = tempMat[2]
    batu = tempMat[1]
    # jumlah pasir : ...
    print("Jumlah Pasir: " + str(pasir) + " unit")
    # jumlah air : ...
    print("Jumlah Air: " + str(air) + " unit")
    # jumlah batu : ...
    print("Jumlah Batu: " + str(batu) + " unit")
# if jin pembangun = 0 then -> jin terajin & jin termalas : -
# 
