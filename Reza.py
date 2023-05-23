# fungsi untuk menambahkan buku
def tambah_buku(dataBuku):
    while True:
        try:
            buku = int(input("anda ingin menambah buku berapa kali : "))
            if buku>0:
                break
            print("Masukkan angka yang valid!")
            #input jumlah buku yang akan dimasukkan ke dalam list
        except ValueError:
            print("Masukkan angka!")
    for i in range(buku):
        print("\n===============================")
        print("buku to - " + str(i + 1) + " :")
        add_buku = {}
        add_buku["ISBN"] = input("ISBN: ")
        add_buku["Judul"] = input("Judul: ")
        add_buku["Tahun Terbit"] = input("Tahun Terbit: ")
        add_buku["Penerbit"] = input("Penerbit: ")
        while True:
            try:
                stok=int(input("Masukkan Jumlah Stok: "))
                if stok>0:
                    break
                print("Masukkan angka yang valid!")
            except ValueError:
                print("Masukkan angka!")
        add_buku["Jumlah Buku"] = stok
        print(f"Buku {add_buku['Judul']} berhasil ditambahkan ke dalam Perpustakaan")
        dataBuku.append(add_buku)

# fungsi untuk menghapus buku berdasarkan ISBN
def hapus_buku(dataBuku,dataPeminjam):
    Isbn = input("Masukkan ISBN buku yang ingin anda hapus : ")
    for buku in dataBuku:
        if buku["ISBN"] == Isbn:
            for peminjam in dataPeminjam:
                if peminjam["Status"] != "Pinjam" and Isbn==peminjam["Nama Buku yang Dipinjam"]:
                    print("Buku masih dipinjam dan tidak dapat dihapus.")
                    return 0
            dataBuku.remove(buku)
            print("Buku dengan ISBN", Isbn, "telah dihapus.")
            return 1
    print("Buku dengan ISBN", Isbn, "tidak tersedia!")
    return 0


