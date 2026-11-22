"""
Modul services.py
Mengelola pencarian, pengurutan, filter, dan perhitungan biaya.
"""


def cari_data(daftar_data, kata_kunci):
    """Mencari tempat fotocopy berdasarkan ID, nama, atau kategori."""
    kata_kunci = kata_kunci.lower().strip()

    return [
        data for data in daftar_data
        if kata_kunci in data["id"].lower()
        or kata_kunci in data["nama"].lower()
        or kata_kunci in data["kategori"].lower()
    ]


def urutkan_data(daftar_data, kolom="nama", terbalik=False):
    """Mengurutkan data berdasarkan kolom yang dipilih."""
    kolom_diizinkan = [
        "id", "nama", "kategori",
        "harga_hitam_putih", "harga_warna", "harga_cetak"
    ]

    if kolom not in kolom_diizinkan:
        raise ValueError("Kolom pengurutan tidak tersedia.")

    return sorted(
        daftar_data,
        key=lambda data: (
            int(data[kolom]) if kolom == "id"
            or kolom.startswith("harga_")
            else data[kolom].lower()
        ),
        reverse=terbalik
    )


def filter_data(daftar_data, **kwargs):
    """Menyaring data berdasarkan beberapa kriteria."""
    hasil = daftar_data

    for kolom, nilai in kwargs.items():
        hasil = [
            data for data in hasil
            if str(data.get(kolom, "")).lower() == str(nilai).lower()
        ]

    return hasil


def hitung_total(harga, *jumlah):
    """Menghitung total biaya berdasarkan harga dan jumlah pesanan."""
    if harga < 0 or any(item <= 0 for item in jumlah):
        raise ValueError("Harga tidak boleh negatif dan jumlah harus lebih dari nol.")

    return harga * sum(jumlah)