# NUMPY

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]


# Numpy kullanmadan iki listeyi çarpalım.

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

print(ab)

# Numpy kullanarak iki listeyi çarpalım.

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

ab = a * b
print(ab)

# NUMPY'IN AVANTAJLARI
# 1- Python dizilerine göre çok daha hızlıdır.
# 2- Üst düzey matematiksel operasyonları daha kolay yapmamıza imkan tanır.


# NumPy Array'i Oluşturmak

np.array([1, 2, 3, 4, 5])
print(type(np.array([1, 2, 3, 4, 5])))

print(np.zeros(10, dtype = int)) # Sıfırlardan oluşan array oluşturdu.
print(np.ones(7, dtype = int)) # Birlerden oluşan array oluşturdu.

print(np.random.normal(10, 4, (2,3)))
# Yukarıda ortalaması 10, standart sapması 4 olan 2 satır ve 3 sütunluk bir array oluşturduk.

# Numpy Array Özellikleri

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size = 5)

a= np.random.randint(10, size = 5)
print(a)

print(a.ndim) # 1
print(a.shape) # (5,)
print(a.size) # 5
print(a.dtype) # int32

b = np.random.randint(25, size = 10)
print(b)

print(b.ndim) # 1
print(b.shape) # (10,)
print(b.size) # 10
print(b.dtype) # int32

# Yeniden şekillendirme (reshaping)

print(np.random.randint(1, 20, size = 9))
# Yukarıdaki tek boyutlu arrayi 2 boyutlu 3,3'lük bir arraye çevirelim.

print(np.random.randint(1, 20, size = 9).reshape(3,3))

# Reshape işlemlerini atama yaparak kalıcı hale de getirebiliriz.

arr = np.random.randint(1, 15, size = 20)
print(arr)
print(arr.reshape(5,4))

# Index Seçimi

a = np.random.randint(10, size = 10)

print(a)
print(a[0])
print(a[7])

# slicing
print(a[2:5])
print(a[:10])
print(a[4:])

# index güncelleme

a[0] = 999
print(a)

# 2 boyutlu arraylerde seçim işlemleri

print("---")
m = np.random.randint(10, size = (3, 5))
print(m)

print(m[0, 0])
print(m[2, 3])
print(m[1,1])

m[1,1] = -10000
print(m)

print(m[:,2])
print(m[2:])
print(m[1:2,1:2])

# Fancy Index


v = np.arange(0, 30, 3) # 0'dan 30'a kadar 3'er 3'er yazdırılır.
print(v)

print(v[1])
print(v[2])
print(v[3])
# Fancy index ile yukarıdaki gibi birden fazla indeksi ayrıca yazdırmak
# yerine aynı anda yazdırabiliriz.

catch = [1, 2, 3]
print(v[catch])

# Numpy'da koşullu işlemler

v = np.array([1, 2, 3, 4, 5])

# Klasik döngü ile

ab = []

for i in v:
    if i < 3:
        ab.append(i)

print(ab) # [1, 2]


# Numpy ile

print(v < 3) # [True, True, False, False, False]
print(v[v < 3]) # [1, 2]

# Diğer işlemler

print(v[v > 3])
print(v[v == 3])
print(v[v != 3])
print(v[v >= 3])


# MATEMATİKSEL İŞLEMLER

print("---")
print(v / 5)
print(v * 5 / 2)
print(v // 2)
print(v ** 10)
print(v - 1)

print("Metotlar aracılığıyla")

print(np.subtract(v, 1)) # çıkarma işlemi
print(np.add(v, 1)) # toplama işlemi
print(np.mean(v)) # ortalama
print(np.sum(v)) # toplama
print(np.min(v)) # en küçük değer
print(np.max(v)) # en büyük değer
print(np.var(v)) # varyans

# Numpy ile iki bilinmeyenli denklem çözümü

print("SORU - 1")
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5,1], [1, 3]])
b = np.array([12, 10])

print(np.linalg.solve(a, b))

print("SORU - 2")

# S
# 3*x0 + x1 = 6
# 2*x0 + x1 = 10

x = np.array([[3, 1], [2, 1]])
y = [6, 10]

print(np.linalg.solve(x, y))

