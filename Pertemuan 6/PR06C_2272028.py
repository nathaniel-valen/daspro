# File : PR06C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Tujuan Program : program yang akan menerima sebuah bil. bulat
# lalu menampilkan jajaran segitiga berukuran N sebanyak 2*N
# restoran yang disediakan. 
# Kamus Data :
# n : var input untuk loop bertipe integer
# i : var counter loop bertipe integer
# j : var counter loop bertipe integer
# k : var counter loop bertipe integer


def main():
   
    n = int(input("n :"))

    for i in range (n):
        for j in range(n):
            if (i % 2 == 0):
                for k in range(n):
                    print("*", end=" ")
            else:
                print("*", end=" ")
                for k in range(n-2):
                    print(" ", end=" ")
                print("*", end=" ")
            print(end=" ")
        print()
        
if __name__ == '__main__':
    main()