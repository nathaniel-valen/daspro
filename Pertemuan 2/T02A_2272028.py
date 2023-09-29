# File : T02A_2272028.py
# Deskripsi :
# Program menghitung berapa nilai rupiah
# dalam beberapa mata uang neaga
# diantarnya euro,peso, dan won
# Kamus Data
# jumlah = var input bertipe int
# mata_uang = var input bertipe str
# euro = var untuk bagi jumlah dibagi harga euro bertipe int
# won = var untuk bagi jumlah dibagi harga won bertipe int
# peso = var untuk bagi jumlah dibagi harga peso bertipe int

def main():
    jumlah = int(input("Jumlah Rupiah : Rp"))
    mata_uang = str(input("Mata uang (Euro/Peso/Won) :"))
    print("=========================")
    
    if (mata_uang == "Euro"):
        euro = jumlah / 16205
        print (jumlah,"Rupiah sama dengan",round(euro,2),"Euro")
    elif (mata_uang == "Peso"):
        peso = jumlah / 257.84
        print (jumlah,"Rupiah sama dengan",round(peso,2),"Peso")
    elif (mata_uang == "Won"):
        won = jumlah / 11.69
        print (jumlah,"Rupiah sama dengan",round(won,2),"Won")
    else:
        print ("Mohon maaf mata uang",mata_uang,"tidak dikenali")
        return 0
if __name__ == '__main__':
    main()

