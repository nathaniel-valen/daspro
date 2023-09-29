# File : PR12C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deksripsi
# Buatlah program yang akan menerima map bom
# berukuran N*N (0 menyatakan kosong dan 1
# menyatakan bom) lalu akan menampilkan map
# baru dimana setiap posisi menandakan berapa banyak
# jumlah bom yang ada di sekitarnya.

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
# jum_peta = var deklarasi jumlah peta
# row = var hitung array ke 0 dikali N
# bomb = var var deklarasi array
# count = var deklarasi count
# i = iterator
# j = iterator
def hitungBom(bomb, n):
    jum_peta = []
    for _ in range(n):
        row = [0] * n
        jum_peta.append(row)

    for i in range(n):
        for j in range(n):
            if bomb[i][j] == 1:
                jum_peta[i][j] = "*"
            else:
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and bomb[ni][nj] == 1:
                            count += 1
                jum_peta[i][j] = count
    
    return jum_peta

# Kamus Lokal
# N = var input ukuran matriks (int)
# A = var hasil deklarasi matriks
# jum_peta = var deklarasi jumlah peta
# i = var iterator
# j = var iterator
def main():
    N = int(input("N: ")) 
    A = deklarasiMatriks(N, N)

    print("Masukkan elemen-elemen matriks A:")
    for i in range(N):
        for j in range(N):
            print("A[{}, {}]:".format(i, j), end=" ")
            A[i][j] = int(input())
        
    jum_peta = hitungBom(A, N)

    print("Output:")
    for i in range(N):
        for j in range(N):
            print(jum_peta[i][j], end=" ")
        print()
        
if __name__ =='__main__':
    main()
