<<<<<<< HEAD
# nama = ["celio","shandy","farel","ghazali","vito"]
# print(type[nama])

# nama = ["celio","shandy","farel","ghazali","vito"]
# print("Sebelum :")
# print(type[nama])

# nama = ["celio","shandy","farel","ghazali","vito"]
# print("Sebelum :")
# print(nama)
# print("sesudah :")
# nama.append("afrizal")
# print(nama)

# nama = ["celio","shandy","farel","ghazali","vito"]
# print("Sebelum :")
# print(nama)
# print("sesudah :")
# nama.insert(2,"afrizal")
# print(nama)

# nama = ["celio","shandy","farel","ghazali","vito"]
# print("Sebelum :")
# print(nama)
# print("sesudah :")
# nama[4] = "fufufafa"
# print(nama)

# #Hapus dan Pindahkan
# nama = ["celio","shandy","farel","ghazali","vito"]
# print("Sebelum :")
# print(nama)
# print("sesudah :")
# # del nama[2]
#     hapus = nama.pop(2)
# print(nama)
#     print(hapus)

# nama = ["celio",
#         "shandy",
#         "farel",
#         "ghazali",
#         "vito",
#         "yuyun",
#         "adi",
#         "ifnu"]
# print("Sebelum :")
# print(nama)
# print("sesudah :")
# nama[4] = "fufufafa"
# print(nama)
# # print(nama[1:9])
# print(nama[1:9:2])

# matkul = ["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]
# data = nama+matkul
# print("Sebelum :")
# print(nama)
# print("sesudah :")
# print(data)
# # print(data*3)

# data = ["farel","celio",[1,2["halo",23,2,4,True]]]
# # print(data[2][2][::-1])
# # print(data[-1])
# matkul = [1,2,3,4,[5,6,7]]

# matkul = [1,2,3,4,5,6,7,8,9]
# for i in matkul:
#     print(i, end="--")

# matkul = [[1,2,3],[4,5,6],[7,8,9]]
# for i in matkul:
#     # print(i)
#     for j in i:
#         print(j)

# nama = ('farrel',"vito",'shandy','rijal')
# print(nama[1:])

# data_mahasiswa = (69,"Informatika","2209106044","Aldy Septian")
# absen,prodi,nim,nama = data_mahasiswa
# print(nim)

# print(
#     """
# ================================
# |   DATA MAHASISWA A24         |
# ================================
# |   1. TAMBAH DATA             |
# |   2. TAMPILKAN DATA          |
# |   3. UBAH DATA               |
# |   4. HAPUS DATA              |
# |   5. KELUAR                  |
# ================================
# """
# )

# while True :
#     pilih = int(input('PILIH : '))
#     if pilih == 1:
#         nama = input("NAMA : ")
#         nim = input("NIM : ")
#         kelas = input("KELAS : ")
#         data_mahasiswa.append([nama,nim,kelas])
#     if pilih == 2:
#         for i in data_mahasiswa:
#             print(f"\n Data mahasiswa ke-{i+1}\n NAMA : {data[i]}\n NIM : {data[i+1]}\n KELAS : {data[i+1]}")

#     if pilih == 3:
#         nama_lama = input("Nama Baru :")
#         for i in range(len[data_mahasiswa]):

#     if pilih == 4:
#     if pilih == 5:
#     else:

# ====================================================================================
# nama = [
#     "celio",
#     "shandy",
#     "farel",
#     "ghazali",
#     "vito",
#     "yuyun",
#     "adri",
#     "rizal",
#     "adi",
#     "ifnu"
# ]

# matkul = ["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]

# data = nama+matkul

# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah:")
# print(data*3)

# # nama.insert(2,"afrizal")
# # print(nama)
# # nama[4]= "fufufafa"
# # hapus = nama.pop(2)
# # print(nama)
# # print(hapus)


# print(nama[1:9:2])

# data = ["farel","celio",[1,2,["halo",23,2.3,True]]]

# print(data[2][2][::-1])

# print(data[::-1])

# matkul = [[1,2,3],[4,5,6],[7,8,9]]
# # print(matkul[4][3][::-1])

# for i in matkul:
#     for j in i:
#         print(j)

# nama = ('farrel', 'vito', 'shandy', 'rijal')
# print(nama[1:])

# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# absen, prodi, nim, nama = mahasiswa
# print(nim)

# print( 
# """
# ===========================
# |   DATA MAHASISWA A24    |
# ===========================
# |    1. TAMBAH DATA       |           
# |    2. TAMPILKAN DATA    |          
# |    3. UBAH DATA         |     
# |    4. HAPUS DATA        |      
# |    5. KELUAR            |  
# ===========================
# """
# )

# data_mahasiswa = []
# while True:
#     pilih = int(input("PILIH : "))
#     if pilih == 1:
#         nama = input("NAMA : ")
#         nim = input("NIM : ")
#         kelas = input("KELAS : ")
#         data_mahasiswa.append([nama,nim,kelas])
#     elif pilih == 2:
#         for i in range(len(data_mahasiswa)):
#             print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
#     elif pilih == 3:
#         nama_lama = input("Nama Baru : ")
#         for i in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
#                 nama_baru = input("NAMA : ")
#                 nim_baru = input("NIM : ")
#                 kelas_baru = input("KELAS : ")
#                 data_mahasiswa[i][0] = nama_baru
#                 data_mahasiswa[i][1] = nim_baru
#                 data_mahasiswa[i][2] = kelas_baru
#     elif pilih == 4:
#         nama_lama = input("Nama yang ingin dihapus")
#         for i in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
#                 del data_mahasiswa[i]
#     elif pilih == 5:
#         print("Terima Kasih Telah Mengakses Data Mahasiswa")
#         break
#     else:
#         print("Anda Salah Input")
=======
#for i in range (2,12,2):
#    print("halo")
#print("hai")

#print("menu rumah makan Informatika 24: ")
#print("---------------------------------")
#simpan = ["Nasi Goreng","Mie Goreng","Mie Ayam","Bakso","Soto"]
#for i in simpan:
#    print(i)

#print("menu rumah makan Informatika 24: ")
#print("---------------------------------")
#simpan = ["Nasi Goreng","Mie Goreng","Mie Ayam","Bakso","Soto"]
#for i, menu in enumerate(simpan,start=1):
#    print(f"{i},{menu}")

#print("menu rumah makan Informatika 24: ")
#print("---------------------------------")
#simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
#for i in range(len{simpan}):
#    print(f"{i+1}, {simpan[i]}")

#makanan = ["mie", "sop", "bakso"]
#minuman = ["es teh", "air putih", "es jeruk"]
#for i in makanan :
#    for j in minuman:
#        print(f"{i} & {j}")

#jawab = "ya"
#Hitung = 0
#while(jawab == "ya" or jawab == "Ya"):
#    hitung += 1
#    jawab = input("hitung lagi tidak? ")
#    print(f"hasil perulangan: {hitung}")

#i = 0
#while i < 5:
#    print(i)
#    i += 1

#i = 0
#while i < 5:
#    print(i)
#    break
#    i += 1

#hitung = 0
#while True:
#    hitung += 1
#    ulang = input("Masih ingin Mengulangi? ")
#    if ulang == "tidak" or ulang == "Tidak":
#        print("Oke kita udahan")
#        break
#print(f"Total perulangan : {hitung}"

#hitung = 0
#while True:
#    hitung += 1
#    ulang = input("Masih ingin Mengulangi? ")
#    if ulang == "y" or ulang == "Y":
#        print("Oke kita lanjut")
#        continue
#    
#print(f"Total perulangan : {hitung}"

#print("Daftar bilangan ganjil dari 1-10")
#for i in range(10):
#    if i % 2 == 0 :
#        print(f"{i} genap")
#        continue
#    else:
#        print(f"{i} ganjil")
#        continue

#print("Daftar bilangan ganjil dari 1-10")
#for i in range(10):
#    if i % 2 == 0 :
#        continue
#    print(i)

#total = 0
#while True:
#    angka = int(input("Masukkan angka positif (input negatif jika ingin berhenti) : "))
#    if angka < 0:
#        break
#    else:
#        total += angka
#print(f"jumlah total adalah: {total}")


# Meminta input dari pengguna untuk range maksimal
#range_maksimal = int(input("Masukkan range maksimal: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan prima
#hitung_prima = 0

# Loop untuk memeriksa setiap angka dari 1 hingga range_maksimal
#for angka in range(1, range_maksimal):
#    angka += 1
#    apakah_prima = True  # Anggap angka tersebut prima

    # Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
#    for i in range(2, angka):
#        if angka % i == 0:
#            apakah_prima = False  # Jika ada pembagi, bukan bilangan prima
            # print(f"{angka} bukan prima")
#            break
    # Jika angka tersebut prima, tambahkan jumlah hitung_prima
#    if apakah_prima == True:
#        print(f"{angka} prima")
#        hitung_prima += 1

# output
#print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")
>>>>>>> 437f9bed506ecdf305c4f9f763afb5060934580d
