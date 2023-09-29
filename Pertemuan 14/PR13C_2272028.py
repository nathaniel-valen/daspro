# File : PR13C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah sebuah program yang memiliki 2 buah array.
# Array 1 untuk menampung nama siswa,
# sedangkan Array 2 untuk menampung nilai siswa.
# Kamus Data
# N = var input panjang array
# name = var deklarasi array kosong sepanjang N
# value = var deklarasi array kosong sepanjang N
# tot = var untuk menghitung total
# rata = var untuk mencari rata-rata

def main():
    N = int(input("Jumlah Siswa: "))
    name = [None] * N
    value = [None] * N

    tot = 0

    for i in range(N):
        print("=====================")
        name[i] = input("Nama: ")
        value[i] = int(input("Nilai: "))
        tot += value[i]

    for i in range(N - 1):
        for j in range(i + 1, N):
            if value[i] < value[j]:
                value[i], value[j] = value[j], value[i]
                name[i], name[j] = name[j], name[i]

    print("=====================")
    for i in range(N):
        print("{} {}".format(name[i], value[i]))

    print("Nilai terbesar diperoleh", name[0])
    rata = tot / N
    print("Nilai rata-rata:", round(rata,2))


if __name__ == '__main__':
    main()
