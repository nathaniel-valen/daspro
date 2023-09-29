# File : PR10B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# BBuatlah sebuah program yang menerima N
# nama MH beserta umurnya lalu akan
# menampilkan semua MH berumur tidak
# lebih kecil dari 17 dan namanya diawali huruf vocal.
# Asumsikan nama tidak mengandung spasi
# Kamus Data
# N = var input untuk berapa banyak array (int)
# A1 = var bilangan menghitung array nama
# A2 = var bilangan menghitung array umur
# NM = var input nama (str)
# age = var input umur (int)
# name = var deklarasi array nama

def main():
    N = int(input("Masukkan jumlah mahasiswa: "))

    A1 = [None] * N
    A2 = [None] * N

    for i in range(N):
        NM = str(input("Nama : "))
        age = int(input("Umur : "))
        A1[i] = NM
        A2[i] = age


    for j in range(N):
        name = A1[j]
        if age >= 17:
            if name[0] == 'a':
                print(name)
            elif name[0] == 'i':
                print(name)
            elif name[0] == 'u':
                print(name)
            elif name[0] == 'e':
                print(name)
            elif name[0] == 'o':
                print(name)

if __name__ == '__main__':
    main()
