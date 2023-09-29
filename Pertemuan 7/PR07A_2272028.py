# File : PR07A_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# yang akan menampilkan urutan abjad hingga huruf e
# dan mengulang lagi dari a sesuai dengan bilangan
# yang kita input secara berulang.

# Kamus Lokal :
# x = var parameter
# i = var counter
def alphabetCount(x):
    for i in range(x):
        if(i % 5) == 0:
            print("a", end=" ")
        elif(i % 5) == 1:
            print("b", end=" ")
        elif(i % 5) == 2:
            print("c", end=" ")
        elif(i % 5) == 3:
            print("d", end=" ")
        elif(i % 5) == 4:
            print("e", end=" ")
    print()

# Kamus Lokal :
# x = var input integer
def main():
    x = int(input("x :"))
    while(x != 0):
        alphabetCount(x)
        x = int(input("x :"))
    print("Program Selesai.")
    
if __name__ == '__main__':
    main()