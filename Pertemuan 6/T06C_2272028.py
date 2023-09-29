# File : PR06C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program m yang akan terus meminta 
# bilangan sampai user memasukkan angka 999.
# Setiap angka yang dimasukkan akan di cek apakah bilangan tersebut 
# prima atau tidak seperti pada contoh program berikut.
# Kamus Data
# n = var input angka (integer)
# i = var counter

def main():
    n = int(input("Masukan angka : "))
    while (n != 999):
        if (n > 1):
            for i in range (2, n, 1):
                if (n % i == 0):
                    print (n, "bukan bilangan prima karena dapat dibagi dengan", i)
                    break
            else:
                print (n, "adalah bilangan prima")
        elif (n < 0):
            print (n, "bukan bilangan bulat positif")
        elif (n == 1 or n == 0):
            print (n, "bukan")     
        
        n = int(input("Masukan angka : "))

    print("Program Berhenti!")
    return 0
if __name__ == '__main__':
    main()