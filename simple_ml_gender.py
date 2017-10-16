from sklearn import tree

# variable classifier dan import decision tree
clf = tree.DecisionTreeClassifier()

# variable berisi data tinggi, berat dan nomor sepatu [tinggi, berat, nomor sepatu]
human_data = [[180, 60, 45], [150, 46, 25], [150, 46, 30], 
[175, 60, 40], [170, 60, 35], [160, 50, 45], [200, 50, 23], 
[130, 50, 25]]

# variable yang menunjukan gender pada variable human_data
gender = ['man', 'woman', 'woman', 'man', 'man', 'woman', 'man', 'woman']

# selanjutnya adalah mentrain data-data diatas
clf = clf.fit(human_data, gender)

# lalu prediksi gender dari data yang di input
tinggi= 160
berat = 55
ukuran_sepatu = 36

prediction = clf.predict([[tinggi, berat, ukuran_sepatu]])

# lalu print hasilnya
print(prediction)