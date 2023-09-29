# File: PR01B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# program yang menjalankan algoritma :
# Menginput var panjang (p)
# Menginput var lebar (l)
# Menginput var tinggi (t)
# Menampilkan keliling dengan rumus:
# 4(p + l + t)
# Menampilkan luas dengan rumus :
# 2(p x l + p x t + p x t)
# Menampilkan volume dengan rumus:
# p x l x t

# Kamus
# p untuk var panjang
# l untuk var lebar
# t untuk var tinggi
# keliling untuk var rumus
# luas untuk var rumus
# volume untuk var rumus


# Program
def main():

    #Input
    p = int(input("Panjang (cm) :"))
    l = int(input("Lebar (cm) :"))
    t = int(input("Tinggi (cm) :"))

    #Proses
    #Rumus1
    keliling = 4*(p + l + t)
    #Rumus2
    luas = 2*((p * l) + (p * t) + (l * t))
    #Rumus3
    volume = p * l * t

    #Output
    print("Keliling =",keliling,"cm")
    print("Luas =",luas,"cm^2")
    print("Volume =",volume,"cm^3")

if __name__ == '__main__':
    main()
