# File : PR07B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :

# Kamus Lokal :
# a = var parameter
# b = var parameter
def operatorTambah(a,b):
    print(a + b)

# Kamus Lokal :
# a = var parameter
# b = var parameter
def operatorKurang(a,b):
    print(a - b)

# Kamus Lokal :
# a = var parameter
# b = var parameter
def operatorKali(a,b):
    print(a * b)

# Kamus Lokal :
# a = var parameter
# b = var parameter
def operatorBagi(a,b):
    print(a / b)

# Kamus Lokal :
# a = var parameter
# b = var parameter
def operatorModulo(a,b):
    print(a % b)

# Kamus Lokal :
# a = var parameter
# b = var parameter
def operatorPangkat(a,b):
    print(a ** b)

# Kamus Lokal :
# a = var input integer
# b = var input integer
# c = var input string
# d = deklarasi var tukar tempat
def main():
    a = int(input("a :"))
    b = int(input("b :"))
    c = str(input("c (+, -, *, /, %, **) :"))
    d = 0
    
    if(a < b):
        d = a
        a = b
        b = d

    if(c == "+"):
        print("Perhitungan :")
        print(a, "+", b,"=",end=" "), operatorTambah(a,b)
    elif(c == "-"):
        print("Perhitungan :")
        print(a,"-", b,"=",end=" "), operatorKurang(a,b)
    elif(c == "*"):
        print("Perhitungan :")
        print(a,"*", b,"=",end=" "), operatorKali(a,b)
    elif(c == "/"):
        print("Perhitungan :")
        print(a,"/", b,"=",end=" "), operatorBagi(a,b)
    elif(c == "%"):
        print("Perhitungan :")
        print(a,"%", b,"=",end=" "), operatorModulo(a,b)
    elif(c == "**"):
        print("Perhitungan :")
        print(a,"**", b,"=",end=" "),operatorPangkat(a,b)
    else :
        print("Inputan Salah contoh (+, -, *, /, %, **)")
    
if __name__ == '__main__':
    main()