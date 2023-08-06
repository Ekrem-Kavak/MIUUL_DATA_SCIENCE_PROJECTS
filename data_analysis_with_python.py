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
df.isnull().sum().sum() # Toplam eksik değer sayısına ulaşırız

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
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int32", "int64", "float64"]]

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


# 3- SAYISAL DEĞİŞKEN ANALİZİ (Analysis of Numerical Variables)

df[["age", "fare"]].describe().T

# Değişkenler içinden sayısal olanları bulalım.
num_cols = [col for col in df.columns if df[col].dtypes in ["float64", "int64"]]

# Sayısal olup kategorik değişkene çevrilenleri çıkaralım.
num_cols = [col for col in num_cols if col not in cat_cols]

# Yukarıdaki özellikleri kullanarak fonksiyon oluşturalım.

def num_summary(dataframe, numerical_col):
        quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
        print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df, "age")

for col in num_cols:
    num_summary(df, col)

# Histogram kullanarak veriyi görselleştirelim.

def num_summary(dataframe, numerical_col, plot = False):
        quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
        print(dataframe[numerical_col].describe(quantiles).T)

        if plot:
            dataframe[numerical_col].hist()
            plt.xlabel(numerical_col)
            plt.title(numerical_col)
            plt.show(block = True)

num_summary(df, "age", plot = True)

# Tüm sayısal değişkenleri görselleştirelim.

for col in num_cols:
    num_summary(df, col, plot = True)


# 4- DEĞİŞKENLERİN YAKALANMASI VE İŞLEMLERİN GENELLEŞTİRİLMESİ

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()
df.info()

def grab_col_names(dataframe, cat_th = 10, car_th = 20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    "num_but_cat", "cat_cols"un içerisindedir.
    """

    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int32", "int64", "float64"]]
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["float64", "int32", "int64"]]

    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observation: {dataframe.shape[0]}") # gözlem sayısı
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

help(grab_col_names)

grab_col_names(df)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

# Kategorik değişken için oluşturduğumuz fonksiyon

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts()}))
    print("------")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)

def num_summary(dataframe, numerical_col, plot = False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)

for col in num_cols:
    num_summary(df, col, plot = True)


# Bool değerleri de int'e çevirip tüm kategorik değişkenleri görselleştirelim.

df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

def cat_summary(dataframe, col_name, plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
            "Ratio": 100 * dataframe[col_name].value_counts()}))
    print("---")

    if plot:
        sns.countplot(x = dataframe[col_name],data = dataframe)
        plt.show(block = True)

for col in cat_cols:
    cat_summary(df, col, plot = True)


# 4- Hedef Değişken Analizi (Analysis of Target Variable)

# Hedef değişken analizlerinde hedef değişken verideki önemli sorulara cevap verir.
# Örneğin, bu veri seti için titanik kazasında hayatta kalan kişileri bağlayan sebepler ve kriterler nedir.

# Bu veri seti için hayatta kalma oranı yani "survived" değişkeninin kategorik değişkenlerle ilişkisi ele alınabilir.

df["survived"].value_counts()
cat_summary(df, "survived")

# Cinsiyete göre hayatta kalma oranları
df.groupby("sex")["survived"].mean()

#  "Survived" değişkeninin diğer değişkenlerle ilişkisini gösteren bir fonksiyon yazalım.

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))

# sınıflara göre hayatta kalma oranları
target_summary_with_cat(df, "survived", "pclass")

# tüm değişkenlere uygulayalım.

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)


# "Survived" değişkenin sayısal değişkenlerle ilişkisine bakalım.
df.groupby("survived")["age"].mean()

# Sözlük içerisinde de gösterebiliriz.
df.groupby("survived").agg({"age":"mean"})

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end = "\n\n")


for col in num_cols:
    target_summary_with_num(df, "survived", col)

