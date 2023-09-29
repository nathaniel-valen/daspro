# File : PR05A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah sebuah program yang akan 
# membentuk sebuah kalimat dari karakter yang diinput. 
# Ketika karakter yang diinput adalah "." program akan berhenti
# Program akan menghitung berapa huruf vocal yang dimasukan.
# Kamus Data
# word = var kalimat untuk menampilkan seluruh karakter
# char = var input huruf bertipe (string)
# vokal = deklarasi var "aiueoAIUEO"
# hit_a = var untuk hitung huruf a
# hit_i = var untuk hitung huruf i
# hit_u = var untuk hitung huruf u
# hit_e = var untuk hitung huruf e
# hit_o = var untuk hitung huruf o

def main():

    vokal = "aiueoAIUEO"
    word = ""
    hit_a = 0
    hit_i = 0
    hit_u = 0
    hit_e = 0
    hit_o = 0

    while True:
        char = input("Huruf :")
        if char == ".":
            break
        word += char
        if char in vokal:
            if char == "a" or char == "A":
                hit_a += 1
            elif char == "i" or char == "I":
                hit_i += 1
            elif char == "u" or char == "U":
                hit_u += 1
            elif char == "e" or char == "E":
                hit_e += 1
            elif char == "o" or char == "O":
                hit_o += 1

    print("Hasil Kalimat:")
    print(word)
    print("Huruf a =", hit_a)
    print("Huruf i =", hit_i)
    print("Huruf u =", hit_u)
    print("Huruf e =", hit_e)
    print("Huruf o =", hit_o)


    
if __name__ == '__main__':
    main()