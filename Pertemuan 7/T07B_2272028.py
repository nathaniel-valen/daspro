# File : T07B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program yang akan menerima masukan sebuah bilangan bulat
# lalu akan menampilkan table factorial dimulai dari 1 sampai a.

# Kamus Lokal :
# a = var parameter
# fact = var untuk menghitung jumlah faktorial
# count = var untuk menghitung urutan
# x = var counter
def myFaktorial(a):
    fact = 1
    count = a 
    for x in range(1,a+1,1):
        fact = fact * x

    for x in range(1,a+1,1):
        print("| ",count, "! | | ",fact,"           |")
        fact //= count
        count -= 1

# Kamus Lokal
# a = var input integer
def main():
    a = int(input("a :"))
    print("|  a   | | nilai faktorial |")
    myFaktorial(a)

if __name__ == '__main__':
    main()