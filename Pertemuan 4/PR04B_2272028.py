# File : PR04B_2272028.py
# Deskripsi :
# Program menerima sebuah bilangan bulat hingka nilai 9999
# lalu akan menampilkan apakah bilangan tersebut genap atau tidak.
# Kamus Data
# n = var input angka(integer)
# x = var untuk deklarasi
# y = var untuk deklarasi
# z = var untuk deklarasi

def main():
    # Deklarasi Variabel
    x = 0
    y = 0
    z = 0

    # Perintah Input dan Output
    n = int(input("n :"))
    print(z, end=" ")

    # Perintah Proses dan Output
    for i in range(1,n,1):
        if(i == 1):
            x = 0
            y = 0
            z = 1
        else :
            y = x
            x = z
            z = x + y
        if(n - 1 == 1):
            print(x)
        else:
            print(z,end=" ")

    
if __name__ == '__main__':
    main()
