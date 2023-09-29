# File : T11C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan meminta N 
# bilangan bulat lalu akan menampilkan
# bilangan ganjil saja, bilangan genap saja
# dan semua bilangan terurut menurun
# Kamus Data
# n var. int input banyak data dan panjang array
# arr array penampung
# i var. int indeks array
# temp var. int variabel penampung
# j var. int indeks array

def main():
    n = int(input("N : "))
    arr = n * [None]
    for i in range (0,n,1):
        arr[i] = int(input())

    print("The Ganjils : ",end=" ")
    for i in range (0,n,1):
        if arr[i] % 2 != 0:
            print(arr[i],end=" ")
    print()

    print("The Genaps : ",end=" ")
    for i in range (0,n,1):
        if arr[i] % 2 == 0:
            print(arr[i],end=" ")
    print()

    for i in range(0,n,1):
        for j in range(0,n-1,1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("Habis Diurutin : ",end=" ")
    for i in range(0,n,1):
        print(arr[i],end=" ")

if __name__ == '__main__':
    main()
