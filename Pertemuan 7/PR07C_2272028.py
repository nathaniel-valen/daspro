# File : PR07C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# program yang akan meminta input bilangan,
# dimana program akan mengecek apakah bilangan palindrom,
# bilangan kuadrat, dan konversi ke angka biner.
# Ketiga perintah tadi akan diletakkan ke dalam fungsi
# seperti pada tabel di bawah.
# Program akan berhenti ketika user menginput angka 999
# dan bilangan yang diinput harus 0 < x < 129.


# Kamus Lokal :
# x = var parameter
# y = var hitung bagi integer
# z = var hitung modulo
def isPalindrom(x):
    if(100 <= x <= 129):
        y = x // 100
    else :
        y = x // 10

    z = x % 10

    if(y == z):
        print(x,"adalah bilangan palindrom")
    elif(x < 10):
        print(x,"adalah bilangan palindrom")
    else :
        print(x,"bukan bilangan palindrom")

# Kamus Lokal :
# x = var parameter
# i = var counter       
def isSquare(x):
    for i in range(1,12,1):
        if((i ** 2) == x):
            print(x,"bilangan kuadrat dengan akarnya adalah",i)
            break
    else :
        print(x,"bukan bilangan kuadrat")

# Kamus Lokal :
# x = var parameter
# binary = deklarasi var hitung biner
def convertBinary(x):
    binary = ""
    print("Angka biner dari",x,":")
    while(x > 0):
        binary = str(x % 2)+" " + binary
        x //= 2
    
    while(len(binary) % 8 != 0):
        binary = "0 " + binary

    print(binary, end=" ")
    print()    

# Kamus Lokal :
# x = var input integer
def main():
    x = int(input("N :"))
    while(x != 999):
        if(0 < x < 129):
            isPalindrom(x)
            isSquare(x)
            convertBinary(x)
        else :
            print("Angka harus 0 < x < 129")
        print("=" * 30)
        x = int(input("N :"))
    print("Program Selesai.")

    
if __name__ == '__main__':
    main()