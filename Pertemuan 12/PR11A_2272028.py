# File : PR11A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima masukan N
# buah bilangan lalu akan menampilkan bilangan yang
# memiliki kelipatan 3, kelipatan 5, kelipatan 7
# dan kelipatan 11.

# Kamus Lokal
# temp = var array kosong
# arr = var untuk panjang array
def printKelipatan3(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            temp += [arr[i]]
    if len(temp) > 0:
        print("Kelipatan 3 itu ada", end=" ")
        for i in range(len(temp)):
            if i > 0:
                print(", ", end="")
                if i == len(temp) - 1:
                    print("dan ", end="")
            print(temp[i], end="")
    else:
        print("Tidak ada kelipatan 3", end=" ")
    print()

# Kamus Lokal
# temp = var array kosong
# arr = var untuk panjang array
def printKelipatan5(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] % 5 == 0:
            temp += [arr[i]]
    if len(temp) > 0:
        print("Kelipatan 5 itu ada", end=" ")
        for i in range(len(temp)):
            if i > 0:
                print(", ", end="")
                if i == len(temp) - 1:
                    print("dan ", end="")
            print(temp[i], end="")
    else:
        print("Tidak ada kelipatan 5", end=" ")
    print()

# Kamus Lokal
# temp = var array kosong
# arr = var untuk panjang array
def printKelipatan7(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] % 7 == 0:
            temp += [arr[i]]
    if len(temp) > 0:
        print("Kelipatan 7 itu ada", end=" ")
        for i in range(len(temp)):
            if i > 0:
                print(", ", end="")
                if i == len(temp) - 1:
                    print("dan ", end="")
            print(temp[i], end="")
    else:
        print("Tidak ada kelipatan 7", end=" ")
    print()

# Kamus Lokal
# temp = var array kosong
# arr = var untuk panjang array
def printKelipatan11(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] % 11 == 0:
            temp += [arr[i]]
    if len(temp) > 0:
        print("Kelipatan 11 itu ada", end=" ")
        for i in range(len(temp)):
            if i > 0:
                print(", ", end="")
                if i == len(temp) - 1:
                    print("dan ", end="")
            print(temp[i], end="")
    else:
        print("Tidak ada kelipatan 11", end=" ")
    print()
    
# Kamus Lokal
# N = var input untuk menentukan panjang array (int)
# arrK = var untuk menghitung panjang array
def main():
    N = int(input("N: "))
    arrK = [None] * N
    for i in range(N):
        arrK[i] = int(input())
    printKelipatan3(arrK)
    printKelipatan5(arrK)
    printKelipatan7(arrK)
    printKelipatan11(arrK)

if __name__ == '__main__':
    main()
