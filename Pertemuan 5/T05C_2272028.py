# File : PR05C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah sebuah program  menampilkan hasil 
# pertambahan waktu dalam bentuk jam, menit dan detik
# Program akan berhenti apabila user memasukan jenis waktu ‘4’.
# Kamus Data
# sec = var input detik (integer)
# min = var input menit (integer)
# hour = var input jam (integer)
# pil = var untuk pilihan jenis waktu yang mau ditambahkan
# sec2 = var untuk deklarasi pertambahan detik
# min2 = var untuk deklarasi pertambahan menit
# hour2 = var untuk deklarasi pertambahan jam

def main():

    sec = int(input("detik: "))
    min = int(input("menit: "))
    hour = int(input("jam: "))

    while True:
        print("Waktu sekarang:")
        print("{:02d} : {:02d} : {:02d}".format(hour, min, sec))

        pil = int(input("Jenis waktu yang ingin ditambahkan(1.Detik 2. Menit 3. Jam 4. Exit): "))

        if (pil == 1):
            sec2 = int(input("detik: "))
            sec += sec2
            if sec >= 60:
                min += sec // 60
                sec %= 60
            if min >= 60:
                hour += min // 60
                min %= 60
            hour %= 24

        elif (pil == 2):
            min2 = int(input("menit: "))
            min += min2
            if min >= 60:
                hour += min // 60
                min %= 60
            hour %= 24

        elif (pil == 3):
            hour2 = int(input("jam: "))
            hour += hour2
            hour %= 24

        elif (pil == 4):
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

    print("Hasil perjumlahan:")
    print("{:02d} : {:02d} : {:02d}".format(hour, min, sec))


    
if __name__ == '__main__':
    main()