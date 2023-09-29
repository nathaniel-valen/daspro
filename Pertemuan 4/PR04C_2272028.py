# File : PR04C_2272028.py
# Deskripsi :
# Program menerima sebuah bilangan bulat hingka nilai 9999
# lalu akan menampilkan apakah bilangan tersebut genap atau tidak.
# Kamus Data
# jauh = var deklarasi string kosong
# dekat = var deklarasi string kosong
# dekatJ = deklarasi var untuk hitung jarak terdekat
# jauhJ = deklarasi var untuk hitung jarak terjauh
# rute = var untuk hitung rute dan tujuan
# total = var untuk menghitung total perjalanan
# penumpang = var input berapa jumlah penumpang (integer)
# nama = var input nama (string)
# tujuan = var input tujuan (string)
# jarak = var input jarak (float)


def main():
    jauh = ""
    dekat = ""
    jauhJ = 0
    dekatJ = 9999
    rute = "| "
    total = 0
    penumpang = int(input("Jumlah Penumpang :"))
    for i in range(0,penumpang,1):
        print("====================================")
        nama = input("Nama :")
        tujuan = input("Tujuan :")
        jarak = float(input("Jarak tempuh (km) :"))
        rute = rute + tujuan + " | "
        total = total + jarak
        
        if( jarak < dekatJ):
            dekatJ = jarak
            dekat = tujuan
        if(jarak > jauhJ):
            jauhJ = jarak
            jauh = tujuan

    print("====================================")
    print("SUMMARY HARI INI")
    print("====================================")
    print("Total Customer :", penumpang)
    print("")
    print("Rute hari ini :")
    print(rute)
    print("====================================")
    print("Total jarak perjalanan hari ini :",round(total,2))
    print("Perjalanan dengan jarak terdekat :",dekatJ,"menuju",dekat)
    print("Perjalanan dengan jarak terjauh :",jauhJ,"menuju",jauh)
    
if __name__ == '__main__':
    main()
