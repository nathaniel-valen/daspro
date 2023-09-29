# File : T02C_2272028.py
# Deskripsi :
# Program mengkonversi angka menjadi kata.
# Kamus Data
# angka = var input bertipe int
# d = var bagi int untuk mencari angka depan
# b = var modular untuk mencari angka belakang
# end = agar syntax print menjadi kesamping


def main():
    angka = int(input("Input Angka dari 1 - 100 :"))

    if( angka == 1):        
        print("satu")
    elif( angka == 2):        
        print("dua")
    elif( angka == 3):        
        print("tiga")
    elif( angka == 4):        
        print("empat")
    elif( angka == 5):        
        print("lima")
    elif( angka == 6):        
        print("enam")
    elif( angka == 7):        
        print("tujuh")
    elif( angka == 8):        
        print("delapan")
    elif( angka == 9):        
        print("sembilan")
    elif( angka == 10):        
        print("sepuluh")
    elif( angka == 11):        
        print("sebelas")
    elif( angka == 12):        
        print("dua belas")
    elif( angka == 13):        
        print("tiga belas")
    elif( angka == 14):        
        print("empat belas")
    elif( angka == 15):        
        print("lima belas")
    elif( angka == 16):        
        print("enam belas")
    elif( angka == 17):        
        print("tujuh belas")
    elif( angka == 18):        
        print("delapan belas")
    elif( angka == 19):        
        print("sembilan belas")
    elif( angka == 20):        
        print("dua puluh")
    elif( angka == 100):
        print("seratus")
    elif (angka > 20 ):
        d = angka // 10
        b = angka % 10
        if ( d == 1 ):
            print("satu", end=" ")
        elif ( d == 2 ):
            print("dua", end=" ")
        elif ( d == 3 ):
            print("tiga", end=" ")
        elif ( d == 4 ):
            print("empat", end=" ")
        elif ( d == 5 ):
            print("lima", end=" ")
        elif ( d == 6 ):
            print("enam", end=" ")
        elif ( d == 7 ):
            print("tujuh", end=" ")
        elif ( d == 8 ):
            print("delapan", end=" ")
        elif ( d == 9 ):
            print("sembilan", end=" ")
        print("puluh", end=" ")
        if ( b == 1 ):
            print("satu", end=" ")
        elif ( b == 2 ):
            print("dua", end=" ")
        elif ( b == 3 ):
            print("tiga", end=" ")
        elif ( b == 4 ):
            print("empat", end=" ")
        elif ( b == 5 ):
            print("lima", end=" ")
        elif ( b == 6 ):
            print("enam", end=" ")
        elif ( b == 7 ):
            print("tujuh", end=" ")
        elif ( b == 8 ):
            print("delapan", end=" ")
        elif ( b == 9 ):
            print("sembilan", end=" ")  
    elif (angka > 100 ):
        d = angka // 10
        b = angka % 10
        if ( d == 1 ):
            print("satu", end=" ")
        elif ( d == 2 ):
            print("dua", end=" ")
        elif ( d == 3 ):
            print("tiga", end=" ")
        elif ( d == 4 ):
            print("empat", end=" ")
        elif ( d == 5 ):
            print("lima", end=" ")
        elif ( d == 6 ):
            print("enam", end=" ")
        elif ( d == 7 ):
            print("tujuh", end=" ")
        elif ( d == 8 ):
            print("delapan", end=" ")
        elif ( d == 9 ):
            print("sembilan", end=" ")
        print("ratus", end=" ")
        if ( b == 1 ):
            print("satu", end=" ")
        elif ( b == 2 ):
            print("dua", end=" ")
        elif ( b == 3 ):
            print("tiga", end=" ")
        elif ( b == 4 ):
            print("empat", end=" ")
        elif ( b == 5 ):
            print("lima", end=" ")
        elif ( b == 6 ):
            print("enam", end=" ")
        elif ( b == 7 ):
            print("tujuh", end=" ")
        elif ( b == 8 ):
            print("delapan", end=" ")
        elif ( b == 9 ):
            print("sembilan", end=" ")  
if __name__ == '__main__':
    main()

