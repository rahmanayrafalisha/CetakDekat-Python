"""
Modul models.py
Mendefinisikan struktur objek tempat fotocopy.
"""

class TempatFotocopy:
    """Mewakili data sebuah tempat fotocopy."""

    def __init__(
        self,
        id,
        nama,
        kategori,
        alamat,
        kontak,
        harga_hitam_putih,
        harga_warna,
        harga_cetak
    ):
        self.id = str(id)
        self.nama = nama
        self.kategori = kategori
        self.alamat = alamat
        self.kontak = kontak
        self.harga_hitam_putih = int(harga_hitam_putih)
        self.harga_warna = int(harga_warna)
        self.harga_cetak = int(harga_cetak)

    def ke_dict(self):
        """Mengubah objek menjadi dictionary untuk penyimpanan csv."""
        return {
            "id": self.id,
            "nama": self.nama,
            "kategori": self.kategori,
            "alamat": self.alamat,
            "kontak": self.kontak,
            "harga_hitam_putih": self.harga_hitam_putih,
            "harga_warna": self.harga_warna,
            "harga_cetak": self.harga_cetak
        }