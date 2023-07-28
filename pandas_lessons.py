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
df.tail(3) # Son 3 satırı gösterir.
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

print(type(df["age"].head())) # pandas.core.series.Series

print(type(df[["age"]].head())) # pandas.frame.DataFrame

# Eğer bir değişkeni [] ile seçersek türü series; [[]] ile seçersek türü
# DataFrame olur.

print(df[["age", "alive"]])

col_names = ["age", "adult_male", "alive"]
print(df[col_names])

# Yeni değişken oluşturma

df["age2"] = df["age"] ** 2
df["age3"] = df["age"] / df["age2"]

print(df.head())

# Eklediğimiz değişkenleri silme

df.drop("age3", axis=1, inplace=True)
print(df.head())

# Liste içindeki verileri silme

print(df.drop(col_names, axis=1).head())

print(df.head())

# Belirli koşulları sağlayan değişkenleri listeleme ve silme

print(df.loc[:, df.columns.str.contains("age")].head())
# Sadece "age" içeren değişkenleri listeledik.

print(df.loc[:, ~df.columns.str.contains("age")].head())
# "age" içermeyen tüm değişkenleri listeledik.

# LOC & ILOC

# iloc: integer based selection

print(df.iloc[0:3]) # ilk 3 indeksi listeler.
print(df.iloc[1:5, 2:5]) # 1. indeksten 5. indekse; 2. değişkenden 5. değişkene kadar listeler.

# loc: label based selection

print("---")
print(df.loc[0:3, "age"]) # 3. indekse kadar age değişkeni verileri listelenir.

col_names = ["age","embarked","alive"]
print(df.loc[0:3, col_names])

# Koşullu seçim (conditional selection)

print(df[df["age"] > 50].head())
print(df[df["age"] > 50]["age"].count())
print("---")

# Yaşı 50'den büyük olan kişilerin age ve class bilgilerini listele
print(df.loc[df["age"] > 50, ["age", "class"]].head())

# Yaşı 50'den büyük ve erkek olan kişilerin age ve class bilgilerini listele.
print(df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head())

# Yaşı 50'den büyük, erkek ve Cherbourg'da oturan kişilerin age, class, embark_town bilgileri

print(df.loc[(df["age"] > 50) &
(df["sex"] == "male") &
(df["embark_town"] == "Cherbourg"),
 ["age", "sex", "embark_town"]].head())

# Yaşı 50'den büyük, erkek ve Cherbourg'da ya da Southampton'da oturan kişilerin age, class, embark_town bilgileri

new_df = df.loc[(df["age"] > 50) &
(df["sex"] == "male") &
((df["embark_town"] == "Cherbourg") | (df["embark_town"] == ["Southampton"])),
 ["age", "sex", "embark_town"]]

# print(new_df)
# print(new_df["embark_town"].value_counts())

