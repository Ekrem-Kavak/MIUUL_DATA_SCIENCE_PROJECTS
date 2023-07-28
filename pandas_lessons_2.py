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

