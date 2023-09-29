# File : PR03B_2272028.py
# Deskripsi :
# Program  yang akan menentukan posisi dari
# sebuah titik terhadap titik acuan. 
# Kamus Data
# tgl = var input bertipe int
# bln = var input bertipe int
# thn = var input bertipe int


def main():

    # Perintah Input
    tgl = int(input("Tanggal :"))
    bln = int(input("Bulan :"))
    thn = int(input("Tahun :"))

    # Perintah Proses dan Output
    if(thn % 4 == 0) :
        if(1 <= bln <= 12) :
            if(bln == 1) :
                if(1 <= tgl <=31) :
                    print(tgl,"Januari",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 3) :
                if(1 <= tgl <=31) :
                    print(tgl,"Maret",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 4) :
                if(1 <= tgl <=30) :
                    print(tgl,"April",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 5) :
                if(1 <= tgl <=31) :
                    print(tgl,"Mei",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 6) :
                if(1 <= tgl <=30) :
                    print(tgl,"Juni",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 7) :
                if(1 <= tgl <=31) :
                    print(tgl,"Juli",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 8) :
                if(1 <= tgl <=31) :
                    print(tgl,"Agustus",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 9) :
                if(1 <= tgl <=30) :
                    print(tgl,"September",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 10) :
                if(1 <= tgl <=31) :
                    print(tgl,"Oktober",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 11) :
                if(1 <= tgl <=30) :
                    print(tgl,"November",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 12) :
                if(1 <= tgl <=31) :
                    print(tgl,"Desember",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")

            else :
                if(1 <= tgl <= 29) :
                    print(tgl,"Februari",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
        else :
            print("Masukan Salah, Tidak ada bulan",bln)
    else :
        if(1 <= bln <= 12) :
            if(bln == 1) :
                if(1 <= tgl <=31) :
                    print(tgl,"Januari",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 3) :
                if(1 <= tgl <=31) :
                    print(tgl,"Maret",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 4) :
                if(1 <= tgl <=30) :
                    print(tgl,"April",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 5) :
                if(1 <= tgl <=31) :
                    print(tgl,"Mei",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 6) :
                if(1 <= tgl <=30) :
                    print(tgl,"Juni",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 7) :
                if(1 <= tgl <=31) :
                    print(tgl,"Juli",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 8) :
                if(1 <= tgl <=31) :
                    print(tgl,"Agustus",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 9) :
                if(1 <= tgl <=30) :
                    print(tgl,"September",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 10) :
                if(1 <= tgl <=31) :
                    print(tgl,"Oktober",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 11) :
                if(1 <= tgl <=30) :
                    print(tgl,"November",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
            elif(bln == 12) :
                if(1 <= tgl <=31) :
                    print(tgl,"Desember",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")

            else :
                if(1 <= tgl <= 28) :
                    print(tgl,"Februari",thn)
                else :
                    print("Masukan Salah, Tidak ada tanggal",tgl,".")
        else :
            print("Masukan Salah, Tidak ada bulan",bln)
        
            
if __name__ == '__main__':
    main()

