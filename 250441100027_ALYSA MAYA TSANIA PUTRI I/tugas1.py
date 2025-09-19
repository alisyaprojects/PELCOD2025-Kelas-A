print ("="*100)
print ("Soal 1 : berapa jam kamu menonton TV series tersebut?")
print ("="*100)
print ("penyelesaian:")
jumlah_episode = int(input("masukkan durasi per episode (menit):"))
Durasi_per_episode = int(input("masukkan durasi per episode : "))

total_menit = Durasi_per_episode * jumlah_episode
total_jam = total_menit / 60

print ("total durasi menonton TV series :", total_menit, "menit =", total_jam,"jam")
print ("="*100)

print ("Soal 2 : berapa sisa uang dari beli cupang dan koi?")
print ("="*100)
print ("penyelesaian:")
 
Jumlah_uang = int(input("masukkan jumlah uang yang dibawa:"))
harga_cupang = 10000
harga_koi = 20000

Jumlah_cupang = int(input("masukkan jumlah ikan yang akan dibeli:"))
Jumlah_koi = int(input("masukkan jumlah koi yang  akan dibeli:"))

total_harga = (Jumlah_cupang*harga_cupang) + (Jumlah_koi*harga_koi)
sisa_uang = Jumlah_uang - total_harga                      

print ("total belanja ikan (Rp) =", total_harga)
print ("sisa uang (Rp):", sisa_uang)
print ("="*100)

print ("soal 3 : perkiraan berapa kali mengisi bensin")
print ("="*100)
print ("penyelesaian:")

jarak = float(input("masukkan total jarak perjalanan (KM):"))
konsumsi =  float(input("masukkan konsumsi BBM sepeda motor (KM per liter):"))
kapasitas_tangki = float(input("masukkan kapasitas tangki motor (liter):"))
harga_bensin = float(input("masukkan harga bensin per liter (Rp):"))

bensin_dibutuhkan = jarak/konsumsi

if bensin_dibutuhkan > 3: 
    harga_diskon_bensin = harga_bensin - 500
else:
    harga_diskon_bensin = harga_bensin
total_biaya = harga_diskon_bensin*bensin_dibutuhkan

jumlah_isi_bensin = bensin_dibutuhkan/kapasitas_tangki

import math
isi_bensin =  math.ceil(bensin_dibutuhkan/kapasitas_tangki)

print (f"ntotal jarak perjalanan (KM) =), {jarak}")
print (f"kapasitas tangki (liter) =), {kapasitas_tangki}")
print (f"bensin dibutuhkan (liter) =), {round(bensin_dibutuhkan,2)}")
print (f"harga bensin per liter =, {harga_diskon_bensin}")
print (f"total biaya bensin (Rp) = {total_biaya}")
print (f"isi bensin sekitar = {isi_bensin} kali")