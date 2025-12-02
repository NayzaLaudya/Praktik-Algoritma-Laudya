import matplotlib.pyplot as plt

# ==========================
# 1. INISIALISASI VARIABEL
# ==========================
suhu_awal = 25        # derajat Celcius
kenaikan_per_detik = 2
waktu_simulasi = 20   # detik

# Array dan matriks
array_suhu = []
matriks_data = []

# ==========================
# 2. PERHITUNGAN (LOOPING)
# ==========================
print("=== Simulasi Pemanasan Logam ===")

for t in range(waktu_simulasi + 1):
    suhu = suhu_awal + kenaikan_per_detik * t

    # simpan ke array dan matriks
    array_suhu.append(suhu)
    matriks_data.append([t, suhu])

    # tampilkan ke layar
    print(f"Detik {t}: Suhu = {suhu}°C")

    # ==========================
    # 3. IF-CONDITION
    # ==========================
    if suhu > 60:
        print("PERINGATAN: Logam sudah panas!")
        break

# ==========================
# 4. MENAMPILKAN MATRKS
# ==========================
print("\n=== Matriks Data [waktu, suhu] ===")
for row in matriks_data:
    print(row)

# ==========================
# 5. PLOTTING GRAFIK
# ==========================
plt.figure()
plt.plot(range(len(array_suhu)), array_suhu, marker='o')
plt.title("Grafik Perubahan Suhu Logam")
plt.xlabel("Waktu (detik)")
plt.ylabel("Suhu (°C)")
plt.grid(True)
plt.show()
