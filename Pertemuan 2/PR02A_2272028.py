# File : PR02A_2272028.py
# Deskripsi :
# Program yang akan menjalankan algoritma
# operator yang dapat diterima hanya +, -, *, dan /.
# Kamus Data
# a1 = var input bertipe int
# a2 = var input bertipe int
# a3 = var input bertipe int
# a4 = var input bertipe int
# o1 = var input bertipe str
# o2 = var input bertipe str
# hasilOp = var untuk menghitung operasi

def main():

    # perintah input
    a1 = int(input("angka1 :"))
    a2 = int(input("angka2 :"))
    a3 = int(input("angka3 :"))
    o1 = str(input("operasi1 :"))
    o2 = str(input("operasi2 :"))

    # perintah proses dan output
    if (o1 == "+") :
        if(o2 == "+"):
            hasilOp = (a1 + a2)+a3
        elif(o2 == "-"):
            hasilOp = (a1 + a2)-a3
        elif(o2 == "*"):
            hasilOp = (a1 + a2)*a3
        elif(o2 == "/"):
            hasilOp = (a1 + a2)/a3
        print("(",a1,o1,a2,")",o2,a3,"=",hasilOp)
    elif (o1 == "-") :
        if(o2 == "+"):
            hasilOp = (a1 - a2)+a3
        elif(o2 == "-"):
            hasilOp = (a1 - a2)-a3
        elif(o2 == "*"):
            hasilOp = (a1 - a2)*a3
        elif(o2 == "/"):
            hasilOp = (a1 - a2)/a3
        print("(",a1,o1,a2,")",o2,a3,"=",hasilOp)
    elif (o1 == "*") :
        if(o2 == "+"):
            hasilOp = (a1 * a2)+a3
        elif(o2 == "-"):
            hasilOp = (a1 * a2)-a3
        elif(o2 == "*"):
            hasilOp = (a1 * a2)*a3
        elif(o2 == "/"):
            hasilOp = (a1 * a2)/a3
        print("(",a1,o1,a2,")",o2,a3,"=",hasilOp)
    elif (o1 == "/") :
        if(o2 == "+"):
            hasilOp = (a1 / a2)+a3
        elif(o2 == "-"):
            hasilOp = (a1 / a2)-a3
        elif(o2 == "*"):
            hasilOp = (a1 / a2)*a3
        elif(o2 == "/"):
            hasilOp = (a1 / a2)/a3
        print("(",a1,o1,a2,")",o2,a3,"=",hasilOp)
    else :
        print("Salah Operasi Nich")
        
if __name__ == '__main__':
    main()

