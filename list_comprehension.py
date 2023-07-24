# QUESTION - 1:
# List comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

"""
Beklenen çıktı:
['NUM_TOTAL',
'NUM_SPENDING',
'NUM_ALCOHOL',
'NUM_NOT_DISTRACTED',
'NUM_NO_PREVIOUS',
'NUM_INS_PREMIUM',
'NUM_INS_LOSSES'
'ABBREV']
"""


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM " + col.capitalize() if df[col].dtype != "O" else col.capitalize() for col in df.columns]
print(df.columns)


# QUESTION - 2:

# List comprehension yapısı kullanarak car_crashes verisinde isminde "no"
# barındırmayan değişkenlerin isimlerinin sonuna "FLAG" ekleyin ve değişkenlerin
# hepsi büyük harfle yazılsın.

"""
Beklenen çıktı:
['TOTAL_FLAG',
'SPEEDING_FLAG',
'ALCOHOL_FLAG',
'NOT_DISTRACTED',
'NO_PREVIOUS',
'INS_PREMIUM_FLAG',
'INS_LOSSES_FLAG',
'ABBREV_FLAG']
"""

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
print(df.columns)


# QUESTION - 3:

# List comprehension yapısı kullanarak aşağıda verilen değişken
# isimlerinden farklı olan değişkenlerin isimlerini seçiniz ve yeni
# bir dataframe oluşturunuz.
# og_list = ["abbrev", "no_previous"]

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
print(new_cols)

new_df = df[new_cols]

print(new_df.head(10))

