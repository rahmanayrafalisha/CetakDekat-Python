from fungsi import (
    tampilkan_tempat,
    pilih_tempat,
    pilih_layanan,
    input_jumlah,
    hitung_biaya
)


#fungsi menu utamanya
def tampilkan_menu():
    print("\n====================================")
    print("           CETAKDEKAT")
    print("    Layanan Fotocopy dan Cetak")
    print("====================================")
    print("1. Lihat Daftar Tempat Fotocopy")
    print("2. Hitung Biaya Fotocopy")
    print("3. Keluar")
    print("====================================")

#fungsi utamanya program
def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            tampilkan_tempat()

        elif pilihan == "2":
            tempat = pilih_tempat()
            layanan = pilih_layanan(tempat)
            jumlah = input_jumlah()

            hitung_biaya(tempat, layanan, jumlah)

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan CetakDekat!")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih 1-3.")


# MENJALANKAN PROGRAM
if __name__ == "__main__":
    main()
