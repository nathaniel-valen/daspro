# File : PR10A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah sebuah program yang menerima tiga buah
# array berukuran N lalu akan menampilkan
# nilai terbesar dari setiap indeks yang ada
# Kamus Data
# N = var input untuk berapa banyak array (int)
# A1 = var bilangan menghitung array
# A2 = var bilangan menghitung array
# A3 = var bilangan menghitung array
# num = var untuk input baris Array 1,2,3
# nmax = var menyimpan nilai terbesar setiap indeks
# value = var nilai terbesar dari setiap indeks


def main():
    N = int(input("Masukkan ukuran array: "))

    A1 = [None] * N
    A2 = [None] * N
    A3 = [None] * N
    print("Array 1:")
    for i in range(N):
        num = int(input())
        A1[i] = num

    print("Array 2:")
    for i in range(N):
        num = int(input())
        A2[i] = num

    print("Array 3:")
    for i in range(N):
        num = int(input())
        A3[i] = num

    nmax = [0] * N
    for j in range(N):
        if A1[j] > nmax[j]:
            nmax[j] = A1[j]
        if A2[j] > nmax[j]:
            nmax[j] = A2[j]
        if A3[j] > nmax[j]:
            nmax[j] = A3[j]

    print("Nilai terbesar:")
    for value in nmax:
        print(value, end=" ")

if __name__ == '__main__':
    main()
