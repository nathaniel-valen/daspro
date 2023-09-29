# File : PR09C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program untuk menghitung gaji seorang pegawai

# Kamus Lokal
# gaPok = var untuk gaji pokok
# tunjKes = var untuk tunjangan kesehatan
# tunjKel = var untuk tunjagan keluarga
def hitungGajiKotor(gaPok, tunjKel, tunjKes):
    return gaPok + tunjKel + tunjKes

# Kamus Lokal
# gaTor = var untuk gaji kotor
def hitungPajak(gaTor):
    if gaTor > 3000000:
        return gaTor * 0.05
    else:
        return 0
# Kamus Lokal
# gaTor = var untuk gaji kotor
# pajak = var untuk pajak
def hitungGajiBersih(gaTor, pajak):
    return gaTor - pajak

# Kamus Lokal
# n = var input nama (str)
# gol = var input golongan (int)
# sT_nikah = var input status nikah (str)
# gaPok = var untuk gaji pokok
# tunjKes = var untuk tunjangan kesehatan
# tunjKel = var untuk tunjangan keluarga
# pajak = var untuk pajak
# gaTor = var untuk gaji kotor
# gaBer = var untuk gaji bersih
def cetakSlipgaji(n, gaPok, tunjKel, tunjKes, gaTor, pajak, gaBer):
    print("Nama: ", n)
    print("Gaji Pokok: ", gaPok)
    print("Tunjangan Kesehatan: ", tunjKes)
    print("Tunjangan Keluarga: ", tunjKel)
    print("========================================")
    print("Gaji Kotor: ", gaTor)
    print("Pajak: ", pajak)
    print("Gaji Bersih: ", gaBer)
    print("========================================")

# Kamus Lokal
# n = var input nama (str)
# gol = var input golongan (int)
# sT_nikah = var input status nikah (str)
# gaPok = var untuk gaji pokok
# tunjKes = var untuk tunjangan kesehatan
# tunjKel = var untuk tunjangan keluarga
# gaTor = var untuk gaji kotor
# gaBer = var untuk gaji bersih
def main():

    n = str(input("Nama: "))
    gol = int(input("Golongan: "))
    sT_nikah = input("Status Nikah: ")
    gaPok = 0
    tunjKes = 0
    tunjKel = 0

    if gol == 1:
        gaPok = 3500000
        tunjKes = 750000
    elif gol == 2:
        gaPok = 3000000
        tunjKes = 500000
    elif gol == 3:
        gaPok = 2500000
        tunjKes = 400000
    elif gol == 4:
        gaPok = 2000000
        tunjKes = 300000

    if sT_nikah == 'k':
        tunjKel = gaPok * 0.1

    gaTor = hitungGajiKotor(gaPok, tunjKel, tunjKes)
    pajak = hitungPajak(gaTor)
    gaBer = hitungGajiBersih(gaTor, pajak)

    cetakSlipgaji(n, gaPok, tunjKel, tunjKes, gaTor, pajak, gaBer)

if __name__ == "__main__":
    main()