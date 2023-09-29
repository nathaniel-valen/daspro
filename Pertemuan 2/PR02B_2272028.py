# File : PR02B_2272028.py
# Deskripsi :
# Program yang akan menghitung total buah
# total harga buah berdasarkan input user
# harga alpukat = 40.000
# harga apel = 35.000
# harga jeruk = 20.000.
# Kamus Data
# a1 = var input bertipe int
# a2 = var input bertipe int
# a3 = var input bertipe int
# a4 = var input bertipe int
# o1 = var input bertipe str
# o2 = var input bertipe str
# hasilOp = var untuk menghitung operasi

def main():

    # berat awal buah
    berat_alpukat = 0
    berat_apel = 0
    berat_jeruk = 0

    # perintah input
    buah = str(input("Buah(Alpukat/Apel/Jeruk) :"))

    # perintah proses
    if (buah == "Alpukat") :
        jmlAlpukat = int(input("Jumlah Alpukat (kg) :"))
        berat_alpukat = berat_alpukat+jmlAlpukat
    elif (buah == "Apel") :
        jmlApel = int(input("Jumlah Apel (kg) :"))
        berat_apel= berat_apel+jmlApel
    elif (buah == "Jeruk") :
        jmlJeruk = int(input("Jumlah Jeruk (kg) :"))
        berat_jeruk = berat_jeruk+jmlJeruk
    print("=========================")
    buah = str(input("Buah(Alpukat/Apel/Jeruk) :"))
    if (buah == "Alpukat") :
        jmlAlpukat = int(input("Jumlah Alpukat (kg) :"))
        berat_alpukat = berat_alpukat+jmlAlpukat
    elif (buah == "Apel") :
        jmlApel = int(input("Jumlah Apel (kg) :"))
        berat_apel= berat_apel+jmlApel
    elif (buah == "Jeruk") :
        jmlJeruk = int(input("Jumlah Jeruk (kg) :"))
        berat_jeruk = berat_jeruk+jmlJeruk
    print("=========================")
    buah = str(input("Buah(Alpukat/Apel/Jeruk) :"))
    if (buah == "Alpukat") :
        jmlAlpukat = int(input("Jumlah Alpukat (kg) :"))
        berat_alpukat = berat_alpukat+jmlAlpukat
    elif (buah == "Apel") :
        jmlApel = int(input("Jumlah Apel (kg) :"))
        berat_apel= berat_apel+jmlApel
    elif (buah == "Jeruk") :
        jmlJeruk = int(input("Jumlah Jeruk (kg) :"))
        berat_jeruk = berat_jeruk+jmlJeruk
    print("=========================")

    totalBerat = berat_alpukat+berat_apel+berat_jeruk
    totalHarga = (berat_alpukat*40000)+(berat_apel*35000)+(berat_jeruk*20000)

    # perintah output
    print("Jumlah Buah Alpukat :",berat_alpukat,"Kg")
    print("Jumlah Buah Apel :",berat_apel,"Kg")
    print("Jumlah Buah Jeruk :",berat_jeruk,"Kg")
    print("Total Jumlah Buah yaitu :",totalBerat,"Kg")
    print("Total Harga Buah Rp",totalHarga)
        
    return 0
        
if __name__ == '__main__':
    main()

