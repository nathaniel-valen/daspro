# File : PR12A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deksripsi
# Buatlah program yang akan menerima masukan
# N*N buah bilangan lalu akan menampilkan bilangan
# matriks setelah dirotasi ke kanan 90 derajat

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
    A = deklarasiMatriks(N, N)

    print("Masukkan elemen-elemen matriks A:")
    for i in range(N):
        for j in range(N):
            print("A[{}, {}]:".format(i, j), end=" ")
            A[i][j] = int(input("Nilai:"))
    
    for i in range (0,N,1):
        for j in range (N-1,-1,-1):
            print(A[j][i],end=' ')
        print()
    
if __name__ =='__main__':
    main()