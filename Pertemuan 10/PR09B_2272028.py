# File : PR09B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah sebuah program yang menerima N 
# bilangan bulat lalu akan menampilkan hasil
# penjumlahan setiap bilangan 
# dengan bilangan sebelumnya jika ada.
# Kamus Data
# x = var input bilangan (int)
# P = var bilangan menghitung array
# P[i] = var input bilangan sesuai looping (int)
# i = var iterator

def main():
    x = int(input("N :"))
    P = [None] * x

    for i in range(0,x,1):
        P[i] = int(input())
    for i in range(0,x,1):
        if (i == 0):
            print(P[i], end=" ")
        else:
            print(P[i] + (P[i - 1]), end=" ")

if __name__ == '__main__':
    main()