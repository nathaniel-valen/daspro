# File : T12A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah program yang akan menerima masukan N*N
# buah bilangan lalu akan menampilkan bilangan
# matriks dalam pola berikut.
# N harus selalu bilangan ganjil

# Kamus Lokal
# arr = var array kosong dengan max sesuai dimensi 1
# arr[i] = var array kosong dengan max sesuai dimensi 2
# d1 = var deklarasi hasil input N pertama 
# d2 = var deklarasi hasil input N kedua
def deklarasiMatriks(d1, d2) :
    arr = [None] * d1
    for i in range (0, d1, 1) :
        arr[i] = [None] * d2
    return arr

# Kamus Lokal
# N = var input ukuran matrix1 (int)
# A = var deklarasi fungsi deklarasiMatriks
# i = var iterator
# j = var iterator
def main() :
    N = int(input("N: ")) 
    while (N % 2 != 1) :
        N = int(input("N: "))

    A = deklarasiMatriks(N, N)

    print("Masukkan elemen-elemen matriks A:")
    for i in range(N):
        for j in range(N):
            print("A[{}, {}]:".format(i, j), end=" ")
            A[i][j] = int(input("Nilai:"))

    print("hasil")
    for i in range(0, N) :
        for j in range(0, N) :
            if (i == 0 or i == (N - 1)) :
                print(A[i][j], end=" ")
            elif (j == 0 or j == (N - 1)):
                print(A[i][j], end=" ")
            elif ((i == j) or (j + i == N - 1)):
                print(A[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()
    return 0

if __name__ == '__main__' :
    main()