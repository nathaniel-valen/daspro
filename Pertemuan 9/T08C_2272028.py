# File : T08C_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# BBuatlah sebuah program untuk menghitung
# biaya sewa warnet KUY berdasarkan
# jumlah menit yang dimasukkan.

# Kamus Lokal
# h = var untuk jam
# min = var untuk menit
def menitKeJam(min):
    h = min // 60
    return h

# Kamus Lokal
# s = var untuk sisa
# min = var untuk menit
def sisaMenit(min):
    s = min % 60
    return s

# Kamus Lokal
# pay = var untuk tagihan
# min = var untuk menit
# h = var untuk jam
# disc = var untuk diskon
def totalTagihan(min, h):
    pay = 7000
    pay += (h - 1) * 6000
    disc = ((h - 1) // 3 * 500) * 3
    pay -= disc
    pay += sisaMenit(min) * 125
    return pay
# Kamus Lokal
# bal = var input untuk saldo (int)
# loan_min = var input untuk menit sewa (int)
# loan_h = var untuk jam menghitung menit ke jam
# pay = var untuk tagihan
# s_bal = var untuk sisa saldo
# min_pay = var untuk kekurangan bayar
def main():
    print("========= WARNET KUY =========")
    bal = int(input("Jumlah saldo: "))
    loan_min = int(input("Durasi sewa (menit): "))

    loan_h = menitKeJam(loan_min)
    pay = totalTagihan(loan_min, loan_h)

    print("==============================")
    print("Total Sewa", loan_h, "jam", sisaMenit(loan_min), "menit")
    print("Jumlah Tagihan:", pay)
    print("==============================")

    if bal >= pay:
        print("!!! LUNAS !!!")
        s_bal = bal - pay
        print("Sisa Saldo:", s_bal)
    else:
        min_pay = pay - bal
        print("Kekurangan pembayaran:", min_pay)
        print("Mohon lakukan isi ulang kepada admin!")

if __name__ == '__main__':
    main()