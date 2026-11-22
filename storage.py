"""
Modul storage.py
Mengatur proses membaca dan menyimpan data tempat fotocopy
menggunakan file CSV.
"""

import csv
import os

#tentuin lokasi file csv
FILE_DATA = os.path.join("data", "tempat_fotocopy.csv")


def baca_data():
    """Membaca seluruh data tempat fotocopy dari file CSV."""
    daftar_tempat = []

    try:
        with open(FILE_DATA, mode="r", newline="", encoding="utf-8") as file:
            pembaca = csv.DictReader(file)

            for baris in pembaca:
                daftar_tempat.append(baris)

    except FileNotFoundError:
        print("File data tidak ditemukan.")

    except (ValueError, csv.Error) as error:
        print(f"Data tidak dapat dibaca: {error}")

    return daftar_tempat


def simpan_data(daftar_tempat):
    """Menyimpan seluruh data tempat fotocopy ke file CSV."""
    kolom = [
        "id",
        "nama",
        "kategori",
        "alamat",
        "kontak",
        "harga_hitam_putih",
        "harga_warna",
        "harga_cetak"
    ]

    try:
        with open(FILE_DATA, mode="w", newline="", encoding="utf-8") as file:
            penulis = csv.DictWriter(file, fieldnames=kolom)
            penulis.writeheader()
            penulis.writerows(daftar_tempat)

    except (OSError, csv.Error) as error:
        print(f"Data gagal disimpan: {error}")