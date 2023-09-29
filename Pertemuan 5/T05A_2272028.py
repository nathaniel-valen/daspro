# File : PR05A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Program yang akan menerima masukan sampai input yang dimasukan 9999
# kemudian program akanmenampilkan 
# jumlah, total serta rata-rata dari angka yang diinput.
# Kamus Data
# n = var input angka untuk diulang (integer)
# total = var untuk menghitung total
# count = var untuk menghitung jumlah baris
# rata_rata = var untuk menghitung rata-rata

def main():

    total = 0
    count = 0
    n = 0

    while n != 9999:
        n = int(input("n: "))
        if n != 9999:
            total += int(n)
            count += 1

        avg = total / count

    print("Jumlah Angka :", count)
    print("Total Angka :", total)
    print("Rata-Rata :", avg)


    
if __name__ == '__main__':
    main()
