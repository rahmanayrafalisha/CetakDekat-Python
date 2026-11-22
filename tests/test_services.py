
"""
Pengujian fungsi pada modul services.py.
Menggunakan library unittest.
"""

import unittest

from services import cari_data, urutkan_data, filter_data, hitung_total


class TestCetakDekat(unittest.TestCase):
    """Kumpulan pengujian fitur pengolahan data CetakDekat."""

    def setUp(self):
        """Menyiapkan data untuk pengujian."""
        self.data = [
            {
                "id": "1",
                "nama": "Fotocopy A",
                "kategori": "Fotocopy",
                "harga_hitam_putih": "200"
            },
            {
                "id": "2",
                "nama": "Fotocopy B",
                "kategori": "Fotocopy",
                "harga_hitam_putih": "250"
            }
        ]

    def test_cari_data(self):
        """Menguji pencarian nama tempat."""
        hasil = cari_data(self.data, "Fotocopy A")
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]["id"], "1")

    def test_cari_data_tidak_ditemukan(self):
        """Menguji pencarian data yang tidak tersedia."""
        hasil = cari_data(self.data, "Toko C")
        self.assertEqual(len(hasil), 0)

    def test_urutkan_data(self):
        """Menguji pengurutan harga dari kecil ke besar."""
        hasil = urutkan_data(
            self.data,
            kolom="harga_hitam_putih"
        )
        self.assertEqual(hasil[0]["id"], "1")

    def test_filter_data(self):
        """Menguji penyaringan data berdasarkan kategori."""
        hasil = filter_data(
            self.data,
            kategori="Fotocopy"
        )
        self.assertEqual(len(hasil), 2)

    def test_hitung_total(self):
        """Menguji perhitungan biaya layanan."""
        hasil = hitung_total(200, 10)
        self.assertEqual(hasil, 2000)


if __name__ == "__main__":
    unittest.main()