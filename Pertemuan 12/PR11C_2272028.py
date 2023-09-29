# File : PR11C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah program yang kosakata yang akan
# meminta user untuk memasukan 10 buah huruf.
# Huruf tersebut akan dijadikan sebuah kata oleh
# user dengan memasukan 5 digit angka yang 
# diinginkan oleh user

# Kamus Lokal
# arrKata = var deklarasi array kosong max 10
# let = var input huruf (str)
# word = var deklarasi string kosong
# arrDigitAngka = var input angka max 5
# dig = var iterator for
# simpan = var hasil dari loop dig dan diubah menjadi int
def cariKata(arrKata, arrDigitAngka):
    arrKata = [None] * 10
    print("Masukkan 10 huruf:")
    for i in range(10):
        let = str(input())
        arrKata[i] = let

    word = ""
    arrDigitAngka = input("5 digit angka :")
    while arrDigitAngka != "99999":
        for dig in arrDigitAngka:
            simpan = int(dig)
            if simpan >= 0 and simpan < len(arrKata):
                word += arrKata[simpan]
        arrDigitAngka = input("5 digit angka :")
        if arrDigitAngka != "99999":
            word += ", "
    print("Kata yang telah dibuat:")
    print(word)

# Kamus Lokal
# arrKata = var deklarasi array kosong max 10
# arrDigitAngka = var deklarasi string
# cariKata(arrKata, arrDigitAngka) = var untuk memanggil fungsi
def main():
    arrKata = [None] * 10
    arrDigitAngka = ""
    cariKata(arrKata, arrDigitAngka)

if __name__ == '__main__':
    main()
