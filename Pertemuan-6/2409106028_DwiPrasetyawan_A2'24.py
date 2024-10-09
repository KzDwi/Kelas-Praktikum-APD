# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twilight"
#     # "Buku1" : "Harry ",
#     "Buku4" : "Harry Potter"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku["Buku4"])

# daftar_buku = {}
# daftar_buku["Buku1"] = "Harry Potter"

# print(daftar_buku)

# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
# }
# }

# # print(Biodata['Social Media']['Discord'])
# print(Biodata['KRS'][1])
# print(Biodata['KRS'][0::])
# print(Biodata.get('KRS'))


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# print(Nilai)
# Nilai ['Sejarah'] = 100
# print(Nilai['Sejarah'])
# Nilai ['Fisika'] = 100
# print(Nilai['Fisika'])

# Nilai.update(Nilai['Biologi' : 80])
# print(Nilai)

# del Nilai['Kimia']
# print(Nilai)

# simpan = Nilai.pop('Fisika')
# print(Nilai)
# print(simpan)
# print("Jumlah Data +",len(Nilai))


# for i in Nilai:
#     print(i)
# print('')
# for i,j in Nilai.items():
    # print(f"Nilai {i} anda adalah {j}")

# for i in Nilai:
#     print(i)
# print('')
# for mapel,nilai in Nilai.items():
#     print(f"Nilai {mapel} adalah {nilai}")

# Copy & 

# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")


# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for penyanyi,  in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# #Sebelum Dilakukan Perubahan
# print(mahasiswa)

# #Menambahkan Item pada Nested Dictionary
# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)

# #Mengubah Item pada Nested Dictionary
# mahasiswa[101]["Nama"] = "Rizal"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[101]["Umur"]
# print(mahasiswa)

# # Studi Kasus 1
# mahasiswa = {
# 25 : {"Nama" : "Rasyid",  "Umur" : 19, "Nim" : 25, "Jurusan" : "Informatika", "Angkatan" : 34},
# }
# #Menambahkan Item pada Nested Dictionary
# mahasiswa[25]["Jenis Kelamin"] = "Pria"
# print(mahasiswa)

# #Mengubah Item pada Nested Dictionary
# mahasiswa[25]["Nama"] = "Zifa"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[25]["Angkatan"]
# print(mahasiswa)

# batagor = {
#     'Matematika' : 90,
#     'Fisika' : 80,
#     'Biologi': 80,
#     'Kimia' : 70
# }

# total = sum(batagor.values())
# print("Nilai total : ", total)
# rata = total / len(batagor)
# print("Nilai rata-rata : ", rata)