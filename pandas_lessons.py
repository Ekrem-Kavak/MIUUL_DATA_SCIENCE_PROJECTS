# PANDAS
##########

# PANDAS SERIES

import pandas as pd

print(pd.Series([10, 34, 24, 100]))

s = pd.Series([1, 2, 3, 4, 5])
print(s)

print(type(s)) # 'pandas.core.series.Series'
print(s.index) # RangeIndex(start = 0, stop = 5, step = 1)
print(s.dtype) # int64
print(s.size) # 5
print(s.ndim) # 1
print(s.values) # [1, 2, 3, 4, 5]
print(type(s.values)) # <class 'numpy.ndarray'>

# values metodu ile pandas serilerini elemanlarına ulaşmak istediğimizde
# bu değerler array şeklinde gösterilecektir.

print(s.head(3)) # ilk 3 elemanı listeler.
print(s.tail(3)) # son 3 elemanı listeler.

# Pandas ile veri okuma (reading data)

# df = pd.read_csv("herhangi bir dosya ismi.cvs")
# df.head()

# Verilere hızlı bakış

import seaborn as sns

df = sns.load_dataset("titanic")
df.head(3) # İlk 3 satırı gösterir.
print("--")
df.tail(5) # Son 3 satırı gösterir.
print("---")

print(df.shape) # (891, 15) 891 satır ve 15 sütundan oluşur.
print(df.info()) # Pandas tablosu hakkındaki genel özellikleri listeler.
print(df.columns) # sütun isimlerini listeler.
print(df.index) # RangeIndex(start = 0, stop = 891, step = 1)

print(df.describe().T) # Tablo hakkındaki detaylı bilgileri listeler.
print(df.isnull().values.any()) # True (Eksik değerler varsa True döndürür.)
print(df.isnull().sum()) # Her bir sütundaki değişkenlerin kaç adet eksik bilgiye
# sahip olduğunu gösterir.
print(df["sex"].head(3)) # Seçilen değişkenin ilk 3 değerini verir.
print(df["sex"].value_counts()) # Kadın ve erkek sayısını verir.

# Pandas'ta seçim işlemleri (Selection in Pandas)

df = sns.load_dataset("titanic")
print(df.head())

print(df[0:13]) # İlk 13 değeri listeler.

# Dataframe üzerinde bulunan verileri silmek

print(df.drop(2, axis=0).head()) # 2. indeksi sildik.

delete_index = [1, 3, 5, 7]
print(df.drop(delete_index, axis=0).head()) # 1,3,5,7. indeksi sildik.

# axis = 0 satırları; axis = 1 sütunları siler.

# Verileri kalıcı yapmak için inplace = True parametresi eklenir.

# print(df.drop(delete_index, axis=0, inplace = 0).head())

# DEĞİŞKENİ INDEKSE ÇEVİRMEK (SÜTUNDAN SATIRA)

print(df["age"].head())

df.index = df["age"]

print(df.drop("age", axis = 1).head())

# işlemi kalıcı yapalım
print(df.drop("age", axis = 1, inplace= True))
print(df)

# INDEKSİ DEĞİŞKENE ÇEVİRMEK (SATIRDAN SÜTUNA)

# 1. yol

df["age"] = df.index
print(df.head)

# Age değişkenini indeksten silelim.
df.drop("age", axis = 1, inplace=True)
print(df.head)

# 2.yol
df = df.reset_index().head()
print(df)


# DEĞİŞKENLER ÜZERİNDE İŞLEMLER

pd.set_option('display.max_columns', None) # Dataframe üzerindeki tüm değişkenleri gösterir.
df = sns.load_dataset("titanic")
print(df)

print("age" in df) # True

print(df["age"].head())
print(df.age.head())

# df["age"].head() = df.age.head()

