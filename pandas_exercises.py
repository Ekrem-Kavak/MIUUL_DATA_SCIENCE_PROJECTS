# PANDAS EXERCISES

# 1- Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

# 2- Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df["sex"].value_counts() # 577 kadın, 314 erkek

# 3- Her bir sütuna ait unique değerlerin sayısını bulunuz.

df.nunique()

# 4- pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].nunique() # 3

# 5- pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df["pclass"].unique() # 3, 1, 2
df["parch"].unique() # 0, 1, 2, 3, 4, 5, 6

# 6- embarked değişkenini kontrol ediniz ve tipini "category" olarak değiştiriniz.

df["embarked"].dtype # Object
df["embarked"] = df["embarked"].astype("category")

# 7- embarked değeri C olanların tüm bilgilerini gösteriniz.

df[df.embarked == "C"]

# 8- embarked değeri S olmayanların tüm bilgilerini gösteriniz.

df[df.embarked != "S"]

# 9- Yaşı 30'Dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df.age < 30) & (df.sex == "female")]

# 10- "fare"i 500'den büyük veya yaşı 70'den büyük yolcuların bilgisini gösteriniz.

df[(df.fare > 500) | (df.age > 70)]

# 11- Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

# 12- "who" değişkenini dataframe'den çıkarınız.

df.drop("who", axis = 1) # kalıcı olması için inplace = True

# 13- "deck" değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri(mode)
# ile doldurunuz.

df.deck.fillna(value = df.deck.mode()[0]) # 0 sayesinde birden fazla mod değeri varsa ilkini alır.

# 14- "age" değişkenindeki boş değerleri "age" değişkenin medyanı ile doldurunuz.

df.age.fillna(value = df.age.median())

# 15- "survived" değişkeninin pclass ve cinsiyet değişkenleri kırılımındaki
# sum, count, mean değerlerini bulunuz.

df.groupby(["pclass", "sex"])["survived"].agg(["sum", "count", "mean"])

# 16- 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonkisyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz.

df["age_flag"] = df["age"].apply(lambda age: 1 if age < 30 else 0)

# 17- Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("tips")

# 18- Time değişkeninin kategorilerine (dinner, lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["time"])["total_bill"].agg(["sum", "min", "max", "mean"])

# 19- Günlere ve time değişkenine göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["time", "day"])["total_bill"].agg(["sum", "min","max", "mean"])

# 20- "Lunch" zamanına ve kadın müşterilerine ait total_bill ve tip değerlerinin "day"e göre toplamını, min, max ve ortalamasını bulunuz.

filtered = df[(df["time"] == "Lunch") & (df["sex"] == "Female")]

filtered.groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"]
})

# 21- Size'i 3'ten küçük, total_bill'i 10'dan büyük siparişlerin ortalaması nedir? (loc)

mean_filter = df.loc[(df["size"] < 3) & (df["total_bill"] > 10)]

mean_filter["total_bill"].mean()

# 22- total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin
# ödediği total_bill ve tip değerlerinin toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]


# 23- total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız.
# İlk 30 kişiyi yeni bir dataframe'e atayınız.

df["total_bill_tip_sum"].value_counts().sort_index(ascending = False)
new_df = df.sort_values("total_bill_tip_sum", ascending = False).head(30)
new_df
