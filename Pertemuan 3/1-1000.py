def main():
    number = int(input("Angka :"))
    if number == 0:
        print("nol")
    elif number == 10:
        print("sepuluh")
    elif number == 11:
        print("sebelas")
    elif number == 12:
        print("dua belas")
    elif number == 13:
        print("tiga belas")
    elif number == 14:
        print("empat belas")
    elif number == 15:
        print("lima belas")
    elif number == 16:
        print("enam belas")
    elif number == 17:
        print("tujuh belas")
    elif number == 18:
        print("delapan belas")
    elif number == 19:
        print("sembilan belas")
    elif number == 1000:
        print("seribu")
    elif number == 10000:
        print("sepuluh ribu")
    else:
        words = ""

        #konversi ribuan
        if number >= 1000:
            if number // 1000 == 2:
                words += "dua ribu "
            elif number // 1000 == 3:
                words += "tiga ribu "
            elif number // 1000 == 4:
                words += "empat ribu "
            elif number // 1000 == 5:
                words += "lima ribu "
            elif number // 1000 == 6:
                words += "enam ribu "
            elif number // 1000 == 7:
                words += "tujuh ribu "
            elif number // 1000 == 8:
                words += "delapan ribu "
            elif number // 1000 == 9:
                words += "sembilan ribu "
            number %= 1000
        # konversi ratusan
        if number >= 100:
            if number // 100 == 1:
                words += "seratus "
            elif number // 100 == 2:
                words += "dua ratus "
            elif number // 100 == 3:
                words += "tiga ratus "
            elif number // 100 == 4:
                words += "empat ratus "
            elif number // 100 == 5:
                words += "lima ratus "
            elif number // 100 == 6:
                words += "enam ratus "
            elif number // 100 == 7:
                words += "tujuh ratus "
            elif number // 100 == 8:
                words += "delapan ratus "
            elif number // 100 == 9:
                words += "sembilan "
            number %= 100
        
        # konversi puluhan
        if number >= 20:
            if number // 10 == 2:
                words += "dua puluh "
            elif number // 10 == 3:
                words += "tiga puluh "
            elif number // 10 == 4:
                words += "empat puluh "
            elif number // 10 == 5:
                words += "lima puluh "
            elif number // 10 == 6:
                words += "enam puluh "
            elif number // 10 == 7:
                words += "tujuh puluh "
            elif number // 10 == 8:
                words += "delapan puluh "
            elif number // 10 == 9:
                words += "sembilan puluh "
            number %= 10
        
        # konversi satuan
        if number == 1:
            words += "satu"
        elif number == 2:
            words += "dua"
        elif number == 3:
            words += "tiga"
        elif number == 4:
            words += "empat"
        elif number == 5:
            words += "lima"
        elif number == 6:
            words += "enam"
        elif number == 7:
            words += "tujuh"
        elif number == 8:
            words += "delapan"
        elif number == 9:
            words += "sembilan"

        print("Hasil Konversi:")
        print(words)
main()
