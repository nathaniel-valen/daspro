# File : PR05C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program yang akan memberikan struk dari pesanan
# yang diinput oleh user dari 2 restoran yang disediakan.
# Pesanan pada masing-masing resto dapat diulang 
# sehingga dalam 1 pesanan bisa terdapat banyak menu makanan/minuman.
# Setelah memesan, akan ada tambahan biaya PPN sebesar 15% dari total pesanan
# Jika toko yang dipilih Solario,
# kode vouchernya “JAYAJAYA” dengan pengurangan harga
# sebanyak 8000.
# Jika toko yang dipilih Tobarob,
# kode vouchernya “FOLLOWYUK” dengan pengurangan harga
# sebanyak 15000.
# Kamus Data
# n = var input nama bertipe str
# pil_tmpt = var input tempat bertipe int
# tmpt = var untuk nama tempat
# menu1 = var untuk nama menu
# menu2 = var untuk nama menu
# menu3 = var untuk nama menu
# harga1 = var untuk harga menu 
# harga2 = var untuk harga menu
# harga3 = var untuk harga menu
# pil_pesan = var input pilihan pesanan bertipe int
# pil_menu = var input pilihan menu bertipe int
# prt_menu = var untuk print menu yang dibeli
# voc = var untuk input kode voucher bertipe str 
# pot = var untuk potongan harga
# total = var untuk menjumlahkan harga, ppn, dan potongan
# ppn = var untuk pajak ppn
# total = var harga total pembelian
# sub_total = var untuk menghitung semua hasil pembelian

def main():

    total = 0
    prt_menu = ""
    total = 0
    sub_total = 0
    ppn = 0
    pot = 0
    
    n = str(input("Nama Pemesan :"))
    print("="*30)
    print("1. Solario")
    print("2. Tobarob")
    pil_tmpt = int(input("Silahkan Pilih Tempat :"))
    print("="*30)

    if (pil_tmpt == 1):
        tmpt = "Solario"
        menu1 = "Nasi Goreng Seafood"
        menu2 = "Bihun Siram Ayam"
        menu3 = "Es Teh Manis"
        harga1 = 40000
        harga2 = 37000
        harga3 = 9000
    elif(pil_tmpt == 2):
        tmpt = "Tobarob"
        menu1 = "Ayam Panggang Itali"
        menu2 = "Dori Sambal Matah"
        menu3 = "Iced Rock Coffee"
        harga1 = 32000
        harga2 = 30000
        harga3 = 25000
    else :
        print("Masukkan tempat tidak ada !")

    print("Selamat datang di",tmpt)
    print("1. Pesan")
    print("2. Cetak Struk")
    pil_pesan = int(input("Pilihan :"))

    while(pil_pesan != 2):
        print("========Menu========")
        print("1.",menu1)
        print("2.",menu2)
        print("3.",menu3)
        pil_menu = int(input("Silahkan Pilihan Menu :"))

        if(pil_menu == 1):
            total += harga1
            prt_menu += menu1
        elif(pil_menu == 2):
            total += harga2
            prt_menu += menu2
        elif(pil_menu == 3):
            total += harga3
            prt_menu += menu3
        else :
            print("Masukkan Salah")
        
        print("Menu ditambahkan")
        print("1. Pesan")
        print("2. Cetak Struk")

        pil_pesan = int(input("Pilihan :"))

        if(pil_pesan == 1):
            prt_menu += ", "

    print("="*30)
    print("Masukkan kode voucher:")
    voc = str(input(""))
    
    if(pil_tmpt == 1):
        if(voc == "JAYAJAYA"):
            pot = 8000
            print("Kode voucher benar !!")
        else :
            print("Kode voucher salah !!")
    elif(pil_tmpt == 2):
        if(voc == "FOLLOWME"):
            pot = 15000
            print("Kode voucher benar !!")
        else :
            print("Kode voucher salah !!")
    
    print("===== Pesanan",tmpt,"=====")
    print("Nama :",n)
    print("Pesanan :", prt_menu)
    print("Harga :", total)
    
    ppn = total * 0.15
    print("PPN :",ppn)
    print("Potongan :", pot)
    sub_total = total + ppn - pot
    print("Total :",sub_total)
    print("="*30)
if __name__ == '__main__':
    main()