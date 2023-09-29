# File : T07C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program yang akan menerima sebuah bilangan bulat N 
# lalu akan menampilkan simbol diamond berukuran N*2 + 1.

# Kamus Lokal
# n = var parameter
# i = var counter
# j = var counter
# k = var counter
def diamondAtas(n):
    for i in range(0,n,1):
        for j in range(n-i,0,-1):
             print(" ",end=" ")
        for k in range(0,i*2+1,1):
             print("+", end=" ")
        print()

# Kamus Lokal
# n = var parameter
# i = var counter
def diamondTengah(n):
    for i in range(0,n*2+1,1):
        print("+", end=" ")
    print()

# Kamus Lokal
# n = var parameter
# jump = var pengurangan (+)
# i = var counter
# j = var counter
# k = var counter
def diamondBawah(n):
    jump = n*2-1
    for i in range(1,n+1,1):
        for j in range(0,i,1):
            print(" ",end=" ")
        for k in range(0,jump,1):
            print("+", end=" ")
        jump -= 2
        print()

# Kamus Lokal
# n = var input integer dan parameter function
def main():
    n = int(input("n :"))
    diamondAtas(n)
    diamondTengah(n)
    diamondBawah(n)

if __name__ == '__main__':
    main()