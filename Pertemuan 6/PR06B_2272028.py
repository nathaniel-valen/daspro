# File : PR06B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi : program menginput n sebagai inputan bil. bulat
# dan menampilkan deretan angka bil. prima 
# Kamus Data :
# n : var input (integer)
# ct : var inisialisasi jumlah bilangan prima
# bil_prima  : var pengecekan (boolean)
# x : var penyimpan bilangan yang ingin diperiksa
# i : var parameter loop (integer)

def main():
    n = int(input("Masukkan bilangan : "))

    ct = 0
    x = 2

    print("===========================")
    print("Bilangan prima yang didapat:")

    while ct < n:
        bil_prima = True
        for i in range(2, x):
            if x % i == 0:
                bil_prima = False
                break
        if bil_prima:
            print(x, end=" ")
            ct += 1
        x += 1 
if __name__ == '__main__':
    main()