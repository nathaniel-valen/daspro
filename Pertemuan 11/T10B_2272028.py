# File : T10B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima dua buah
# array berukuran N dan M lalu akan menampilkan
# semua bilangan yang muncul di keduanya
# Kamus Data
# N = var input untuk berapa banyak array (int)
# arr1 = var bilangan menghitung array
# arr2 = var bilangan menghitung array
# simpan = var untuk menyimpan bilangan dari kedua array
# num1 = var iterator array pertama
# num2 = var iterator array kedua
# num = var input angka dalam array (int)

def main():
    N = int(input("N: "))
    arr1 = [None] * N
    for i in range(N):
        num = int(input())
        arr1[i] = num

    M = int(input("M: "))
    arr2 = [None] * M
    for i in range(M):
        num = int(input())
        arr2[i] = num

    simpan = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2:
                simpan = simpan + [num1]
                break

    print("Hasil irisan :", end=" ")
    for num in simpan:
        print(num, end=" ")

if __name__ == '__main__':
    main()
