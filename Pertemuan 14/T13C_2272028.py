# File : T13C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah sebuah program yang meminta user
# untuk memasukkan sejumlah data Nrp dan Nama. 
# nrp dan nama tersebut akan disimpan ke dalam array
# Kamus Data
# jum_data = var input jumlah data
# nrp_list = var panjang array sebanyak jum_data
# nama_list = var panjang array sebanyak jum_data
# nrp = var input nrp
# name = var input nama
# cari = car input NRP yang dicari
# index = var deklarasi
def main():
    jum_data = int(input("Jumlah data: "))
    nrp_list = [None] * jum_data
    nama_list = [None] * jum_data

    for i in range(jum_data):
        nrp = int(input("NRP: "))
        name = str(input("Nama: "))
        nrp_list[i] = nrp
        nama_list[i] = name

    while True:
        cari = int(input("NRP yang dicari : "))
        if cari == 99999:
            break

        index = -1
        for i in range(len(nrp_list)):
            if nrp_list[i] == cari:
                index = i
                break
        
        if index != -1:
            print(f"Nama dari {cari} adalah {nama_list[index]}")
        else:
            print("Data NRP yang dicari tidak ditemukan")
    print("Selesaiiiii")

if __name__ == '__main__':
    main()