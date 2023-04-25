def ayam_berkokok():
    print("Kukuruyuk.. Kukuruyuk..")
    with open('candi.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        count = 0
        for row in reader:
            count += 1
        jumlah_candi = count - 1 
        
    print(f"Jumlah Candi: {jumlah_candi}\n")
    
    if jumlah_candi >= 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("'Bandung Bondowoso angry noise'")
        print("Roro Jonggrang dikutuk menjadi candi.")
        
def hancurkan_candi():

    with open('candi.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        candi_list = list(reader)
    
    candi_id = input('Masukkan ID candi: ')
    
    index = -1
    for i in range(len(candi_list)):
        if candi_list[i][0] == candi_id:
            index = i
            break

    if index != -1:
        konfirmasi = input('Apakah anda yakin ingin menghancurkan candi dengan id:',candi_id,'(y/n)?')
        if konfirmasi == 'y':
            ncandi_list = []
            for i in range(len(candi_list)):
                if i != index:
                    new_candi_list.append(candi_list[i])
            candi_list = ncandi_list
            print('Candi telah berhasil dihgancurkan')
        else:
            print('Candi tidak jadi dihancurkan')
    else:
        print('Tidak ada candi dengan ID tersebut.')
    
    with open('candi.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(candi_list)
