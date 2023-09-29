# File : T03A_2272028.py
# Deskripsi :
# Program akan membaca data pegawai :
# Bagian Karyawan, Nomor Karyawan, Status Nikah,
# Jumlah Anak, Golongan, Jam Kerja
# Kamus Data
# bagKaryawan = var input bagian karyawan bertipe str
# noKaryawan = var input no karyawan bertipe int
# namaKaryawan = var input nama karyawan bertipe str
# statusKaryawan = var input nama karyawan bertipe str
# jumlahAnak = var input no karyawan bertipe int
# golKaryawan = var input no karyawan bertipe int
# jamKerja = var input no karyawan bertipe int
# k = deklarasi string Ketua untuk menjadi variabel
# s = deklarasi string Staff untuk menjadi variabel
# gajiTambahan = var untuk menghitung gaji bonus melalui var JamKerja
# gajiPokok = var untuk gaji pokok
# tunjangan = var untuk memberikan bonus tunjangan
# total = var untuk menjumlahkan gajiPokok + tunjangan + gajiTambahan

def main():
    
    # Perintah input
    
    bagKaryawan = input("Bagian Karyawan : ")
    noKaryawan = int(input("Nomor :"))
    namaKaryawan = input("Nama :")
    statusKaryawan = input("Status Nikah :")
    jumlahAnak = int(input("Jumlah Anak :"))
    golKaryawan = int(input("Golongan :"))
    jamKerja = int(input("Jam Kerja :"))

    # Perintah Proses
    
    k = "Ketua"
    s = "Staff"
    gajiTambahan = 1
    total = 1

    if (bagKaryawan == k):
        k = "K"
        if (golKaryawan == 1):
            print("Masuk")
            gajiPokok = 5000000
            if statusKaryawan == "Ya":
                print("Masuk 2")
                tunjangan = 500000 + (500000 * jumlahAnak)
            elif statusKaryawan == "Tidak":
                tunjangan = 3000000
            if jamKerja > 160:
                print("Masuk 3")
                gajiTambahan = 15000 * (jamKerja-160)
            else :
                gajiTambahan = 0
                
        elif (golKaryawan == 2):
            gajiPokok = 3500000
            if statusKaryawan == "Ya":
                tunjangan = 500000 + (350000 * jumlahAnak)
            elif statusKaryawan == "Tidak":
                tunjangan = 3000000
            if jamKerja > 160:
                gajiTambahan = 15000 * (jamKerja-160)
            else :
                gajiTambahan = 0
                
        elif (golKaryawan == 3):
            gajiPokok = 2500000
            if statusKaryawan == "Ya":
                tunjangan = 500000 + (250000 * jumlahAnak)
            elif statusKaryawan == "Tidak":
                tunjangan = 3000000
            if jamKerja > 160:
                gajiTambahan = 15000 * (jamKerja-160)
            else :
                gajiTambahan = 0
                
    elif (bagKaryawan == s):
        s = "S"
        if (golKaryawan == 1):
            gajiPokok = 5000000
            if statusKaryawan == "Ya":
                tunjangan = 500000 + (500000 * jumlahAnak)
            elif statusKaryawan == "Tidak":
                tunjangan = 3000000
            if jamKerja > 160:
                gajiTambahan = 15000 * (jamKerja-160)
            else :
                gajiTambahan = 0
                
        elif (golKaryawan == 2):
            gajiPokok = 3500000
            if statusKaryawan == "Ya":
                tunjangan = 500000 + (350000 * jumlahAnak)
            elif statusKaryawan == "Tidak":
                tunjangan = 3000000
            if jamKerja > 160:
                gajiTambahan = 15000 * (jamKerja-160)
            else :
                gajiTambahan = 0
                
        elif (golKaryawan == 3):
            gajiPokok = 2500000
            if statusKaryawan == "Ya":
                tunjangan = 500000 + (250000 * jumlahAnak)
            elif statusKaryawan == "Tidak":
                tunjangan = 3000000
            if jamKerja > 160:
                gajiTambahan = 15000 * (jamKerja-160)
            else :
                gajiTambahan = 0
                    
    total = gajiPokok + tunjangan + gajiTambahan

    # Perintah Output
    
    print("=====================================")
    print("NIP :", end=" ")
    if bagKaryawan == "Ketua" :
        print(k, end="")
    elif bagKaryawan == "Staff" :
        print(s, end= "")
    print("_",noKaryawan," - ",namaKaryawan, sep="")
    print("Gaji Pokok :",gajiPokok)
    print("Tunjangan :",tunjangan)
    print("Gaji Tambahan :", gajiTambahan)
    print("Total Gaji : ",total)

    
if __name__ == '__main__':
    main()

