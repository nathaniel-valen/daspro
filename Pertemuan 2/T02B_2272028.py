# File : T02B_2272028.py
# Deskripsi :
# Program membantu menanam tanaman pada petak ladang
# jenis tanaman yang ingin ditanam
# yaitu :
# turnip, cabbage, cucumber
# Kamus Data
# awal_petak = var bersifat integer
# jenis = var bersifat integer
# tot_turnip = var bersifat integer
# tot_cucumber = var bersifat integer
# tot_cabbage = var bersifat integer
# turnip = var jumlah awal dan total jumlah turnip
# cucumber = var jumlah awal dan total jumlah cucumber
# cabbage = var jumlah awal dan total jumlah cabbage
# petak_turnip = var untuk petak yang dibutuhkan turnip
# petak_cabbage = var untuk petak yang dibutuhkan cabbage
# petak_cucumber = var untuk petak yang dibutuhkan cucumber

def main():
    pet_turnip = 0
    petak_cabbage = 0
    petak_cucumber = 0
    turnip = 0
    cabbage = 0
    cucumber = 0
    
    awal_petak = int(input("Jumlah Petak : "))

    print("====== Penanaman ke-1 =======")
    jenis = int(input("Jenis : "))
    
    if (jenis == "1"):
        tot_turnip = input("Jumlah Turnip :")
        turnip = tot_turnip + turnip
    elif (jenis == "2"):
        tot_cabbage = int(input("Jumlah Cabbage :"))
        cabbage = tot_cabbage + cabbage
    elif (jenis == "3"):
        tot_cucumber = int(input("Jumlah Cucumber :"))
        cucumber = tot_cucumber + cucumber

    print("====== Penanaman ke-2 =======")
    jenis = input("Jenis : ")
    
    if (jenis == "1"):
        tot_turnip = int(input("Jumlah Turnip :"))
        turnip = tot_turnip + turnip
    elif (jenis == "2"):
        tot_cabbage = int(input("Jumlah Cabbage :"))
        cabbage = tot_cabbage + cabbage
    elif (jenis == "3"):
        tot_cucumber = int(input("Jumlah Cucumber :"))
        cucumber = tot_cucumber + cucumber

    print("====== Penanaman ke-3 =======")
    jenis = input("Jenis : ")
    
    if (jenis == "1"):
        tot_turnip = int(input("Jumlah Turnip :"))
        turnip = tot_turnip + turnip
    elif (jenis == "2"):
        tot_cabbage = int(input("Jumlah Cabbage :"))
        cabbage = tot_cabbage + cabbage
    elif (jenis == "3"):
        tot_cucumber = int(input("Jumlah Cucumber :"))
        cucumber = tot_cucumber + cucumber

    petak_turnip = turnip * 1
    petak_cucumber = cucumber * 2
    petak_cabbage = cabbage * 3

    keseluruhan = petak_turnip + petak_cucumber + petak_cabbage
    total_petak = awal_petak - keseluruhan

    print("======= Total Penanaman =======")
    print(turnip,"Turnip pada",petak_turnip,"petak")
    print(cucumber,"Cucumber pada",petak_cucumber,"petak")
    print(cabbage,"Cabbage pada",petak_cabbage,"petak")
    print("Total",keseluruhan,"tersisa",total_petak,"petak")
    return 0       
    
if __name__ == '__main__':
    main()

