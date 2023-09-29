# File : PR04A_2272028.py
# Deskripsi :
# Program menerima sebuah bilangan bulat hingka nilai 9999
# lalu akan menampilkan apakah bilangan tersebut genap atau tidak.
# Kamus Data
# n = input angka untuk diulang (integer)
# a = input angka untuk cek genap atau bukan genap (integer)

def main():
    # Perintah Input
    n = int(input("N :"))

    # Perintah Proses + Output
    for i in range(n):
        a = int(input("Angka :"))
        if( a % 2 == 0 and a <= 9999):
            print("Genap")
        elif( a <= 9999 ):
            print("Bukan Genap")
        else :
            print("Angka melebihi kapasitas")
    return 0

    
if __name__ == '__main__':
    main()
