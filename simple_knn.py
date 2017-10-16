from sklearn.neighbors import KNeighborsClassifier

# membuat classifier dengan menggunakan algoritma nearest neighbors
# dengan jumlah tetangga = 3
clf = KNeighborsClassifier(n_neighbors = 3)


# variable data dengan isi array sebagai berikut:
# [jumlah masuk parkiran dalam sehari, index jenis mobil, level bau ketek supir range (1 - 10), umur supir]
#
# index jenis_mobil
# 0. toyota avanza
# 1. roll royce
# 2. suzuki ertiga
# 3. hino truck
# 4. daihatsu ayla
data = [[5, 0, 3, 45], [4, 4, 5, 35], [3, 3, 6, 40], [1, 0, 1, 23], 
       [1, 4, 1, 35], [1, 1, 0, 45], [2, 1, 0, 35], [7, 4, 5, 25],
       [2, 0, 1, 26], [6, 4, 5, 38], [4, 2, 5, 35], [3, 2, 3, 30]]

# variable target dari data-data di atas
#
# index target value
# 0 = taxi online
# 1 = mobil biasa
target = [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0]

# train data di atas
clf.fit(data, target)

# prediksi data berdasarkan input kita
input_jumlah_masuk_parkir = 4
input_jenis_mobil = 0
input_level_bau_ketek = 5
input_umur_supir = 40

# membuat prediksi
prediksi = clf.predict([[input_jumlah_masuk_parkir, input_jenis_mobil, input_level_bau_ketek, input_umur_supir]])

# mencetak prediksi
target_prediksi = ["taxi online", "mobil biasa"]
print(target_prediksi[int(prediksi)])