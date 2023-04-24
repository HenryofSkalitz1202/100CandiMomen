import csv

def ayam_berkokok():
    print("Kukuruyuk.. Kukuruyuk..\n")
    with open('candi.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) 
        jumlah_candi = sum(1 for row in reader)
    
    print(f"Jumlah Candi: {jumlah_candi}\n")
    
    if jumlah_candi >= 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("'Bandung Bondowoso angry noise'")
        print("Roro Jonggrang dikutuk menjadi candi.")
        


