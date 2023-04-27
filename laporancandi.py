candi = read_candi("candi.csv")


def laporcandi() :
    # total candi : ...
    totalcan = 0
    for i in range(100) : 
        if candi[i][1] != "" : # if candinya ada pembuat (ada candi)
        totalcan += 1 
    print("Total Candi: " + str(totalcan)) 
    
    # total pasir yang digunakan : ...
    # total batu yang digunakan : ...
    # total air yang digunakan : ... 
    matbahan = [0,0,0] # isi total bahan sementara
    for i in range(100) : 
        matbahan[0] += int(candi[i][2]) # pasir
        matbahan[1] += int(candi[i][3]) # batu
        matbahan[2] += int(candi[i][4]) # air
    print("Total Pasir yang digunakan: " + str(matbahan[0]))
    print("Total Batu yang digunakan: " + str(matbahan[1]))
    print("Total Air yang digunakan: " + str(matbahan[2]))
   
    # ID candi termahal: idx (Rp...) 
    # ID candi termurah: idx (Rp...)
    # Harga candi (Rp) : 10000 * Pasir + 15000 * Batu + 7500 * Air
    prices = [[0, 0] for i in range(100)] # [price, index]
    for i in range(100) : 
        prices[i][0] = int(candi[i][2]) * 10000 + int(candi[i][3]) * 15000 + int(candi[i][4]) * 7500
        prices[i][1] = candi[i][0]
    for i in range(100) : # sort list of prices
        for j in range(i + 1, 100) :
            if prices[i][0] > prices[j][0] :
                temp = prices[i]
                prices[i] = prices[j]
                prices[j] = temp
    maxprice = prices[99][0] # nilainya pasti ; idx pasti juga karena sorted from lowest -> highest val
    idxmax = prices[99][1]
    minprice = prices[99][0] # nilainya belum pasti karena ada nilai yg 0 atau blm ada inputan
    idxmin = 0
    for i in range(100) :
        if prices[i][0] != 0 : # if value is valid (bukan bernilai 0 karena no value di file)
            if prices[i][0] < minprice :
                minprice = prices[i][0]
                idxmin = i
    # algoritma utk penulisan output harga candi (Rp 100.000 contoh^)
    tempmax = maxprice
    tempmin = minprice
    countM = 0
    while tempmax > 0: # bilangan bisa dibagi 1000 sebanyak countM kali
        tempmax = tempmax//(1000**countM)
        if tempmax > 0 :
            countM+= 1 
    countN = 0
    while tempmin > 0:
        tempmin = tempmin//(1000**countN)
        if tempmin > 0 :
            countN += 1 
    strmax = str(maxprice) # ubah bentuk jadi array of chars
    nmax = len(strmax) + countM 
    strmin = str(minprice)
    nmin = len(strmin) + countN
    maxhead = len(str(maxprice // (1000**countM))) # contoh : 12.000.000 -> 2 bilangan di depan
    minhead = len(str(minprice // (1000**countN)))
    
    outmax = ["" for i in range(nmax)] # panjang array baru ditambah "." disetiap kelipatan 1000
    outmin = ["" for i in range(nmin)]
    
    incr = 0 # increment (penggeser indeks sementara)
    for i in range(nmax-countM) :
        # selama belum melewati "head" nya, incr tidak dipakai
        if i >= maxhead : 
            if (i-maxhead) % 3 == 0 :  # 
                incr += 1 
        outmax[i + incr] = strmax[i]
    for i in range(nmax) :
        if outmax[i] == "" :
            outmax[i] = "."   
    
    incr = 0
    for i in range(nmin-countN) :
        # selama belum melewati "head" nya, incr tidak dipakai
        if i >= minhead : 
            if (i-minhead) % 3 == 0 :  # 
                incr += 1 
        outmin[i + incr] = strmin[i]
    for i in range(nmin) :
        if outmin[i] == "" :
            outmin[i] = "." 
    
    outstrmax = ""
    outstrmin = ""
    for i in range(nmax) :
        outstrmax += outmax[i]
    for i in range(nmin) : 
        outstrmin += outmin[i]
    print("ID Candi Termahal: " + str(idxmax) + " (Rp " + outstrmax + ")")
    print("ID Candi Termurah: " + str(idxmin) + " (Rp " + outstrmin + ")")
