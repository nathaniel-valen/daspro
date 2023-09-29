# File : T08A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima masukan
# dua buah bilangan dan akan menampilkan 
# bilangan terkecil dari dua bilangan tersebut.

# Kamus Lokal
# a = var untuk bilangan pertama
# b = var untuk bilangan kedua
def terkecil(a, b):
    if a < b:
        return a
    else:
        return b
    
# Kamus Lokal
# bil_one = var input nilai a (int)
# bil_two = var input nilai b (int)
# res = var untuk hasil bilangan terkecil
def main():
    # Input dua bilangan
    bil_one = int(input("a :"))
    bil_two = int(input("b :"))

    # Memanggil fungsi terkecil() dan mencetak hasilnya
    res = terkecil(bil_one, bil_two)
    print("Bilangan terkecil: ", res)

if __name__ == '__main__':
    main()
