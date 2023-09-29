# File : T10C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang kosakata yang akan
# meminta useruntuk memasukkan 10 buah huruf.
# Huruf tersebut akan dijadikan sebuah kata oleh
# user dengan memasukkan 5 digit angka yang 
# diinginkan oleh user. User akan terus menerus 
# memasukkan 5 digit angka sampai memasukkan 99999. 
# Kamus Data
# arr = var untuk array kosong max 10
# let = var input huruf (str)
# word = var deklarasi kata
# num = var input 5 digit angka (int)
# dig = var iterator
# simpan = var untuk menyimpan nilai integer

def main():
    arr = [None] * 10
    print("Masukkan 10 huruf:")
    for i in range(10):
        let = str(input())
        arr[i] = let

    word = ""
    num = input("Masukkan 5 digit angka (99999 untuk selesai): ")
    while num != "99999":
        for dig in num:
            simpan = int(dig)
            if simpan >= 0 and simpan < len(arr):
                word += arr[simpan]
        num = input("Masukkan 5 digit angka (99999 untuk selesai): ")
        if num != "99999":
            word += ", "
    print("Kata yang telah dibuat:")
    print(word)

if __name__ == '__main__':
    main()
