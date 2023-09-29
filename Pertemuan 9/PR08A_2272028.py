# File : PR09A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima masukan
# lima buah bilangan dan akan menampilkan bilangan
# kedua terkecil dari kelima bilangan tersebut

# Kamus Lokal
# kcl = var penyimpanan nilai a,b,c,d,e
# dua_kcl = var mencari nilai kecil kedua
def keduakecil(a,b,c,d,e):
    # mencari nilai terkecil dan kedua terkecil
    kcl = min(a,b,c,d,e)
    if a == kcl:
        dua_kcl = min(b,c,d,e)
    elif b == kcl:
        dua_kcl = min(a,c,d,e)
    elif c == kcl:
        dua_kcl = min(a,b,d,e)
    elif d == kcl:
        dua_kcl = min(a,b,c,e)
    else:
        dua_kcl = min(a,b,c,d)
    # mengembalikan nilai kedua terkecil
    return dua_kcl

# Kamus Lokal
# a = var input integer
# b = var input integer
# c = var input integer
# d = var input integer
# e = var input integer
# keduakecil(a,b,c,d,e) =
# var untuk memanggil fungsi keduakecil
def main ():
    # meminta pengguna memasukkan lima bilangan
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))
    d = int(input("Masukkan bilangan keempat: "))
    e = int(input("Masukkan bilangan kelima: "))

    # mencetak bilangan kedua terkecil
    print("Kedua terkecil: ", keduakecil(a,b,c,d,e))

if __name__ == "__main__":
    main()