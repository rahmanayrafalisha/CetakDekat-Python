
from data import tempat_fotocopy

def tampilkan_tempat():
    print("\n================================")
    print("     DAFTAR TEMPAT FOTOCOPY")
    print("================================")

    for kode, tempat in tempat_fotocopy.items():
        print(f"\n{kode}. {tempat['nama']}")
        print(f"   Alamat : {tempat['alamat']}")
        print(f"   Kontak : {tempat['kontak']}")


def pilih_tempat():
    tampilkan_tempat()

    while True:
        pilihan = input("\nPilih tempat fotocopy (1/2): ").strip()

        if pilihan in tempat_fotocopy:
            return tempat_fotocopy[pilihan]

        print("Pilihan tidak tersedia. Silakan coba lagi.")


def tampilkan_layanan(tempat):
    print("\n================================")
    print("       PILIH JENIS LAYANAN")
    print("================================")

    for kode, layanan in tempat["harga"].items():
        print(
            f"{kode}. {layanan['nama']} "
            f"- Rp{layanan['harga']:,}".replace(",", ".")
        )


def pilih_layanan(tempat):
    tampilkan_layanan(tempat)

    while True:
        pilihan = input("\nPilih layanan (1/2/3): ").strip()

        if pilihan in tempat["harga"]:
            return tempat["harga"][pilihan]

        print("Pilihan layanan tidak tersedia.")


def input_jumlah():
    while True:
        try:
            jumlah = int(input("\nMasukkan jumlah lembar: "))

            if jumlah <= 0:
                print("Jumlah lembar harus lebih dari 0.")
            else:
                return jumlah

        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


def hitung_biaya(tempat, layanan, jumlah):
    harga = layanan["harga"]
    total = harga * jumlah

    print("\n================================")
    print("       HASIL PERHITUNGAN")
    print("================================")
    print(f"Tempat Fotocopy : {tempat['nama']}")
    print(f"Jenis Layanan   : {layanan['nama']}")
    print(f"Harga per Lembar: Rp{harga:,}".replace(",", "."))
    print(f"Jumlah Lembar   : {jumlah}")
    print("--------------------------------")
    print(f"TOTAL BIAYA     : Rp{total:,}".replace(",", "."))
    print("================================")
