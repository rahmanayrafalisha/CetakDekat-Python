"""
Modul ui.py
Mengatur tampilan sederhana aplikasi CetakDekat.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from models import TempatFotocopy
from storage import baca_data, simpan_data
from services import cari_data, urutkan_data, hitung_total
from validasi import validasi_teks, validasi_angka


class CetakDekatApp:
    """Kelas untuk mengatur tampilan aplikasi CetakDekat."""

    def __init__(self, root):
        self.root = root
        self.root.title("CetakDekat")
        self.root.geometry("1000x600")
        self.root.configure(bg="#FCEEF3")

        self.daftar_data = baca_data()

        self.buat_tampilan()
        self.tampilkan_data()

    def buat_tampilan(self):
        """Membuat komponen tampilan aplikasi."""

        # Bagian judul
        header = tk.Frame(self.root, bg="#B9DDF2", pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="CETAKDEKAT",
            font=("Arial", 20, "bold"),
            bg="#B9DDF2",
            fg="#333333"
        ).pack()

        tk.Label(
            header,
            text="Layanan Fotocopy dan Cetak Dokumen",
            font=("Arial", 10),
            bg="#B9DDF2",
            fg="#444444"
        ).pack()

        # Bagian pencarian
        frame_atas = tk.Frame(self.root, bg="#FCEEF3")
        frame_atas.pack(fill="x", padx=20, pady=15)

        tk.Label(
            frame_atas,
            text="Cari Tempat:",
            bg="#FCEEF3"
        ).pack(side="left")

        self.input_cari = tk.Entry(frame_atas, width=25)
        self.input_cari.pack(side="left", padx=5)

        tk.Button(
            frame_atas,
            text="Cari",
            command=self.cari,
            bg="#B9DDF2"
        ).pack(side="left", padx=3)

        tk.Button(
            frame_atas,
            text="Tampilkan Semua",
            command=self.tampilkan_data,
            bg="#F4C6D7"
        ).pack(side="left", padx=3)

        tk.Label(
            frame_atas,
            text="Urutkan:",
            bg="#FCEEF3"
        ).pack(side="left", padx=(15, 5))

        self.pilihan_urut = ttk.Combobox(
            frame_atas,
            values=[
                "nama",
                "id",
                "harga_hitam_putih",
                "harga_warna",
                "harga_cetak"
            ],
            state="readonly",
            width=20
        )
        self.pilihan_urut.set("nama")
        self.pilihan_urut.pack(side="left")

        tk.Button(
            frame_atas,
            text="Urutkan",
            command=self.urutkan,
            bg="#B9DDF2"
        ).pack(side="left", padx=3)

        # Bagian tabel
        frame_tabel = tk.Frame(self.root)
        frame_tabel.pack(fill="both", expand=True, padx=20, pady=5)

        kolom = (
            "id", "nama", "kategori", "alamat",
            "kontak", "harga_hitam_putih",
            "harga_warna", "harga_cetak"
        )

        self.tabel = ttk.Treeview(
            frame_tabel,
            columns=kolom,
            show="headings",
            height=12
        )

        judul_kolom = {
            "id": "ID",
            "nama": "Nama Tempat",
            "kategori": "Kategori",
            "alamat": "Alamat",
            "kontak": "Kontak",
            "harga_hitam_putih": "Hitam Putih",
            "harga_warna": "Warna",
            "harga_cetak": "Cetak"
        }

        for nama_kolom in kolom:
            self.tabel.heading(
                nama_kolom,
                text=judul_kolom[nama_kolom]
            )
            self.tabel.column(
                nama_kolom,
                width=120,
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            frame_tabel,
            orient="vertical",
            command=self.tabel.yview
        )

        self.tabel.configure(yscrollcommand=scrollbar.set)
        self.tabel.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bagian tombol
        frame_tombol = tk.Frame(self.root, bg="#FCEEF3")
        frame_tombol.pack(pady=20)

        tk.Button(
            frame_tombol,
            text="Tambah Data",
            command=self.tambah_data,
            width=15,
            bg="#F4C6D7"
        ).pack(side="left", padx=5)

        tk.Button(
            frame_tombol,
            text="Ubah Data",
            command=self.ubah_data,
            width=15,
            bg="#B9DDF2"
        ).pack(side="left", padx=5)

        tk.Button(
            frame_tombol,
            text="Hapus Data",
            command=self.hapus_data,
            width=15,
            bg="#F4C6D7"
        ).pack(side="left", padx=5)

        tk.Button(
            frame_tombol,
            text="Hitung Biaya",
            command=self.hitung_biaya,
            width=15,
            bg="#B9DDF2"
        ).pack(side="left", padx=5)

    def tampilkan_data(self, data=None):
        """Menampilkan data ke dalam tabel."""

        for item in self.tabel.get_children():
            self.tabel.delete(item)

        data = self.daftar_data if data is None else data

        for tempat in data:
            self.tabel.insert(
                "",
                "end",
                values=(
                    tempat["id"],
                    tempat["nama"],
                    tempat["kategori"],
                    tempat["alamat"],
                    tempat["kontak"],
                    tempat["harga_hitam_putih"],
                    tempat["harga_warna"],
                    tempat["harga_cetak"]
                )
            )

    def cari(self):
        """Mencari data berdasarkan kata kunci."""

        kata_kunci = self.input_cari.get()
        hasil = cari_data(self.daftar_data, kata_kunci)
        self.tampilkan_data(hasil)

        if not hasil:
            messagebox.showinfo("Informasi", "Data tidak ditemukan.")

    def urutkan(self):
        """Mengurutkan data berdasarkan kolom pilihan."""

        try:
            kolom = self.pilihan_urut.get()
            hasil = urutkan_data(self.daftar_data, kolom)
            self.tampilkan_data(hasil)

        except ValueError as error:
            messagebox.showerror("Kesalahan", str(error))

    def tambah_data(self):
        """Menambahkan data tempat fotocopy."""

        try:
            nama = validasi_teks(
                simpledialog.askstring("Tambah Data", "Nama tempat:") or "",
                "Nama tempat"
            )
            kategori = validasi_teks(
                simpledialog.askstring("Tambah Data", "Kategori:") or "",
                "Kategori"
            )
            alamat = validasi_teks(
                simpledialog.askstring("Tambah Data", "Alamat:") or "",
                "Alamat"
            )
            kontak = simpledialog.askstring(
                "Tambah Data", "Kontak:"
            ) or "Belum tersedia"

            harga_bw = validasi_angka(
                simpledialog.askstring("Tambah Data", "Harga hitam putih:") or "",
                "Harga hitam putih"
            )
            harga_warna = validasi_angka(
                simpledialog.askstring("Tambah Data", "Harga warna:") or "",
                "Harga warna"
            )
            harga_cetak = validasi_angka(
                simpledialog.askstring("Tambah Data", "Harga cetak:") or "",
                "Harga cetak"
            )

            id_baru = str(max(
                [int(item["id"]) for item in self.daftar_data],
                default=0
            ) + 1)

            tempat = TempatFotocopy(
                id_baru, nama, kategori, alamat, kontak,
                harga_bw, harga_warna, harga_cetak
            )

            self.daftar_data.append(tempat.ke_dict())
            simpan_data(self.daftar_data)
            self.tampilkan_data()

            messagebox.showinfo("Berhasil", "Data berhasil ditambahkan.")

        except ValueError as error:
            messagebox.showerror("Kesalahan Input", str(error))

    def ubah_data(self):
        """Mengubah data tempat fotocopy yang dipilih."""

        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu.")
            return

        id_data = str(self.tabel.item(pilihan[0])["values"][0])
        tempat = next(
            (item for item in self.daftar_data if item["id"] == id_data),
            None
        )

        if tempat is None:
            return

        try:
            kolom = [
                ("nama", "Nama tempat"),
                ("kategori", "Kategori"),
                ("alamat", "Alamat"),
                ("kontak", "Kontak"),
                ("harga_hitam_putih", "Harga hitam putih"),
                ("harga_warna", "Harga warna"),
                ("harga_cetak", "Harga cetak")
            ]

            for key, label in kolom:
                nilai = simpledialog.askstring(
                    "Ubah Data",
                    label,
                    initialvalue=str(tempat[key])
                )

                if nilai is None:
                    return

                if key.startswith("harga_"):
                    tempat[key] = validasi_angka(nilai, label)
                else:
                    tempat[key] = validasi_teks(nilai, label)

            simpan_data(self.daftar_data)
            self.tampilkan_data()
            messagebox.showinfo("Berhasil", "Data berhasil diubah.")

        except ValueError as error:
            messagebox.showerror("Kesalahan Input", str(error))

    def hapus_data(self):
        """Menghapus data tempat fotocopy yang dipilih."""

        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu.")
            return

        id_data = str(self.tabel.item(pilihan[0])["values"][0])

        if messagebox.askyesno("Konfirmasi", "Hapus data ini?"):
            self.daftar_data = [
                item for item in self.daftar_data
                if item["id"] != id_data
            ]

            simpan_data(self.daftar_data)
            self.tampilkan_data()
            messagebox.showinfo("Berhasil", "Data berhasil dihapus.")

    def hitung_biaya(self):
        """Menghitung biaya layanan fotocopy."""

        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning("Peringatan", "Pilih tempat fotocopy dahulu.")
            return

        id_data = str(self.tabel.item(pilihan[0])["values"][0])
        tempat = next(
            (item for item in self.daftar_data if item["id"] == id_data),
            None
        )

        if tempat is None:
            return

        layanan = simpledialog.askstring(
            "Hitung Biaya",
            "Pilih layanan:\n1. Hitam Putih\n2. Warna\n3. Cetak Dokumen"
        )

        if layanan is None:
            return

        daftar_harga = {
            "1": ("Fotocopy Hitam Putih", int(tempat["harga_hitam_putih"])),
            "2": ("Fotocopy Warna", int(tempat["harga_warna"])),
            "3": ("Cetak Dokumen", int(tempat["harga_cetak"]))
        }

        if layanan not in daftar_harga:
            messagebox.showerror("Kesalahan", "Pilihan layanan tidak tersedia.")
            return

        jumlah = simpledialog.askinteger(
            "Hitung Biaya",
            "Masukkan jumlah pesanan:",
            minvalue=1
        )

        if jumlah is None:
            return

        nama_layanan, harga = daftar_harga[layanan]
        total = hitung_total(harga, jumlah)

        messagebox.showinfo(
            "Hasil Perhitungan",
            f"Tempat: {tempat['nama']}\n"
            f"Layanan: {nama_layanan}\n"
            f"Harga satuan: Rp{harga:,}\n"
            f"Jumlah: {jumlah}\n"
            f"Total biaya: Rp{total:,}"
        )