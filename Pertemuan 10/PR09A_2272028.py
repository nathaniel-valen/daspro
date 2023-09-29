# File : PR09A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah sebuah program yang menerima N
# bilangan bulat lalu akan menampilkan
# bilangan kedua terkecil.
# Kamus Data
# x = var input bilangan (int)
# P = var bilangan menghitung array
# P[i] = var input bilangan sesuai looping (int)
# i = var iterator
# j = var iterator
# k = var iterator
# temp = var simpan sementara k ke- berapa
# P[k] = var simpan nilai array di for k
# P[k+1] = var untuk check besar kecilnya [P] 

def main():
    x = int(input("N :"))
    P = [None] * x

    for i in range(x):
        P[i] = int(input())
    for j in range(0,x,1):
        for k in range(0,x-1,1):
            if (P[k+1] < P[k]):
                temp = P[k]
                P[k] = P[k+1]
                P[k+1] = temp
    print("Hasil :",P[1])


if __name__ == '__main__':
    main()