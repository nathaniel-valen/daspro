# File : T09A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima masukan N
# bilangan bulat lalu akan menampilkan N bilangan
# terkait secara terbalik dan jumlah totalnya
# Kamus Data
# x = var input bilangan (int)
# P = var bilangan menghitung array
# P[i] = var input bilangan sesuai looping (int)
# tot = var untuk menghitung total

def main():
    x = int(input("N: "))
    P = [None] * x
    tot = 0

    for i in range(x):
        P[i] = int(input())
        tot += P[i]

    for i in range(x - 1, -1, -1):
        print(P[i], end=" ")
    print()

    print("Total:", tot)

if __name__ == '__main__':
    main()