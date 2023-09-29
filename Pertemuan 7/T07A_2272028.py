# File : T07A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program yang akan menerima sebuah bilbul n 
# lalu akan menampilkan deret genap
# jika n tersebut genap dan akan menampilkan 
# deret ganjil jika N tersebut ganjil. 
# Pengecekan nilai n adalah ganjil atau genap 
# akan dilakukan pada fungsi main(). 
# Jika genap maka akan memanggil fungsi deretGanjil(),
# sedangkan jika n adalah ganjil akan memanggil deretGenap()

# Kamus Lokal
# i = var counter
# n = var parameter
def deretGanjil(n):
    for i in range(1,2*n,2):
        print(i, end=" ")

# Kamus Lokal
# i = var counter
# n = var parameter
def deretGenap(n):
    for i in range(2,2*n+1,2):
        print(i, end=" ")

# Kamus Lokal
# n = var input integer
def main():
    n = int(input("n :"))
    if(n % 2 == 0):
        deretGanjil(n)
    else :
        deretGenap(n)
if __name__ == '__main__':
    main()