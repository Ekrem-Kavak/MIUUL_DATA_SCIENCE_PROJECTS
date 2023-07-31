# PANDAS (PART - 2)

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")

print(df.head())

# Toplulaştırma & Gruplaştırma (Aggregation & Grouping)

# Bireylerin yaş ortalaması
print(df["age"].mean())

# Cinsiyete göre yaş ortalaması

print(df.groupby("sex")["age"].mean())

# Bir değişkenin türlerinin farklı özelliklerini listelemek için dict() veri tipi kullanılır.

print(df.groupby("sex").agg({"age": ["mean", "sum"]}))

# Cinsiyete göre yaş bilgisinin ortalamasını ve toplamını; hayatta kalma bilgisinin
# ortalamasını alalım.

print(df.groupby("sex").agg({"age" : ["mean", "sum"],
                             "survived": ["mean"]}))

# İki seviyeli groupby örneği

print(df.groupby(["sex", "embark_town"]).agg({"age":["mean"],
                 "survived":"mean"}))

# Üç seviyeli groupby örneği

print(df.groupby(["sex", "embark_town", "class"]).agg({"age":["mean"],
                 "survived":"mean"}))

print(df.groupby(["sex","embark_town","class"]).agg({
        "age": ["mean"],
        "survived" : ["mean"],
        "sex": ["count"]
}))


# PIVOT TABLE

# pivot table ön tanımlı olarak ortalama (mean) alır.

print(df.pivot_table("survived", "sex", "embarked"))

# ortalama yerine standart sapma
print(df.pivot_table("survived", "sex", "embarked", aggfunc = "std"))

# İki boyutlu pivot table
print(df.pivot_table("survived","sex",["embarked","class"]))

# Yaş değişkenin verilere etkisi

# cut metodu sayısal değişkenleri kategorik değişkene çevirmenin bir yoludur.
# Tam olarak bilmediğimiz sayısal değişkenler için de qcut kullanılır.
# Bu metot değerleri çeyreklik değerlere ayrılır.

# Yaş için yeni bir değişken atadık ve cut ile bölümlendirdik.
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
print(df.head())

# yeni değişkeni pivot table içinde değerlendirelim.

print("  ")
print(df.pivot_table("survived", "sex", "new_age"))
print(" ")

# print(df.pivot_table("survived", "sex", ["new_age", "class"]))

# Tabloyu yan yana görmek için
print(pd.set_option("display.width", 500))
print(df.pivot_table("survived", "sex", ["new_age", "class"]))

# APPLY & LAMBDA

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

# age içeren değişkenlerin 10'a bölümü (ayrı ayrı)
print((df["age"]/10).head())
print((df["age2"]/10).head())
print((df["age3"]/10).head())

# For döngüsü ile

df.drop("new_age", axis=1, inplace = True) # kategorik olan değişkeni sildik.

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

print(df.head())

# apply & lambda kullanarak

# 1.yol
print(df[["age", "age2", "age3"]].apply(lambda x: x/10).head())

# 2.yol
print(df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head())

# Age içeren değerleri normalize edelim (standartlaştırma)

print("-------")
print(df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head())

# Yukarıdaki işlemi fonksiyon aracılığıyla lambda kullanmadan yapalım.

print("-----")
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

print(df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head())

# Yaptığımız normalleştirme işlemini kaydedelim.

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
print(df.head())

# BİRLEŞTİRME (JOIN) İŞLEMİ

# 1- CONCAT ile

import numpy as np

m = np.random.randint(1, 30, size = (5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

print(pd.concat([df1, df2]))

# İndekslerin sırasıyla yazılması için "ignore_index = True" eklenir.

print(pd.concat([df1, df2], ignore_index = True))

# concat metodu ön tanımlı olarak alt alta birleştirir. axis = 1 yaparak yan yana çevrilir.

print(pd.concat([df1, df2], ignore_index = True, axis = 1))

# 2- MERGE ile

df1 = pd.DataFrame({"employees": ["John", "Dennis", "Mark", "Maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees" : ["Mark", "John", "Dennis", "Maria" ],
                    "start_date": [2010, 2009, 2014, 2019]})

print(pd.merge(df1, df2))
print("  ")

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

print(pd.merge(df3, df4))


import pandas as pd
import numpy as np

df = pd.DataFrame(data = np.random.randint(1,10, size = (2, 3)),
                  columns = ["var1", "var2", "var3"])

df[(df.var1 <= 5)][["var2", "var3"]]

