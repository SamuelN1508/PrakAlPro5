# Meminta input jumlah matkul
jumlah = int(input("Masukan jumlah kuliah: "))

# Nilai ips awal 0
ips = 0

# Perulangan for dengan range(jumlah)
for i in range(jumlah):
    # Meminta input nilai matkul dalam perulangan
    nilai = input(f"Nilai MK {i+1}: ")
    # Menentukan apakah nilainya A, B, C atau D
    if nilai == "A":
        # Jika nilai A maka ips akan ditambah 4, dan seterusnya
        ips += 4
    elif nilai == "B":
        ips += 3
    elif nilai == "C":
        ips += 2
    elif nilai == "D":
        ips += 1

# Menghitung rata rata ips
IPS = ips/jumlah

# Membulatkan IPS sampai 2 digit belakang koma
rounded_IPS = round(IPS, 2)

# Print hasil IPS akhir
print(f"Nilai IPS anda semester ini {rounded_IPS}")

