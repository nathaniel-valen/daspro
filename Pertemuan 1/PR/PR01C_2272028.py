# File: PR01C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# menerima masukan nominal uang,
# lalu akan menampilkan jumlah
# lembaran paling sedikit yang merepresentasikan
# nominal dalam satuan rupiah.

# Kamus
# nominal = var input int
# sisa_sementara = var sisa nominal
# cepe,gocap, dst = var pecahan
# sisa = var total sisa nominal


# Program
def main():

    #Input,Proses,Output
    nominal = int(input("Nominal ="))
    print("menjadi pecahan :")
    cepe = nominal // 100000
    sisa_sementara = nominal % 100000
    print(cepe,"lembar uang seratus ribu")
    gocap = sisa_sementara // 50000
    sisa_sementara2 = sisa_sementara % 50000
    print(gocap,"lembar uang lima puluh ribu")
    noban = sisa_sementara2 // 20000
    sisa_sementara3 = sisa_sementara2 % 20000
    print(noban,"lembar uang dua puluh ribu")
    ceban = sisa_sementara3 // 10000
    sisa_sementara4 = sisa_sementara3 % 10000
    print(ceban,"lembar uang sepuluh ribu")
    goceng = sisa_sementara4 // 5000
    sisa_sementara5 = sisa_sementara4 % 5000
    print(goceng,"lembar uang lima ribu")
    noceng = sisa_sementara5 // 2000
    sisa_sementara6 = sisa_sementara4 % 2000
    print(noceng,"lembar uang dua ribu")
    ceceng = sisa_sementara6 // 1000
    sisa_sementara7 = sisa_sementara6 % 1000
    print(ceceng,"lembar uang seribu")
    gope_kecil = sisa_sementara7 // 500
    sisa_sementara8 = sisa_sementara7 % 500
    print(gope_kecil,"lembar uang lima ratus")
    nope_kecil = sisa_sementara8 // 200
    sisa_sementara9 = sisa_sementara7% 200
    print(nope_kecil,"lembar uang dua ratus")
    cepe_kecil = sisa_sementara9 // 100
    sisa_sementara10 = sisa_sementara9 % 100
    print(cepe_kecil,"lembar uang seratus")
    gocap_kecil = sisa_sementara10 // 50
    sisa = sisa_sementara10 & 50
    print(gocap_kecil,"lembar uang lima puluh")

if __name__ == '__main__':
    main()
