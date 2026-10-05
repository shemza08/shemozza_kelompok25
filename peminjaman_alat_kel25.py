# Tugas Praktikum Modul 4 - Function dan Method
# Sistem Peminjaman Alat Laboratorium - Kelompok 25

BATAS_HARI = 3
DENDA_PER_HARI = 5000


# Function non-return, tanpa parameter
def tampilkan_watermark():
    print("=" * 46)
    print("   SISTEM PEMINJAMAN ALAT LAB - KELOMPOK 25")
    print("=" * 46)


# Function return, dengan parameter
def hitung_denda(lama_pinjam):
    if lama_pinjam > BATAS_HARI:
        return (lama_pinjam - BATAS_HARI) * DENDA_PER_HARI
    return 0


# Function return, dengan parameter
def input_angka(pesan):
    teks = input(pesan)
    while not teks.isdigit():
        print("Input harus berupa angka bulat.")
        teks = input(pesan)
    return int(teks)


# Function return, tanpa parameter
def pilih_menu():
    while True:
        print("\n1. Lihat daftar alat")
        print("2. Pinjam alat")
        print("3. Kembalikan alat")
        print("4. Selesai")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan in ("1", "2", "3", "4"):
            return pilihan
        print("Menu tidak tersedia, coba lagi.")


class LabKomputer:
    def __init__(self):
        self.alat = {
            "A01": ["Arduino Uno", 5],
            "A02": ["ESP32", 3],
            "A03": ["Multimeter", 2],
            "A04": ["Solder", 1],
        }
        self.peminjaman = []

    # Method non-return, tanpa parameter
    def tampilkan_alat(self):
        print("\nKode  Nama Alat       Stok")
        for kode, (nama, stok) in self.alat.items():
            if stok > 0:
                print(f"{kode}   {nama:<15} {stok}")
            else:
                print(f"{kode}   {nama:<15} habis")

    # Method return, tanpa parameter
    def total_dipinjam(self):
        return len(self.peminjaman)

    # Method non-return, dengan parameter
    def pinjam(self, peminjam, kode):
        if kode not in self.alat:
            print("Kode alat tidak ditemukan.")
        elif self.alat[kode][1] == 0:
            print(f"Stok {self.alat[kode][0]} sedang habis.")
        else:
            self.alat[kode][1] -= 1
            self.peminjaman.append([peminjam, kode])
            print(f"{peminjam} meminjam {self.alat[kode][0]}, "
                  f"batas pengembalian {BATAS_HARI} hari.")

    # Method non-return, dengan parameter
    def kembalikan(self, peminjam, kode, lama_pinjam):
        if [peminjam, kode] not in self.peminjaman:
            print("Data peminjaman tidak ditemukan.")
        else:
            self.peminjaman.remove([peminjam, kode])
            self.alat[kode][1] += 1
            denda = hitung_denda(lama_pinjam)
            if denda > 0:
                terlambat = lama_pinjam - BATAS_HARI
                rupiah = f"{denda:,}".replace(",", ".")
                print(f"Terlambat {terlambat} hari, denda Rp{rupiah}")
            else:
                print("Alat kembali tepat waktu, tidak ada denda.")


tampilkan_watermark()
lab = LabKomputer()
menu = pilih_menu()
while menu != "4":
    if menu == "1":
        lab.tampilkan_alat()
    elif menu == "2":
        nama = input("Nama peminjam : ")
        kode = input("Kode alat     : ").upper()
        lab.pinjam(nama, kode)
    else:
        nama = input("Nama peminjam : ")
        kode = input("Kode alat     : ").upper()
        lama = input_angka("Lama pinjam (hari): ")
        lab.kembalikan(nama, kode, lama)
    menu = pilih_menu()

print(f"\nSesi selesai. Alat yang masih dipinjam: {lab.total_dipinjam()}")
print("Terima kasih - Kelompok 25")
