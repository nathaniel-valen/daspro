# File : PR03A_2272028.py
# Deskripsi :
# Program  yang akan menentukan posisi dari
# sebuah titik terhadap titik acuan. 
# Kamus Data
# x1 = var input bertipe int
# y1 = var input bertipe int
# x2 = var input bertipe int
# y2 = var input bertipe int


def main():

    # Perintah Input
    x1 = int(input("titik acuan x :"))
    y1 = int(input("titik acuan y :"))
    x2 = int(input("titik x :"))
    y2 = int(input("titik y :"))

    # Perintah Proses dan Output
    if (x2 > x1) :
        if (y2 > y1) :
            print("titik (",x2,",",y2,") terletak disebelah kanan atas titik acuan (",x1,",",y1,")")
        elif (y2 < y1) :
            print("titik (",x2,",",y2,") terletak disebelah kanan bawah titik acuan (",x1,",",y1,")")
        else :
            print("titik (",x2,",",y2,") terletak disebelah kanan titik acuan (",x1,",",y1,")")

    elif (x2 < x1) :
        if (y2 > y1) :
            print("titik (",x2,",",y2,") terletak disebelah kiri atas titik acuan (",x1,",",y1,")")
        elif (y2 < y1) :
            print("titik (",x2,",",y2,") terletak disebelah kiri bawah titik acuan (",x1,",",y1,")")
        else :
            print("titik (",x2,",",y2,") terletak disebelah kiri titik acuan (",x1,",",y1,")")        

    else :
        if (y2 > y1) :
            print("titik (",x2,",",y2,") terletak disebelah atas titik acuan (",x1,",",y1,")")
        elif (y2 < y1) :
            print("titik (",x2,",",y2,") terletak disebelah bawah titik acuan (",x1,",",y1,")")
        else :
            print("titik (",x2,",",y2,") memiliki posisi yang sama dengan titik acuan (",x1,",",y1,")")
if __name__ == '__main__':
    main()

