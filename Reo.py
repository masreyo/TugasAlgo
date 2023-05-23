def hapus_mahasiswa(dataMahasiswa):
    try:
        npm = int(input("Masukkan NPM mahasiswa yang akan dihapus: "))
    except ValueError:
        print("NPM tersebut tidak ada.")
        return 0

    for mahasiswa in dataMahasiswa:
        if mahasiswa["NPM"] == npm:
            confirmation = input("Apakah Anda yakin ingin menghapus mahasiswa dengan npm "+str(mahasiswa["NPM"])+" dengan nama "+str(mahasiswa["Nama"])+" tersebut? (Y/N): ")
            if confirmation.lower() == "y":
                dataMahasiswa.remove(mahasiswa)
                print("Data mahasiswa berhasil dihapus.")
                return 1
            else:
                print("Proses hapus dibatalkan.")
                return 0
    print("NPM tersebut tidak ada.")
    return 0