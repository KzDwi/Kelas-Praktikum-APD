#=========================================================

#Studi Kasus Nomor 1

# harga = int(input("Masukkan harga barang :"))
# jumlah = int(input("Masukkan jumlah buku :"))
# diskon = 0.20
# harga_total = harga * jumlah

# if harga_total >= 100000 and jumlah >= 5 :
#     harga_diskon = harga_total - (harga_total * diskon)
#     print(f"total bayar sejumlah Rp {harga_diskon} setelah mendapat potongan sebesar 20%")
# else:
#     print(f"total bayar sejumlah Rp {harga_total}")

#=========================================================

#Studi Kasus Nomor 2

#jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) :").upper()
    #saya menggunakan .upper() di codingan awal saya untuk error handling ketika semisal yang di input adalah "l" dan bukan "L"
#hasil = "Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"
#print(hasil)
#====================
# jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) :") 

# result = "Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"

# print(result)

#=========================================================

#Contoh Penggunaan Match Case

# print("""
# ================================================================

#                   Kalkulator Sederhana
      
#     [1] Pertambahan 
#     [2] Pengurangan 
#     [3] Perkalian   
#     [4] Pembagian   
# ================================================================
# """)
# fitur = int(input("Pilih Fitur [1 - 4] : "))
# match fitur:
#     case 1:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a + b
#         print(f"Hasil penjumlahan Angka 1 dan Angka 2 adalah {c}")
#     case 2:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a - b
#         print(f"Hasil pengurangan Angka 1 dan Angka 2 adalah {c}")
#     case 3:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a * b
#         print(f"Hasil perkalian Angka 1 dan Angka 2 adalah {c}")
#     case 4:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a / b
#         print(f"Hasil pembagian Angka 1 dan Angka 2 adalah {c}")
#     case _:
#         print("Salah masukkan angka bro")