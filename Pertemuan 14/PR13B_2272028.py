# File : PR13B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah program yang akan menerima masukan N
# buah bilangan dan string mode lalu akan
# menampilkan N bilangan tersebut secara terurut
# menaik atau menurun berdasarkan mode tersebut.
# Penting untuk diingat bahwa mode tersebut 
# hanya ada dua jenis yaitu “menaik” dan “menurun”
# Kamus Data
# N = var input panjang array
# Arr = var deklarasi array kosong sepanjang N
# mode = var input mode menaik/menurun
# sort = var deklarasi string
# num = var agar print tidak didalam array

def main():
    N = int(input("N : "))
    Arr = [None] * N

    for i in range(N):
        Arr[i] = int(input("Angka :"))

    mode = input("Masukkan mode (menaik/menurun): ")

    if mode == "menaik" or mode == "Menaik":
        for i in range(N-1):
            for j in range(i+1, N):
                if Arr[i] > Arr[j]:
                    Arr[i], Arr[j] = Arr[j], Arr[i]
    elif mode == "menurun" or mode == "Menurun":
        for i in range(N-1):
            for j in range(i+1, N):
                if Arr[i] < Arr[j]:
                    Arr[i], Arr[j] = Arr[j], Arr[i]
    else:
        print("Mode tidak valid. Program berhenti.")
        return

    sort = ""
    for num in Arr:
        sort += str(num) + " "
    print(sort)

if __name__ == '__main__':
    main()
