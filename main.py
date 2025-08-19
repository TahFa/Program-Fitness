import os

temp = {}
jadwal = {}

def manage_data(nama, jk, umur, bb, tb, nama_baru=None):
    if nama_baru and nama_baru != nama:
        temp[nama_baru] = (jk, umur, bb, tb)
        del temp[nama]
        nama = nama_baru
    else:
        temp[nama] = (jk, umur, bb, tb)
    return nama

def view_dataDiri(nama):
    while True:
        os.system('cls')
        jk, umur, bb, tb = temp[nama]
        print(f"Nama Lengkap\t: {nama}")
        print(f"Jenis Kelamin\t: {jk}")
        print(f"Usia\t\t: {umur}")
        print(f"Berat Badan\t: {bb}")
        print(f"Tinggi Badan\t: {tb}")
        option = input("Ingin Ubah Data diri? (y/n): ").lower().strip()

        if option == "y":
            while True:
                os.system('cls')
                nama_baru = input("\nMasukkan Nama Lengkap\t: ").strip()
                jk = input("Jenis Kelamin (L/P)\t: ").upper().strip()
                try:
                    umur = int(input("Usia\t\t\t: ").strip())
                    bb = int(input("Berat Badan (kg)\t: ").strip())
                    tb = int(input("Tinggi Badan (cm)\t: ").strip())

                    if nama_baru and jk:
                        print("\nData Berhasil di Update!\n")
                        manage_data(nama, jk, umur, bb, tb, nama_baru)
                        nama = nama_baru
                        break
                    else:
                        print("Input tidak boleh kosong!\n")
                        input("\nTekan Enter untuk kembali...")
                except ValueError:
                    print("Usia, berat dan tinggi badan harus berupa angka!\n")
                    input("\nTekan Enter untuk kembali...")
        elif option == "n":
            break
        else:
            print("Input Tidak Valid! Ketik y atau n")
            input("\nTekan Enter untuk kembali...")

    return nama

def hitung_imt(berat, tinggi):
    imt = berat / ((tinggi / 100) ** 2)
    if imt < 18.5:
        kategori = "Kurus"
    elif 18.5 <= imt <= 25.0:
        kategori = "Normal"
    elif 25.0 < imt <= 27.0:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"
    return imt, kategori

def rekomendasi_olahraga(tujuan):
    olahraga = {
        1: {
            "pemula": ["Jalan cepat 20 menit", "Stretching", "Wall sit"],
            "menengah": ["Jogging 20 menit", "Squat 3x15", "Plank 3x30 detik"],
            "lanjutan": ["HIIT 20 menit", "Push-up 4x10", "Burpees 3x10"]
        },
        2: {
            "pemula": ["Wall push-up", "Bodyweight squat", "Chair dip"],
            "menengah": ["Push-up", "Dumbbell shoulder press", "Goblet squat"],
            "lanjutan": ["Deadlift", "Barbell squat", "Split push/pull/leg"]
        },
        3: {
            "pemula": ["Jalan santai", "Step-up", "March in place"],
            "menengah": ["Skipping", "Jogging", "Mountain climber"],
            "lanjutan": ["Sprint", "HIIT full body", "Jump lunge"]
        }
    }

    print("Beberapa latihan yang mungkin cocok untukmu : ")
    for level, latihan in olahraga[tujuan].items():
        print(f"{level:8} :", ", ".join(latihan))

def tambah_jadwal():
    while True:
        os.system('cls')
        hari = input("Masukkan hari olahraga (Contoh: Jumat)\t: ").title()
        nama = input("Masukkan nama olahraga\t\t\t: ").capitalize()

        if not hari or not nama:
            print("Input tidak boleh kosong!\n")
            input("\nTekan Enter untuk kembali...")
            continue
        elif hari not in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]:
            print("Input hari tidak valid!\n")
            input("\nTekan Enter untuk kembali...")
            continue

        try:
            durasi = int(input("Durasi Olahraga (Menit)\t\t\t: "))
            if hari not in jadwal:
                jadwal[hari] = []
            jadwal[hari].append({"nama": nama, "durasi": durasi})
            print(f"\nJadwal olahraga hari {hari} berhasil ditambahkan.\n")

            while True:
                ask = input("Mau buat Jadwal lagi? (y/n): ").lower().strip()
                if ask == "y":
                    break
                elif ask == "n":
                    return
                else:
                    print("Input Tidak Valid")
                    input("\nTekan Enter untuk kembali...")
        except ValueError:
            print("Durasi harus berupa angka!\n")
            input("\nTekan Enter untuk kembali...")

def hapus_jadwal(hari):
    if hari not in jadwal or not jadwal[hari]:
        print("Tidak ada jadwal di hari tersebut.\n")
        return

    while True:
        os.system('cls')
        print(f"\nJadwal di hari {hari}:")
        for i, item in enumerate(jadwal[hari], 1):
            print(f"{i}. {item['nama']} - {item['durasi']} menit")

        try:
            nomor = int(input("Nomor latihan yang ingin dihapus: "))
            if 1 <= nomor <= len(jadwal[hari]):
                hapus = jadwal[hari].pop(nomor - 1)
                print(f"'{hapus['nama']}' berhasil dihapus dari hari {hari}.\n")
                if not jadwal[hari]:
                    del jadwal[hari]
                break
            else:
                print("Nomor tidak valid!\n")
                input("\nTekan Enter untuk kembali...")
        except ValueError:
            print("Input harus berupa angka!\n")
            input("\nTekan Enter untuk kembali...")

def lihat_jadwal():
    while True:
        os.system('cls')
        if not jadwal:
            print("Belum ada jadwal yang tersimpan.\n")
            return

        print("\n" + "Jadwal Olahraga".center(45))
        print("-" * 45)

        for hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]:
            if hari in jadwal:
                print(f"{hari}:")
                for i, item in enumerate(jadwal[hari], 1):
                    print(f"    {i}. {item['nama']} - {item['durasi']} menit")
                print()

        ask = input("Mau hapus jadwal? (y/n): ").lower().strip()
        if ask == "y":
            pilih_hari = input("Ketik hari yang ingin dihapus jadwalnya: ").title().strip()
            if pilih_hari in jadwal:
                hapus_jadwal(pilih_hari)
            else:
                print("Hari tidak valid atau tidak ada di Jadwal!\n")
                input("\nTekan Enter untuk kembali...")
        elif ask == "n":
            break
        else:
            print("Input tidak valid!\n")
            input("\nTekan Enter untuk kembali...")

def kalori_harian(nama):
    jk, umur, bb, tb = temp[nama]
    list_aktivitas = {
        1: (1.2, "Tidak aktif (sedentari)"),
        2: (1.375, "Sedikit aktif (olahraga ringan 1-3 hari/minggu)"),
        3: (1.55, "Cukup aktif (olahraga sedang 3-5 hari/minggu)"),
        4: (1.725, "Sangat aktif (olahraga berat 6-7 hari/minggu)"),
        5: (1.9, "Ekstra aktif (pekerjaan fisik + olahraga intens)")
    }

    jumlah_hari = len(jadwal)
    if jumlah_hari == 0:
        tingkat_aktivitas = 1
    elif jumlah_hari < 3:
        tingkat_aktivitas = 2
    elif 3 <= jumlah_hari <= 5:
        tingkat_aktivitas = 3
    elif jumlah_hari == 6:
        tingkat_aktivitas = 4
    else:
        tingkat_aktivitas = 5

    bmr = 10 * bb + 6.25 * tb - 5 * umur + ( 5 if jk == "L" else 161)
    tdee = bmr * list_aktivitas[tingkat_aktivitas][0]
    return round(tdee)


def main():
    os.system('cls')
    print("="*8, "Selamat Datang di Program Fitness", "="*8 + "\n")

    while True:
        nama = input("Masukkan Nama Lengkap\t: ").strip()
        jk = input("Jenis Kelamin (L/P)\t: ").upper().strip()
        try:
            umur = int(input("Usia\t\t\t: ").strip())
            bb = int(input("Berat Badan (kg)\t: ").strip())
            tb = int(input("Tinggi Badan (cm)\t: ").strip())

            if nama and jk:
                manage_data(nama, jk, umur, bb, tb)
                break
            else:
                print("Input tidak boleh ada yang kosong!\n")
        except ValueError:
            print("Usia, berat dan tinggi badan harus berupa angka!\n")
    
    key = nama

    while True:
        os.system('cls')
        print("\nSilahkan Pilih Fitur :")
        print("1. Hitung IMT")
        print("2. Rekomendasi Olahraga")
        print("3. Buat Jadwal Olahraga")
        print("4. Lihat Jadwal Olahraga")
        print("5. Kalori Harian")
        print("6. Data Diri")
        print("7. Keluar")
        try:
            choose = int(input("Pilih : "))
            match choose:
                case 1:
                    imt, kategori = hitung_imt(temp[key][2], temp[key][3])
                    print(f"IMT: {round(imt, 2)} -> {kategori}")
                    input("\nTekan Enter untuk kembali...")
                case 2:
                    while True:
                        os.system('cls')
                        print("Tujuan olahragamu?")
                        print("1. Kebugaran\n2. Massa Otot\n3. Turun Berat")
                        try:
                            tujuan = int(input("Pilih (1-3): "))
                            if tujuan in [1, 2, 3]:
                                os.system('cls')
                                rekomendasi_olahraga(tujuan)

                                while True:
                                    ask = input("\nMau langsung Buat Jadwal? (y/n): ").lower().strip()
                                    if ask == "y":
                                        tambah_jadwal()
                                        break
                                    elif ask == "n":
                                        break
                                    else:
                                        print("Input tidak valid!")
                                break
                            else:
                                print("Input angka 1-3.")
                                input("\nTekan Enter untuk kembali...")
                        except ValueError:
                            print("Input harus berupa angka!")
                            input("\nTekan Enter untuk kembali...")
                case 3:
                    tambah_jadwal()
                case 4:
                    lihat_jadwal()
                case 5:
                    hasil_kalori = kalori_harian(key)
                    print(f"Kebutuhan kalori harian anda: {hasil_kalori} kcal")
                    input("\nTekan Enter untuk kembali...")
                case 6:
                    key = view_dataDiri(key)
                case 7:
                    print("Terima kasih telah menggunakan program ini..")
                    break
                case _:
                    print("Pilihan tidak valid!")
                    input("\nTekan Enter...")
        except ValueError:
            print("Masukkan angka yang valid!")
            input("\nTekan Enter...")

main()
