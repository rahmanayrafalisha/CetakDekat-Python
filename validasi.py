"""
Modul validasi.py
Berisi fungsi untuk memeriksa kebenaran input pengguna.
"""


def validasi_teks(teks, nama_field):
    """Memastikan input teks tidak kosong."""
    if not teks.strip():
        raise ValueError(f"{nama_field} tidak boleh kosong.")

    return teks.strip()


def validasi_angka(nilai, nama_field):
    """Memastikan input berupa angka positif."""
    try:
        angka = int(nilai)

        if angka < 0:
            raise ValueError(f"{nama_field} tidak boleh negatif.")

        return angka

    except ValueError:
        raise ValueError(f"{nama_field} harus berupa angka positif atau nol.")


def validasi_jumlah(jumlah):
    """Memastikan jumlah pesanan lebih dari nol."""
    angka = validasi_angka(jumlah, "Jumlah")

    if angka <= 0:
        raise ValueError("Jumlah pesanan minimal 1.")

    return angka