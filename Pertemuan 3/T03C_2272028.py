# File : T03C_2272028.py
# Deskripsi :
# Program akan membaca data pegawai :
# Bagian Karyawan, Nomor Karyawan, Status Nikah,
# Jumlah Anak, Golongan, Jam Kerja
# Kamus Data
# number = var input bertipe int
# konversi = var hasil konversi

def main():
    # Perintah Input
    number = int(input("Angka :"))

    # Perintah Proses
    
    if number == 0:
        print("nol")
    elif number == 10:
        print("sepuluh")
    elif number == 11:
        print("sebelas")
    elif number == 12:
        print("dua belas")
    elif number == 13:
        print("tiga belas")
    elif number == 14:
        print("empat belas")
    elif number == 15:
        print("lima belas")
    elif number == 16:
        print("enam belas")
    elif number == 17:
        print("tujuh belas")
    elif number == 18:
        print("delapan belas")
    elif number == 19:
        print("sembilan belas")
    elif number == 1000:
        print("seribu")
    elif number == 10000:
        print("sepuluh ribu")
    else:
        konversi = ""

        #Konversi Ribuan
        if number >= 1000:
            if number // 1000 == 2:
                konversi += "dua ribu "
            elif number // 1000 == 3:
                konversi += "tiga ribu "
            elif number // 1000 == 4:
                konversi += "empat ribu "
            elif number // 1000 == 5:
                konversi += "lima ribu "
            elif number // 1000 == 6:
                konversi += "enam ribu "
            elif number // 1000 == 7:
                konversi += "tujuh ribu "
            elif number // 1000 == 8:
                konversi += "delapan ribu "
            elif number // 1000 == 9:
                konversi += "sembilan ribu "
            number %= 1000
        # Konversi Ratusan
        if number >= 100:
            if number // 100 == 1:
                konversi += "seratus "
            elif number // 100 == 2:
                konversi += "dua ratus "
            elif number // 100 == 3:
                konversi += "tiga ratus "
            elif number // 100 == 4:
                konversi += "empat ratus "
            elif number // 100 == 5:
                konversi += "lima ratus "
            elif number // 100 == 6:
                konversi += "enam ratus "
            elif number // 100 == 7:
                konversi += "tujuh ratus "
            elif number // 100 == 8:
                konversi += "delapan ratus "
            elif number // 100 == 9:
                konversi += "sembilan ratus "
            number %= 100
        
        # Konversi Puluhan
        if number >= 20:
            if number // 10 == 2:
                konversi += "dua puluh "
            elif number // 10 == 3:
                konversi += "tiga puluh "
            elif number // 10 == 4:
                konversi += "empat puluh "
            elif number // 10 == 5:
                konversi += "lima puluh "
            elif number // 10 == 6:
                konversi += "enam puluh "
            elif number // 10 == 7:
                konversi += "tujuh puluh "
            elif number // 10 == 8:
                konversi += "delapan puluh "
            elif number // 10 == 9:
                konversi += "sembilan puluh "
            number %= 10
                
        # Konversi Satuan
        if number == 1:
            konversi += "satu"
        elif number == 2:
            konversi += "dua"
        elif number == 3:
            konversi += "tiga"
        elif number == 4:
            konversi += "empat"
        elif number == 5:
            konversi += "lima"
        elif number == 6:
            konversi += "enam"
        elif number == 7:
            konversi += "tujuh"
        elif number == 8:
            konversi += "delapan"
        elif number == 9:
            konversi += "sembilan"
            
        # Perintah Output
        print("Hasil konversi:")
        print(konversi)
    
if __name__ == '__main__':
    main()

