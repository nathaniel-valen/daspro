# File : PR10C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program yang akan menerima masukan N
# buah bilangan dan M buah bilangan lalu akan
# menampilkan gabungan dari kedua himpunan bilangan tersebut.
# Asumsikan bilangan tidak selalu unik,
# namun hasil gabungan harus unik.
# Kamus Data
# N = var input untuk berapa banyak array (int)
# M = var input untuk berapa banyak array (int)
# arrN = var bilangan menghitung array
# arrM = var bilangan menghitung array
# temp = var unutk menampung hasil dari N dan M
# penampung = var deklarasi counter
# bulean = var check angka sama atau tidak

def main():
    N = int(input("N :"))
    arrN = [None] * N
    
    for i in range(N):
        arrN[i] = int(input("Input 1 :"))
    
    M = int(input("M :"))
    arrM = [None] * M

    for i in range(M):
        arrM[i] = int(input("Input 2 :"))

    temp = [None] * (N + M)
    penampung = 0
    bulean = 'true'
    for j in range(N):
        for k in range(N):
            if(arrN[j] == temp[k]):
                bulean = 'false'
        if bulean == 'true':
            temp[penampung] = arrN[j]
            penampung += 1
        bulean = 'true'
    
    for j in range(M):
        for k in range(M):
            if(arrM[j] == temp[k]):
                bulean = 'false'
        if bulean == 'true':
            temp[penampung] = arrM[j]
            penampung += 1
        bulean = 'true'
    
    for i in range(0,N+M,1):
        if temp[i] != None:
            print(temp[i], end=" ")



if __name__ == '__main__':
    main()