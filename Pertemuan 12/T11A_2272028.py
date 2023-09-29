# File : T11A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah sebuah program yang menerima N
# bilangan bulat lalu akan menampilkan bilangan
# kedua terkecil.
# Kamus Lokal
# n = var untuk panjang array
# min_num = var minimal angka
# K2 = var untuk deklarasi kedua terkecil
def getSecondMin(arr):
    n = len(arr)
    if n < 2:
        return None

    min_num = arr[0]
    K2 = None

    for i in range(1, n):
        if arr[i] < min_num:
            K2 = min_num
            min_num = arr[i]
        elif arr[i] != min_num and K2 == None or arr[i] < K2:
            K2 = arr[i]

    return K2

# Kamus Lokal
# N = var input panjang array (int)
# arr = var untuk total panjang array
# num = var untuk input angka (int)
# K2 = var untuk hasil dari bilangan kedua terkecil
def main():
    N = int(input("N : "))
    arr = [None] * N

    for i in range(N):
        num = int(input())
        arr[i] = num

    K2 = getSecondMin(arr)

    print("Bilangan kedua terkecil:", K2)

if __name__ == '__main__':
    main()
