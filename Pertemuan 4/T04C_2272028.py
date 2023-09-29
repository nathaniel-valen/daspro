# File : T04C_2272028.py
# Deskripsi :
# Program menerima sebuah bilangan bulat N
# program akan mengecek apakah
# bilangan tersebut adalah bilangan prima atau bukan. 
# Deret dimulai dari angka awal
# Kamus Data
# n = var input nilai (integer)

def main():
    # Perintah Input
    n = int(input("N :"))

    # Perintah Proses + Output
    for i in range (2,n) :
        if( n % i == 0):
            print("Bukan Prima")
            break
        else:
            print("Prima")
            break
    
if __name__ == '__main__':
    main()
