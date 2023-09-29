# File : PR05B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah sebuah program yang akan 
# membentuk sebuah kalimat dari karakter yang diinput. 
# Ketika karakter yang diinput adalah "." program akan berhenti
# Kamus Data
# word = var kalimat untuk menampilkan seluruh karakter
# char = var input huruf bertipe (string)

def main():

    word = ""
    char = ""

    while char != ".":
        char = str(input("Karakter : "))
        word += char

    print("Hasil Kalimat :")
    print(word)

    
if __name__ == '__main__':
    main()