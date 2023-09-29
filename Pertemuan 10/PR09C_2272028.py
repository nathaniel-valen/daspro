# File : PR09C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima masukan N 
# buah judul buku dan sebuah kata lalu akan
# menampilkan semua judul buku dengan kata terkait.

# Kamus Lokal
# tit_book = var untuk judul buku
# w = var untuk kata yang ingin dicari
# rest = var untuk hasil kata yang dicari
# tit = var hasil judul yang dicari sesuai kata
# find_tit = var deklarasi pencarian sesuai judul
def find_judul(tit_book, w):
    rest = []
    for tit in tit_book:
        find_tit = tit.find(w)
        if find_tit != -1:
            rest += [tit]
    return rest

# Kamus Lokal
# x = var input bilangan (int)
# tit_book = var bilangan menghitung array
# tit_book[i] = var input bil sesuai loop (str)
# w = var input kata yang ingin dicari (str)
# rest = var hasil dari dari fungsi find_judul
def main():
    x = int(input("N : "))
    tit_book = [None] * x
    for i in range(x):
        tit_book[i] = str(input("Judul {}:".format(i+1)))

    w = str(input("Cari: "))

    print("Judul yang mengandung kata {}:".format(w))
    rest = find_judul(tit_book, w)
    for tit in rest:
        print(tit)

if __name__ == '__main__':
    main()