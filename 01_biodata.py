TAHUN_SEKARANG = 2026

print("BIODATA MAHASISWA")

nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

umur = TAHUN_SEKARANG - tahun_lahir

print("\nKARTU BIODATA")
print(f"Nama   : {nama}")
print(f"NIM    : {nim}")
print(f"Kelas  : {kelas}")
print(f"Umur   : sekitar {umur} tahun")