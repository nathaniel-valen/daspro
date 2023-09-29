# File : PR03C_2272028.py
# Deskripsi :
# program yang akan memberikan struk dari pesanan yang diinput oleh user
# dari berbagai tempat minuman yang disediakan 
# Pertama program akan meminta nama pemesan.
# Kemudian program akan meminta inputan tempat, menu,
# dan size dari tiap tempat yang dipilih.
# Kamus Data
# nama = var input bertipe str
# tempat = var input bertipe int
# menu = var input bertipe int
# size = var input bertipe int
# harga = var untuk harga
# voucher = var bertipe str
# potongan = var untuk memberikan potongan harga
# total = var untuk menjumlahkan harga, ppn, dan potongan
# ppn = var untuk PPN


def main():
    
    # Perintah Input dan Output
    nama = input("Nama pemesan :")
    print("=======================")
    print("1. Mixu")
    print("2. Moonbucks")
    tempat = int(input("Silahkan Pilih Tempat :"))

    # Perintah Input Proses dan Output
    if( tempat == 1):
        print("=======================")
        print("Selamat datang di Mixu")
        print("======== Menu =========")
        print("1. Creamy mango Boba")
        print("2. Boba Sundae")
        print("3. Fresh Squeezed Lemonade")
        menu = int(input("Silahkan Pilih Menu :"))
        print("======= Ukuran ========")
        print("1. Unyu - 20000")
        print("2. Medium - 22000")
        print("3. Large - 24000")
        size = int(input("Mau ukuran apa: "))
        
        harga = 0
        if (menu == 1) :
            if size == 1:
                harga = 20000
            elif size == 2:
                harga = 22000
            elif size == 3:
                harga = 24000
            else:
                print("Ukuran yang Anda pilih tidak tersedia.")
        elif (menu == 2) :
            if size == 1:
                harga = 14000
            elif size == 2:
                harga = 16000
            elif size == 3:
                harga = 18000
            else:
                print("Ukuran yang Anda pilih tidak tersedia.")
        elif (menu == 3) :
            if size == 1:
                harga = 8000
            elif size == 2:
                harga = 10000
            elif size == 3:
                harga = 12000
            else:
                print("Ukuran yang Anda pilih tidak tersedia.")
        else :
            print("Menu yang Anda pilih tidak tersedia.")

        if (harga != 0) :
            print("=======================")
            voucher = input("Masukkan kode voucher: ")
            potongan = 0
            if (voucher == "ILOVEMIXU") :
                potongan = 5000
                print("Kode voucher benar !!")
            else:
                print("Kode voucher salah !!")


            total = harga + (harga * 0.1) - potongan
            print("===== Pesanan Mixu =====")
            print("Nama:", nama)
            if (menu == 1) :
                print("Pesanan: Creamy mango Boba")
            elif (menu == 2) :
                print("Pesanan: Boba Sundae")
            elif (menu == 3) :
                print("Pesanan: Fresh Squeezed Lemonade")
            if (size == 1):
                print("Ukuran: Unyu")
            elif (size == 2) :
                print("Ukuran: Medium")
            elif (size == 3) :
                print("Ukuran: Large")
            print("Harga:", harga)
            print("PPN:", round(harga * 0.1))
            print("Potongan:", potongan)
            print("Total:", round(total))
            print("=======================")

    # Perintah Input Proses dan Output        
    elif( tempat == 2):
        print("=======================")
        print("Selamat datang di Moonbucks")
        print("======== Menu =========")
        print("1. Asian Dolce Latte")
        print("2. Caramel Java Chip")
        print("3. Mango Passion Fruit")
        menu = int(input("Silahkan Pilih Menu :"))
        print("======= Ukuran ========")
        print("1. Tall - 53000")
        print("2. Grande - 58000")
        print("3. Venti - 60000")
        size = int(input("Mau ukuran apa: "))

        harga = 0
        if (menu == 1) :
            if size == 1:
                harga = 53000
            elif size == 2:
                harga = 58000
            elif size == 3:
                harga = 60000
            else:
                print("Ukuran yang Anda pilih tidak tersedia.")
        elif (menu == 2) :
            if size == 1:
                harga = 58000
            elif size == 2:
                harga = 63000
            elif size == 3:
                harga = 67000
            else:
                print("Ukuran yang Anda pilih tidak tersedia.")
        elif (menu == 3) :
            if size == 1:
                harga = 45000
            elif size == 2:
                harga = 49000
            elif size == 3:
                harga = 52000
            else:
                print("Ukuran yang Anda pilih tidak tersedia.")
        else :
            print("Menu yang Anda pilih tidak tersedia.")

        if (harga != 0) :
            print("=======================")
            voucher = input("Masukkan kode voucher: ")
            potongan = 0
            if (voucher == "MOONBUCKSSUWU") :
                potongan = 20000
                print("Kode voucher benar !!")
            else:
                print("Kode voucher salah !!")


            total = harga + (harga * 0.1) - potongan
            print("===== Pesanan Moonbucks =====")
            print("Nama:", nama)
            if (menu == 1) :
                print("Pesanan: Asian Dolce Latte")
            elif (menu == 2) :
                print("Pesanan: Caramel Java Chip")
            elif (menu == 3) :
                print("Pesanan: Mango Passion Fruit")
            if (size == 1):
                print("Ukuran: Tall")
            elif (size == 2) :
                print("Ukuran: Grande")
            elif (size == 3) :
                print("Ukuran: Venti")
            print("Harga:", harga)
            print("PPN:", round(harga * 0.1))
            print("Potongan:", potongan)
            print("Total:", round(total))
            print("=======================")
        
            
            
if __name__ == '__main__':
    main()

