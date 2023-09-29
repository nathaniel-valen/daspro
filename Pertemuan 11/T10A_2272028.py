# File : T10A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima masukan
# dua buah array bilangan bulat berukuran N
# lalu akan menjumlahkan bilangan pada indeks yang sama
# Kamus Data
# n = var input untuk berapa banyak array (int)
# arr1 = var bilangan menghitung array
# arr2 = var bilangan menghitung array
# rest = var untuk hasil dari array
# tot = var untuk mendeklarasi result array

def main():
    n = int(input("N: "))

    arr1 = [None] * n
    arr2 = [None] * n

    for i in range(n):
        arr1[i] = int(input("A :"))

    for i in range(n):
        arr2[i] = int(input("B :"))

    rest = [None] * n

    tot = 0
    print(end="")
    for i in range(n):
        rest[i] = arr1[i] + arr2[i]
        tot += rest[i]
        print(rest[i],end=" ")
    print()
    print("Total :", tot, end=" ")

if __name__ == '__main__':
    main()
