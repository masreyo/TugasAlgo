def ubah_buku(dataBuku):
    bukuTmp = input("Masukkan ISBN Buku yang ingin diubah: ")
    for buku in dataBuku:
        if buku["ISBN"]==bukuTmp:
            buku["Judul"]=input("Judul: ")
            buku["Tahun Terbit"]=input("Tahun Terbit: ")
            buku["Penerbit"]=input("Penerbit: ")
            while True:
                try:
                    stok=int(input("Masukkan Jumlah Stok: "))
                    if stok>0:
                        buku["Jumlah Buku"] = stok
                        print("Berhasil edit data buku!")
                        return 1
                    print("Masukkan angka yang valid!")
                except ValueError:
                    print("Masukkan angka!")
    print("Buku dengan ISBN",bukuTmp,"Tidak Ditemukan!")
    return 0

