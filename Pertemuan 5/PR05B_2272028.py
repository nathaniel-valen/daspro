# File : PR05B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
#  program yang akan menerima sebuah bilangan bulat N 
# lalu akan menampilkan N simbol Nintendo. 
# Simbol tersebut ditampilkan secara terurut dari 
# segitiga, kotak, lingkaran, dan silang.
# Jika nilai N lebih besar dari 4
# Kamus Data
# n = var input nilai (integer)
# j = var deklarasi untuk urutan print

def main():

    n = int(input("n : "))
    j = 1

    while j <= n :
        if((j % 4) == 1):
            print("  *  ")
            print("* * *")
            print("     ")
        elif((j % 4) == 2):
            print("*    ")
            print("* *  ")
            print("*    ")
            print("     ")
        elif((j % 4) == 3):
            print("  *  ")
            print("* *  ")
            print("  *  ")
            print("     ")
        elif((j % 4) == 0):
            print("* * *")
            print("  *  ")
            print("     ")
    
        j += 1

    return 0

if __name__ == '__main__':
    main()