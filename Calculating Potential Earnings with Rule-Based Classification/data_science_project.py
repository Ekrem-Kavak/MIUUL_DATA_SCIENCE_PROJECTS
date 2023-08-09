# KURAL TABANLI SINIFLANDIRMA İLE POTANSİYEL MÜŞTERİ GETİRİSİ HESAPLAMA

"""
Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı
(level based) yeni müşteri tanımları oluşturmak ve bu yeni müşteri tanımlarına
göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
şirkete ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

"persona.csv" veri seti uluslarası bir oyun şirketinin sattığı ürünlerin fiyatlarını
ve bu ürünleri satın alan kullancıların bazı demografik bilgilerini barındırmaktadır.
Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
tablo tekilleştirilmemiştir. Diğer bir ifade ile demografik özelliklere sahip
bir kullanıcı birden fazla alışveriş yapmış olabilir.

Değişkenler
price - müşterinin harcama tutarı
source - müşterinin bağlandığı cihaz türü
sex - müşterinin cinsiyeti
country - müşterinin ülkesi
age - müşterinin yaşı
"""

# GÖREV - 1

# 1- persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import numpy as np
import pandas as pd

df = pd.read_csv("persona.csv")
print(df)

print(df.describe())

# 2- Kaç unique "SOURCE" vardır? Frekansları nedir?

print(df["SOURCE"].nunique()) # 2
print(df["SOURCE"].unique()) # ["android", "ios"]
print(df["SOURCE"].value_counts())

# 3- Kaç unique "PRICE" vardır?

print(df["PRICE"].nunique()) # 6

# 4- Hangi "PRICE"dan kaçar tane satış gerçekleşmiştir?

print(df["PRICE"].value_counts())

# 5- Hangi ülkeden kaçar tane satış olmuştur?

print(df["COUNTRY"].value_counts())

# 6- Ülkelere göre satışlardan toplam ne kadar kazanılmış?

print(df.groupby("COUNTRY").agg({"PRICE": "mean"}))

# 7- "SOURCE" türlerine göre satış sayıları nedir?

print(df["SOURCE"].value_counts())

# 8- Ülkelere göre "PRICE" ortalamaları nedir?

print(df.groupby("COUNTRY")["PRICE"].mean())

# 9- "SOURCE"lara göre PRICE ortalamaları nedir?

# 1. YOL
print(df.groupby("SOURCE")["PRICE"].mean())
# 2. YOL
print(df.groupby("SOURCE").agg({"PRICE": "mean"}))

# 10- COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

print(df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE": "mean"}))

# GÖREV - 2

# "COUNTRY", "SOURCE", "SEX", "AGE" kırılımında ortalama kazançlar nedir?

print(df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}))

# GÖREV - 3

# Yukarıdaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde
# sıralayınız ve çıktıyı "ag_df" olarak kaydediniz.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values(by ="PRICE", ascending= False)
print(agg_df)

# GÖREV - 4

# Indekste yer alan isimleri değişken ismine çeviriniz.

agg_df = agg_df.reset_index()
print(agg_df)

# GÖREV - 5

# Age değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz. (AGE_CAT)

intervals = [0, 10, 20, 30, 40, 50]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins = intervals, labels= ["0_10", "11_20", "21_30", "31_40", "41_50"])
print(agg_df)


# GÖREV - 6

# Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturun.

agg_df["customers_level_based"] = df["COUNTRY"] + "_" + df["SOURCE"] + "_" + df["SEX"]
print(agg_df)

# GÖREV - 7

# Yeni müşterileri PRICE'a göre 4 segmente ayırınız.
# Segmentleri "segment" isimlendirmesi ile değişken olarak agg_df'e ekleyiniz.
# Segmentlere göre mean, max, min özelliklerine bakınız.

segment = pd.qcut(agg_df["PRICE"], 4, labels = ["A", "B", "C", "D"])
print(segment)
agg_df["SEGMENT"] = segment
print(agg_df)
print(agg_df.groupby("SEGMENT").agg({"PRICE": ["mean","max","min","sum"]}))

# GÖREV - 8

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]


