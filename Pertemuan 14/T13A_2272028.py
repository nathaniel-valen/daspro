# File : T13A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah program yang akan menerima masukan N
# buah bilangan dan sebuah bilangan bulat X
# lalu akan menampilkan “ketemu” jika X ada
# dalam N bilangan tersebut dan akan
# menampilkan “teu ketemu” jika sebaliknya. 

# Kamus Lokal
# ang = var iterator
# arr = var kumpulan array yang berisi angka (int)
# x = var cek apakah ada angka diarray atau tidak
def cariAngka(arr, x):
    for ang in arr:
        if ang == x:
            return "ketemu"
    return "teu ketemu"

# Kamus Lokal
# N = var input panjang arr
# arr = var deklarasi panjang array
# num = var input angka sepanjang array
# x = var input cari angka
# result = var deklarasi fungsi cariAngka
def main():

    N = int(input("N : "))
    arr = [None] * N

    for i in range(N):
        num = int(input())
        arr[i] = num

    x = int(input("Cari Angka : "))

    result = cariAngka(arr, x)
    print(result)

if __name__ == '__main__':
    main()