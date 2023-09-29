# File : PR13A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi
# Buatlah program yang akan menerima masukan N
# buah bilangan lalu akan menampilkan N bilangan
# tersebut secara terurut menurun. 
# Kamus Data
# N = var input panjang array
# Arr = var deklarasi array kosong sepanjang N
# num = var agar print tidak didalam array
def main():
    N = int(input("N : "))
    Arr = [0] * N

    for i in range(N):
        Arr[i] = int(input("Masukkan bilangan ke-{}: ".format(i+1)))

    # Mengurutkan bilangan secara menurun
    for i in range(N):
        for j in range(i+1, N):
            if Arr[i] > Arr[j]:
                Arr[i], Arr[j] = Arr[j], Arr[i]

    print("Bilangan terurut menurun:")
    for num in Arr:
        print(num, end=" ")

if __name__ == '__main__':
    main()
