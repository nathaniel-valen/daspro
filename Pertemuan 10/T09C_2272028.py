# File : T09C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang kosakata yang akan meminta user
# untuk memasukkan 10 buah huruf.
# Huruf tersebut akan dijadikan sebuah kata oleh user
# dengan memasukkan 5 digit angka yang diinginkan oleh user. 
# Kamus Data
# huruf = var untuk array sampai ke-10
# huruf[i] = var input huruf sampai ke-10 (str)
# angka = var input 5 digit angka (int)
# kata = var deklarasi kata

def main():
    huruf = [""] * 10
    for i in range(0,10,1):
        huruf[i] = str(input())

    angka = int(input("Masukkan 5 digit angka: "))
    kata = str(angka)

    print("Kata yang telah dibuat :", end=" ")

    for j in range (0,5,1):
        print(huruf[int(kata[j])], end="")

if __name__ == '__main__':
    main()