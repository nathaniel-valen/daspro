# File : T12C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah program yang akan menerima masukan jumlah siswa.
# Kemudian buatlah 2 buah matriks,
# pertama untuk menyimpan kelas dan nama siswa,
# kedua untuk untuk menyimpan nilai
# UTS, UAS, dan KAT setiap siswa.

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
# rata = var deklarasi rata-rata
# nilai = var untuk nilai (int)
# persenan = var untuk persenan (int)
def RataNilai(nilai, persenan):
    rata = 0
    for i in range(len(nilai)):
        rata += nilai[i] * persenan[i]
    return rata / sum(persenan)

# Kamus Lokal
# rata_siswa = var deklarasi var array kosong
# rata_kecil = var deklarasi rata-rata terkecil (int)
# kelas kecil = var deklarasi kelas terkecil (none)
# nama_kecil = var deklarasi nama terkecil (none)
# siswa = var input total siswa (int)
# kls_nama = var pemanggilan fungsi DeklarasiMatriks
# nilai = var pemanggilan fungsi DeklarasiMatriks
# kls = var input kelas (str)
# nama = var input nama (str)
# nilai [i][0] = var input nilai KAT (int)
# nilai [i][1] = var input nilai KAT (int)
# nilai [i][2] = var input nilai KAT (int)
# K_A_T = var input persentase KAT (float)
# U_T_S = var input persentase UTS (float)
# U_A_S = var input persentase UAS (float)
# rata = var pemanggilan fungsi RataNilai
def main():

    rata_siswa = []
    rata_kecil = 101
    kelas_kecil = None
    nama_kecil = None
    siswa = int(input("Jumlah siswa: "))
    kls_nama = DeklarasiMatriks(siswa, 2)
    nilai = DeklarasiMatriks(siswa, 3)

    for i in range(siswa):
        print("=" * 40)
        kls = str(input("Kelas: "))
        nama = str(input("Nama: "))
        nilai[i][0] = int(input("Nilai KAT: "))
        nilai[i][1] = int(input("Nilai UTS: "))
        nilai[i][2] = int(input("Nilai UAS: "))
        kls_nama[i][0] = kls
        kls_nama[i][1] = nama
        
    print("=" * 40)
    print("Masukkan persenan nilai:")
    K_A_T = float(input("KAT: "))
    U_T_S = float(input("UTS: "))
    U_A_S = float(input("UAS: "))

    for i in range(siswa):
        nama = kls_nama[i][1]
        rata = RataNilai(nilai[i], [K_A_T, U_T_S, U_A_S])
        rata_siswa += [(nama, rata)]
    print("=" * 40)
    for i in range(siswa):
        nama = rata_siswa[i][0]
        rata = rata_siswa[i][1]
        kls = kls_nama[i][0]
        print("Kelas {} dengan nama {} rata-ratanya {}".format(kls, nama, rata))
        if rata < rata_kecil:
                rata_kecil = rata
                kelas_kecil = kls
                nama_kecil = nama

    print("=" * 40)
    print("Rata-rata terkecil diperoleh oleh {} dari Kelas {}".format(nama_kecil, kelas_kecil))

if __name__ == '__main__':
    main()