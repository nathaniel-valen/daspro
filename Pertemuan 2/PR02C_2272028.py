# File : PR02C_2272028.py
# Deskripsi :
# Progman penjualan di sebuah toko Code Clothing.
# Toko ini menjual beberapa pakaian:
# Kaos memiliki pilihan warna yaitu:maroon,navy,lilac
# Kemeja memiliki pilihan motif yaitu:kotak-kotak,polos
# harga apel = 35.000
# harga jeruk = 20.000.
# Kamus Data
# hargaJaket = var untuk harga satuan jaket
# hargaKaos = var untuk harga satuan kaos
# hargaKemeja = var untuk harga satuan kemeja
# jenis = var input untuk jenis pakaian bertipe string
# bridge = var untuk mendeklarasikan bahan,motif, dan warna
# bahan = var input bertipe string
# ukuran = var input bertipe string
# harga = var untuk menghitung operasi dan menjadi total harga
# bayar = var bertipe integer untuk uang pembayaran
# kembalian = variabel untuk menghitung kembalian

def main():

    # harga awal jenis
    hargaJaket = 150000
    hargaKaos = 70000
    hargaKemeja = 100000

    # perintah input
    print("==========================================================")
    jenis = input("Jenis Pakaian (kaos/kemeja/jaket) :")
    
    # perintah output
    if( jenis == "jaket") :
        bridge = "berbahan"
        bahan = input("Bahan jaket(b. baby terry, d. denim, t. taslan) :")
        if(bahan == "b"):
            bahan = "baby terry"
            ukuran = input("Ukuran Pakaian (s/m/l) :")
            if(ukuran == "s"):
                    harga = hargaJaket
            elif(ukuran == "m"):
                    harga = hargaJaket + (hargaJaket * 0.2)
            elif(ukuran == "l"):
                    harga = hargaJaket + (hargaJaket * 0.4)
        elif(bahan == "d"):
            bahan = "denim"
            ukuran = input("Ukuran Pakaian (s/m/l) :")
            if(ukuran == "s"):
                    harga = hargaJaket
            elif(ukuran == "m"):
                    harga = hargaJaket + (hargaJaket * 0.2)
            elif(ukuran == "l"):
                    harga = hargaJaketc+ (hargaJaket * 0.4)
        elif(bahan == "t"):
            bahan = "taslan"
            ukuran = input("Ukuran Pakaian (s/m/l) :")
            if(ukuran == "s"):
                harga = hargaJaket
            elif(ukuran == "m"):
                harga = hargaJaket + (hargaJaket * 0.2)
            elif(ukuran == "l"):
                harga = hargaJaketc+ (hargaJaket * 0.4)
    elif( jenis == "kaos"):
        bridge = "berwarna"
        bahan = str(input("Pilhan Warna(m. maroon, n. navy, l. lilac) :"))
        if(bahan == "m"):
            bahan = "maroon"
            ukuran = str(input("Ukuran Pakaian (s/m/l) :"))
            if(ukuran == "s"):
                harga = hargaKaos
            elif(ukuran == "m"):
                harga = hargaKaos +(hargaKaos * 0.2)
            elif(ukuran == "l"):
                harga = hargaKaos +(hargaKaos * 0.4)
        elif(bahan == "n"):
            bahan = "navy"
            ukuran = str(input("Ukuran Pakaian (s/m/l) :"))
            if(ukuran == "s"):
                harga = hargaKaos
            elif(ukuran == "m"):
                harga = hargaKaos +(hargaKaos * 0.2)
            elif(ukuran == "l"):
                harga = hargaKaos +(hargaKaos * 0.4)
        elif(bahan == "l"):
            bahan = "lilac"
            ukuran = str(input("Ukuran Pakaian (s/m/l) :"))
            if(ukuran == "s"):
                harga = hargaKaos
            elif(ukuran == "m"):
                harga = hargaKaos +(hargaKaos * 0.2)
            elif(ukuran == "l"):
                harga = hargaKaos +(hargaKaos * 0.4)
                
    elif( jenis == "kemeja"):
        bridge = "bermotif"
        bahan = str(input("Pilhan Motif(k. kotak-kotak,p. polos) :"))
        if(bahan == "k"):
            bahan = "kotak-kotak"
            ukuran = str(input("Ukuran Pakaian (s/m/l) :"))
            if(ukuran == "s"):
                harga = hargaKemeja
            elif(ukuran == "m"):
                harga = hargaKemeja + (hargaKemeja * 0.2)
            elif(ukuran == "l"):
                harga = hargaKemeja + (hargaKemeja * 0.4)
        elif(bahan == "p"):
            bahan = "polos"
            ukuran = str(input("Ukuran Pakaian (s/m/l) :"))
            if(ukuran == "s"):
                harga = hargaKemeja
            elif(ukuran == "m"):
                harga = hargaKemeja + (hargaKemeja * 0.2)
            elif(ukuran == "l"):
                harga = hargaKemeja + (hargaKemeja * 0.4)


    #perintah output
    print("==========================================================")
    print("Barang yang dibeli :")
    print("1",jenis,bridge,bahan,"berukuran",ukuran)
    print("Harga:",harga)
    print("==========================================================")

    bayar = int(input("Uang yang dibayarkan: Rp."))
    kembalian = bayar - harga

    print("Kembalian: Rp.",kembalian)
    print("==========================================================")
    
    return 0
if __name__ == '__main__':
    main()

