buku = {
    "judul": "Cinta Bertemu Di Teknik Unmul",
    "penulis": "Darrell",
    "tahun_terbit": 2026
}

while True:
    print("MENU BUKU =")
    print("1. Tampilkan")
    print("2. Tambah penerbit")
    print("3. Ubah penulis")
    print("4. Hapus penerbit")
    print("5. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        print(buku)

    elif pilih == "2":
        buku["penerbit"] = input("Penerbit: ")

    elif pilih == "3":
        buku["penulis"] = input("Penulis baru: ")

    elif pilih == "4":
        del buku["penerbit"]

    elif pilih == "5":
        print("Data akhir:", buku)
        break

    else:
        print("Pilihan salah.")