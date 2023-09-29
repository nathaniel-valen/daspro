# File : PR06A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program yang akan menerima masukan sebuah bilangan bulat
# lalu akan menampilkan pola segitiga
# Kamus Data
# n = var input angka (integer)
# i = var counter
# j = var counter

def main():
    n = int(input("n :"))

    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for j in range(2*i+2):
            print("*", end=" ")
        print()

if __name__ == '__main__':
    main()