# File : T12B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah program yang akan menerima masukan N*N
# buah bilangan lalu akan menampilkan jumlah
# nilai per kolom.

# Kamus Lokal
# arr = var array kosong dengan max sesuai dimensi 1
# arr[i] = var array kosong dengan max sesuai dimensi 2
# d1 = var deklarasi hasil input N pertama 
# d2 = var deklarasi hasil input N kedua
def DeklarasiMatriks(d1, d2):
    arr = [None] * d1
    for i in range(d1):
        arr[i] = [None] * d2
    return arr

# Kamus Lokal
# N = var input ukuran matrix1 (int)
# A = var deklarasi fungsi deklarasiMatriks
# i = var iterator
# j = var iterator
# tot_kolom = var deklarasi (int)
# dek_str = var deklarasi (str)
def main():
    N = int(input("Masukkan nilai N: "))
    A = DeklarasiMatriks(N, N)

    print("Masukkan elemen-elemen matriks A:")
    for i in range(N):
        for j in range(N):
            print("A[{}, {}]:".format(i, j), end=" ")
            A[i][j] = int(input("Nilai:"))

    print("Matriks A:")
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=" ")
        print()

    print("Column:")
    for j in range(N):
        tot_kolom = 0
        dek_str = ""
        for i in range(N):
            tot_kolom += A[i][j]
            if i == 0:
                dek_str += str(A[i][j])
            else:
                dek_str += " + " + str(A[i][j])
        print(dek_str + " =", tot_kolom)

if __name__ == '__main__':
    main()