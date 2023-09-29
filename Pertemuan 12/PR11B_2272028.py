# File : PR11B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima input
# satu bilangan decimal kemudian program akan
# menampilkan biner dari decimal tersebut.

# Kamus Lokal
# bin = var deklarasi string kosong
# dec = var bilangan desimal (int)
def printBinary(dec):
    bin = ""
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    bin = '0' * (8 - len(bin)) + bin

    for i in range (0,len(bin),1):
        print(bin[i], end=" ")

# Kamus Lokal
# dec = var input angka desimal (int)
def main():
    dec = int(input("Masukkan bilangan desimal: "))
    printBinary(dec)

if __name__ == '__main__':
    main()
