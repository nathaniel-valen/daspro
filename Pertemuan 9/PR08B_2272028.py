# File : PR09B_2272028.py
# Penulis : Nathaniel Valentino Robert
# Deskripsi :
# Buatlah program untuk memberitahu user,
# apakah berat badannya sudah ideal atau belum.
# Program akan meminta user untuk memasukan
# tinggi badan (cm)dan berat badan (kg).
# Ideal tidaknya berat badan ditentukan
# oleh Body Mass Index (BMI).

# Kamus Lokal
# tB_m = var menghitung konversi tb cm ke m
# BMI = var menghitung BMI
def hitungBMI(bB, tB):
    # menghitung BMI
    tB_m = tB / 100 # konversi tinggiBadan dari cm ke m
    BMI = bB / (tB_m * tB_m)
    return BMI

# Kamus Lokal
# BMI = var hasil BMI yang sudah dihitung
# sT = var status BMI
def cekStatus(BMI):
    # menentukan kriteria berat badan seseorang berdasarkan nilai BMI
    if BMI < 18.5:
        sT = "underweight atau berat badan kurang"
    elif 18.5 <= BMI <= 22.9:
        sT = "berat badan ideal, sangat bagus"
    elif 23 <= BMI <= 24.9:
        sT = "kategori ideal warning, jaga pola makan dan olahraga"
    elif 25 <= BMI <= 29.9:
        sT = "kondisi berat badan memasuki batas obesitas, segera mulai program diet"
    else:
        sT = "anda sudah termasuk kategori obesitas"
    return sT

# Kamus Lokal
# bB = var input berat badan (float)
# tB = var input tinggi badan (float)
# BMI = var hasil fungsi hitungBMI
# sT = var hasil fungsi cekStatus
def main():
    # meminta pengguna memasukkan tinggi badan dan berat badan
    bB = float(input("Berat badan (kg): "))
    tB = float(input("Tinggi badan (cm): "))

    # menghitung BMI dan menentukan kriteria berat badan
    BMI = hitungBMI(bB, tB)
    sT = cekStatus(BMI)

    # mencetak hasil
    print("BMI:", BMI)
    print(sT)

if __name__ == "__main__":
    main()
