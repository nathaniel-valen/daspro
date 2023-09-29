# File : PR06A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Tujuan Program : program untuk membuat gambar hati 
# dengan panjang dan lebar sebnayak 2*n yang diinput
# Kamus Data :
# n : var input n bertipe int
# i : var counter loop bertipe int
# j : var counter loop bertipe int
# k : var counter loop bertipe int
# x : var counter loop bertipe

def main():
 
    n = int(input("n :"))

    s_atas = (n + 1) // 2

    # Segitiga Atas
    for i in range (0,s_atas,1):
        for x in range(0,2,1):
            for j in range (0,(s_atas)-i-1,1):
                print(" ", end=" ")
            for k in range (0,2*i+1,1):
                print("*", end=" ")
            for j in range (0,(s_atas)-i-1,1):
                print(" ", end=" ")
        print()

    # Segitiga Bawah   
    for i in range (0,n,1):
        for j in range (0,i,1):
            print(" ", end=" ")
        for k in range (0,(n-i)*2,1):
            print("*", end=" ")
        print()
        
if __name__ == '__main__':
    main()