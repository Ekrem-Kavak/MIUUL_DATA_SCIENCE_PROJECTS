# GELİŞMİŞ FONKİSYONEL KEŞİFÇİ VERİ ANALİZİ

# 1- Genel Resim
# 2- Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3- Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4- Hedef Değişken Analizi (Analysis of Target Variable)
# 5- Korelasyon Analizi (Analysis of Correlation)

# 1- GENEL RESİM

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

df.head() # ilk 5 satırı listeler
df.tail() # son 5 satırı listeler
df.shape # satır ve sütun sayısı (891, 15)
df.info() # değişkenlerle ilgili bilgiler
df.columns # değişken isimleri
df.index # RangeIndex(start = 0, stop = 891, step = 1)
df.describe().T # bazı istatistikleri verir
df.isnull().values.any() # Null değerinin olup olmadığını söyler
df.isnull().sum() # her değişkende kaç null değer olduğunu söyler

def check_df(dataframe, head = 5):
    print("------- Shape ---------")
    print(dataframe.shape)
    print("-------- Types --------")
    print(dataframe.dtypes)
    print("--------- Head --------")
    print(dataframe.head(head))
    print("--------- Tail -------- ")
    print(dataframe.tail(head))
    print("--------- NA ---------- ")
    print(dataframe.isnull().sum())
    print("------- Quantiles -----")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

# 2- KATEGORİK DEĞİŞKEN ANALİZİ (Analysis of Categorical Variables)

df["embarked"].value_counts() # "embarked" değişkeni içindeki bileşenlerin sayısı
df["sex"].unique() # "sex" değişkeni içindeki tekil değerler
df["class"].nunique() # "class" değişkeni içindeki tekil bileşen sayısı

# Kaç tane kategorik değişken olduğunu bulalım.
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# 10 daha az bileşeni olan sayısal değişkenleri kategorik değişkene çevirdik.
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

# Kategorik olup bileşeni (sınıfı) 20'den fazla olanları gözlemleyelim. Bileşenlerin 20'den fazla olması
# verinin bilgi vermesi açısından faydasız görülebilir.
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

# Kategorik değişkenler ve kategorik değişkene dönüşen numerik değişkenleri
# aynı liste içine alalım.
cat_cols = cat_cols + num_but_cat

# cat_but_num içindeki faydasız kategorik değişkenleri çıkaralım.
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

# kategorik olmayan değişkenler
[col for col in df.columns if col not in cat_cols]

# Değişkenlere göre değer sayısı ve oranlarını gösteren bir fonksiyon oluşturalım.

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print(" --- ")

cat_summary(df, "sex")
cat_summary(df, "class")

# Fonksiyon sayesinde tüm kategorik değişkenlerin sayısını ve oranını bulacağız.

for col in cat_cols:
    cat_summary(df, col)

# Kategorik değişkenleri aynı zamanda countplot ile görselleştirelim.

def cat_summary(dataframe, col_name, plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
          "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("-------")

    if plot:
        sns.countplot(x = dataframe[col_name], data = dataframe)
        plt.show(block = True)


cat_summary(df, "sex", plot = True)
cat_summary(df, "sibsp", plot = True)

# Yukarıdaki fonksiyonu tüm değişkenlere uygulayalım.
# "bool" değerler countplot üzerinde çalışmadığı için bool tipindekileri eklemedik.

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("bool değeri")
    else:
        cat_summary(df, col, plot = True)

# bool tipinde olanları integer'a çevirelim.

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot = True)
    else:
        cat_summary(df, col, plot = True)






