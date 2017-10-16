# import algoritma logistic regression pada scikit learn
from sklearn.linear_model import LogisticRegression

# membuat variable classifier dengan algoritma logistic regression
clf = LogisticRegression()

# properti yang dibutuhkan pada aplikasi ini mempunyai sebuah array dengan value sebagai berikut
# index 0 : Jarak rumah dalam KM
# index 1 : Level bau ketek (1 - 10)
# index 2 : Jenis kendaraan denga properti 0 = angkot, 1 = motor, 2 = mobil
# index 3 : Pengeluaran saat PDKT
# index 4 : Jumlah ketemuan dalam seminggu [dalam puluh ribu]
data = [[5, 1, 0, 5, 1], [35, 6, 2, 8, 4], [1, 4, 0, 11, 1], [23, 3, 1, 3, 3], [54, 1, 0, 80, 5], 
        [16, 3, 1, 6, 3], [7, 3, 2, 10, 2], [4, 7, 1, 12, 2], [10, 2, 1, 5, 2], [8, 2, 0, 40, 3], 
        [3, 5, 0, 7, 2], [18, 2, 1, 150, 3], [6, 4, 1, 2, 4], [23, 1, 2, 6, 1], [17, 1, 1, 20, 2]]

# target berdasarkan data diatas adalah sebagai berikut
# value 0 : diterima
# value 1 : ditolak
target = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]

# target value
target_value = ["Aku mau kok jadi pacar kamu", "Kita temenan aja ya!"]

# mentrain data berdasarkan properti diatas
clf.fit(data, target)

# membuat prediksi dari cowok kere
prediction = clf.predict([[23, 1, 2, 6, 1]])

# memperint dari prediksi
print target_value[int(prediction)]