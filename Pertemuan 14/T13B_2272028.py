# File : T13B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah sebuah program yang meminta N
# sebagai jumlah element array yang akan
# diisi oleh user. Kemudian minta user 
# untuk memasukan angka yang dicari. 

# Kamus Lokal
# n = var panjang kata didalam var arr
# i = var deklarasi
# x = var hasil input angka yang akan dicari
def sequential_search_with_sentinel(arr, x):
    n = len(arr)
    i = 0
    while i < n and arr[i] != x:
        i += 1
    if i == n:
        return f"Angka {x} tidak ditemukan"
    else:
        return f"Angka {x} ditemukan pada indeks ke-{i}"

# Kamus Lokal
# N = var input panjang arr
# arr = var deklarasi panjang array
# num = var input angka sepanjang array
# x = var input cari angka
# result = var fungsi sequential_search_with_sentinel  
def main():
    N = int(input("N : "))
    arr = [None] * N

    for i in range(N):
        num = int(input())
        arr[i] = num
    
    x = int(input("Angka yang dicari: "))
    result = sequential_search_with_sentinel(arr, x)
    print(result)

if __name__ == '__main__':
    main()