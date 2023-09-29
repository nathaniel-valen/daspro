# File : T11B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima dua
# buah array berukuran N dan M lalu akan
# menampilkan semua bilangan yang muncul di keduanya.

# Kamus Lokal
# arr = var deklarasi array kosong
# i = deklarasi untuk total inputan
# num = var input angka (int)
# arr = var untuk menambahkan angka ke array
def inputArr(length):
    arr = []
    i = 0
    while i < length:
        num = int(input())
        arr += [num]
        i += 1
    return arr

# Kamus Lokal
# rest = var deklarasi array kosong
# i = deklarasi untuk total inputan
# j = deklarasi untuk total inputan
# arr1 = var untuk hasil array pertama
# arr2 = var untuk hasil array kedua
def iris(arr1, arr2):
    rest = []
    i = 0
    while i < len(arr1):
        j = 0
        while j < len(arr2):
            if arr1[i] == arr2[j]:
                rest += [arr1[i]]
                break
            j += 1
        i += 1
    return rest

# Kamus Lokal
# N = var input panjang array pertama (int)
# M = var input panjang array kedua (int)
# arr1 = var untuk total panjang array pertama
# arr2 = var untuk total panjang array kedua
# hasil_irisan = var ubtuk iris dari arr1 dan arr2
# i = deklarasi untuk total inputan
def main():
    N = int(input("N: "))
    arr1 = inputArr(N)

    M = int(input("M: "))
    arr2 = inputArr(M)

    hasil_irisan = iris(arr1, arr2)

    print("Hasil irisan:", end=" ")
    i = 0
    while i < len(hasil_irisan):
        print(hasil_irisan[i], end=" ")
        i += 1

if __name__ == '__main__':
    main()
