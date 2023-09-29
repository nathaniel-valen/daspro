# File : T03B_2272028.py
# Deskripsi :
# Program yang akan mengubah input detik menjadi
# jam menit detik
# dan menampilkan hasil pertambahan waktu dalam bentuk
# jam, menit dan detik.
# Kamus Data
# sec = var input detik bersifat int
# min = deklarasi untuk menit
# hour = deklarasi untuk jam
# now = menentukan waktu sekarang
# type = var input jenis waktu bersifat int
# plus = deklarasi untuk penjumlahan waktu

def main():
    # Perintah input    
    sec = int(input("detik :"))
    min = 0
    hour = 0

    # Perintah Proses
    hour = sec // 3600
    min = (sec % 3600) // 60
    sec = (sec % 3600) % 60

    # Perintah Output
    print("Waktu Sekarang :")
    now = print("{:02d} : {:02d} : {:02d}". format(hour,min,sec))

    # Perintah input 
    type = int(input("Jenis waktu yang ingin ditambahkan(1.detik 2.menit 3.jam) :"))

    # Perintah Proses
    if type == 1:
        plus = int(input("Detik :"))
        sec += plus
        if (sec >= 60):
            min += (sec // 60)
            sec = sec % 60
            if ( min >= 60) :
                hour += (min //60)
                min = min % 60
                if (hour >= 24) :
                    hour = hour % 24
    elif type == 2:
        plus =int(input("Menit :"))
        min += plus
        if ( min >= 60) :
            hour += (min //60)
            min = min %60
            if (hour >= 24) :
                hour = hour % 24    
    elif type == 3:
        plus = int(input("Jam :"))
        hour += plus
        if (hour >= 24) :
                    hour = hour % 24
    
    # Perintah Output    
    print("{:02d} : {:02d} : {:02d}". format(hour,min,sec))
    
if __name__ == '__main__':
    main()

