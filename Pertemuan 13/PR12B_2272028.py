# File : PR12B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deksripsi
# Buatlah program yang akan menerima masukan
# dua buah N*N buah bilangan lalu akan menampilkan
# matriks baru yang setiap elemennya merupakan
# penjumlahan nilai pada posisi yang sama dari kedua
# matriks awal.

# Kamus Lokal
# arr = var array kosong dengan max sesuai dimensi 1
# arr[i] = var array kosong dengan max sesuai dimensi 2
# d1 = var deklarasi hasil input N pertama 
# d2 = var deklarasi hasil input N kedua
def deklarasiMatriks(d1, d2):
    arr = [None] * d1
    for i in range(d1):
        arr[i] = [None] * d2
    return arr


# Kamus Lokal
# rest_matrix = var deklarasi pemanggilan fungsi
# m1 = var untuk inisialisasi matrix 1
# m2 = var untuk inisialisasi matrix 2
# i = iterator
# j = iterator
def tambahMatriks(m1, m2, n):
    rest_matrix = deklarasiMatriks(n, n)

    for i in range(n):
        for j in range(n):
            rest_matrix[i][j] = m1[i][j] + m2[i][j]

    return rest_matrix

# Kamus Lokal
# N = var input ukuran matrix1 (int)
# m1 = var deklarasi fungsi deklarasiMatriks 1
# m2 = var deklarasi fungsi deklarasiMatriks 2
# res = var deklarasi fungsi tambahMatriks
# row = iterator
# row_str = var deklarasi string kosong
# i = var iterator
# j = var iterator
def main():
    N = int(input("N: "))
    m1 = deklarasiMatriks(N, N)
    m2 = deklarasiMatriks(N, N)

    print("Masukkan elemen-elemen matriks A:")
    for i in range(N):
        for j in range(N):
            m1[i][j] = int(input("A[{}, {}]: ".format(i, j)))

    print("Masukkan elemen-elemen matriks B:")
    for i in range(N):
        for j in range(N):
            m2[i][j] = int(input("B[{}, {}]: ".format(i, j)))

    res = tambahMatriks(m1, m2, N)

    print("Output:")
    for row in res:
        row_str = ""
        for i in range(len(row)):
            row_str += str(row[i])
            if i != len(row) - 1:
                row_str += " "
        print(row_str)




if __name__ == '__main__':
    main()
