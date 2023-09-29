# File : PR04A_2272028.py
# Deskripsi :
# Program yang akan menampilkan deret m angka dimulai dari n
# dengan kelipatan x
# Kamus Data
# n = var input angka (integer)
# m = var input angka (integer)
# x = var input angka (integer)
# total = deklarasi variabel total
# bil = var untuk menhitung deret angka
# rata = var untuk menghitung rata-rata

def main():

    # Perintah Input
    n = int(input("n :"))
    m = int(input("m : "))    
    x = int(input("x : "))

    total = 0

    print("Deret",m,"angka, dimulai dari",n,"dengan kelipatan",x)

    # Perintah Proses
    for i in range(m):
        if(i != m - 1):
            bil = n + i * x
            print(bil, end=", ")
            total += bil
        else :
            bil = n + i * x
            print(bil)
            total += bil
    
    rata = total / m

    # Perintah Output
    print("Total seluruh deret adalah", total)
    print("Rata-rata deret adalah",rata)

if __name__ == '__main__':
    main()
