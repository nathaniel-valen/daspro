# File: T01B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :  program yang akan menghitung total harga buah berdasarkan input user.
# Buah yang tersedia yaitu alpukat, apel dan jeruk.
# Harga alpukat yaitu 40.000, harga apel yaitu 35.000 dan harga jeruk yaitu 20.000

# Kamus
# nama_buah1, nama_buah2, nama_buah3 : variabel integer input untuk jumlah Kg masing-masing buah
# alpukat, apel, jeruk : variabel untuk harga masing-masing buah

# Program
def main():
    nama_buah1 = int(input("Jumlah Alpukat (Kg) :"))
    nama_buah2 = int(input("Jumlah Apel (Kg) :"))
    nama_buah3 = int(input("Jumlah Jeruk (Kg) :"))

    alpukat = 40000
    apel = 35000
    jeruk = 20000

    totalAlpukat = alpukat * nama_buah1 #Rumus1
    totalApel = apel * nama_buah2 #Rumus2
    totalJeruk = jeruk * nama_buah3 #Rumus3

    total = totalAlpukat + totalApel + totalJeruk #Rumus4

    print("====================================")
    print("Total Harga Buah Rp.", total)
if __name__ == '__main__':
    main()