# File : T08B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang dapat menerima
# lima bilangan dan mencari nilai terbesar diantaranya.
# Anda harus membuat fungsi “terbesar(a,b,c,d,e)”
# untuk mengakomodasi kebutuhan terkait.

# Kamus Lokal
# a = var angka pertama
# b = var angka kedua
# c = var angka ketiga
# d = var angka keempat
# e = var angka kelima
def terbesar(a, b, c, d, e):
    if a >= b and a >= c and a >= d and a >= e:
        return a
    elif b >= a and b >= c and b >= d and b >= e:
        return b
    elif c >= a and c >= b and c >= d and c >= e:
        return c
    elif d >= a and d >= b and d >= c and d >= e:
        return d
    else:
        return e

# Kamus Lokal
# bil_one = var input bilangan pertama
# bil_two = var input bilangan kedua
# bil_three = var input bilangan ketiga
# bil_four = var input bilangan keempat
# bil_five = var input bilangan kelima
# res = var untuk hasil

def main():
    bil_one = int(input("a :"))
    bil_two = int(input("b :"))
    bil_three = int(input("c :"))
    bil_four = int(input("d :"))
    bil_five = int(input("e :"))

    res = terbesar(bil_one, bil_two, bil_three, bil_four, bil_five)
    print("Bilangan terbesar: ", res)

if __name__ == '__main__':
    main()