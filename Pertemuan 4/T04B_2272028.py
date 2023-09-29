# File : T04B_2272028.py
# Deskripsi :
# Program menghitung jumlah deret dari input yang diberikan.
# Deret dimulai dari angka awal
# Kamus Data
# hit = deklarasi variabel untuk hitungan
# jDeret = deklarasi variabel untuk jumlah deret
# hasilString = deklarasi variabel untuk string hasil
# jS = var untuk jumlah suku (integer)
# awal = var untuk awal (integer)
# inc = var untuk increment (integer)
# oP = var untuk operasi (string)

def main():
    # Deklarasi Variable
    hit = 0
    jDeret = 0

    # Perintah Input
    jS = int(input("Jumlah Suku :"))
    awal = int(input("Awal :"))
    inc = int(input("Increment :"))
    oP = input("Operasi :")
    print("Deret :")

    # Perintah Proses
    if(oP == "+" or oP == "*" or oP == "/" or oP == "-"):
        jDeret = awal
        print(awal,oP,end=" ")
    for i in range (jS - 1) :
        if(oP == "+"):
            if(hit < jS - 2):
                awal = awal + inc
                jDeret = jDeret + awal
                print(awal,oP,end=" ")
            else :
                awal = awal + inc
                jDeret = jDeret + awal
                print(awal)
            hit = hit + 1
            hasilString = "Jumlah Deret :"
            
        elif(oP == "-"):
            if(hit < jS - 2):
                awal = awal + inc
                jDeret = jDeret - awal
                print(awal,oP,end=" ")
            else :
                awal = awal + inc
                jDeret = jDeret - awal
                print(awal)
            hit = hit + 1
            hasilString = "Hasil Kurang Deret :"
        
        elif(oP == "*"):
            if(hit < jS - 2):
                awal = awal + inc
                jDeret = jDeret * awal
                print(awal,oP,end=" ")
            else :
                awal = awal + inc
                jDeret = jDeret * awal
                print(awal)
            hit = hit + 1
            hasilString = "Hasil Kali Deret :"
        
        elif(oP == "/"):
            if(hit < jS - 2):
                awal = awal + inc
                jDeret = jDeret / awal
                print(awal,oP,end=" ")
            else :
                awal = awal + inc
                jDeret = jDeret / awal
                print(awal)
            hit = hit + 1
            hasilString = "Hasil Bagi Deret :"

    # Perintah Output
    print(hasilString, jDeret)
    
    return 0

    
if __name__ == '__main__':
    main()
