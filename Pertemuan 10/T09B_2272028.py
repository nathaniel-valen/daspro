# File : T09B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima N buah bilangan
# lalu menampilkan bilangan pertama, terakhir,dan ditengah.
# Jika N genap, maka tampilkan kedua bilangan di tengah.
# Kamus Data
# x = var input bilangan (int)
# bil = var bilangan menghitung array
# bil[i] = var input bilangan sesuai looping (int)
# teng_kir = var untuk menghitung tengah kiri
# teng_kan = var untuk menghitung tengan kanan
# teng = var untuk menghitung tengah

def main():
    x = int(input("N : "))
    bil = [None] * x

    for i in range(x):
        bil[i] = int(input())
  
    print("Pertama:", bil[0])
    print("Terakhir:", bil[x-1])
    
    if x % 2 == 0:
        teng_kir = x // 2 - 1
        teng_kan = x // 2
        print("Tengah:", bil[teng_kir], bil[teng_kan])
    else:
        teng = x // 2
        print("Tengah:", bil[teng])

if __name__ == '__main__':
    main()