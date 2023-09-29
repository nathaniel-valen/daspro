# File : PR06B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program yang akan menerima masukan sebuah bilangan 
# lalu akan menampilkan deretan bilangan tersebut 
# dalam representasi persegi!
# Kamus Data
# n = var input angka (integer)
# i = var counter
# j = var counter
# num = var deklarasi untuk print angka

def main():
    num = 1
    n = int(input("n :"))

    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                if n > 3 :
                    print("{:02d}".format(num), end=" ")
                else :
                    print(num, end=" ")
                num += 1
            else:
                num -= 1
                if n > 3 :
                    print("{:02d}".format(num), end=" ")
                else :
                    print(num, end=" ")
        print()
        num += n
    return 0

if __name__ == '__main__':
    main()