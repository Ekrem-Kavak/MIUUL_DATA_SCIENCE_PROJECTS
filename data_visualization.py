############
# VERİ GÖRSELLEŞTİRME

# MATPLOTLIB

# Kategorik değişkenleri görselleştirme

# Kategorik değişkenlerde genelde sütun grafiği ya da pasta grafiği kullanılır.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

print(df.head())

# df["sex"].value_counts().plot(kind = "bar")
plt.show()

# Sayısal değişkenlerin gösterimi

# Sayısal değişkenlerde genelde histogram ve kutu grafiği kullanılır.

# plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

# MATPLOTLIB'IN ÖZELLİKLERİ

import numpy as np
import matplotlib.pyplot as plt


# plot


x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y, 'o') # o ile noktaları belirleriz.
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y, "o")
plt.show()

# marker

# işaretleyici olarak kullanılır.

y = np.array([13, 28, 11, 100])

plt.plot(y, marker = "o")
plt.show()

plt.plot(y, marker = "*")
plt.show()

plt.plot(y, marker = "+")
plt.show()

plt.plot(y, marker = "H")
plt.show()

# Yukarıdaki markerlar (işaretleyici) dışında da farklı markerler bulunmaktadır.

# Line (çizgi)

y = np.array([50, 100, 200, 400])
plt.plot(y)
plt.show()

# Farklı line (çizgi) tipleri de kullanabiliriz.

y = np.array([10, 20, 30, 40])
plt.plot(y, linestyle = "dashed") # çizgiler halinde
plt.show()

plt.plot(y, linestyle = "dotted") # noktalar halinde
plt.show()

plt.plot(y, linestyle = "dashdot") # nokta ve çizgiler halinde
plt.show()

# Çizgilere istersek renk özelliği de ekleyebiliriz.

plt.plot(y, linestyle = "dashed", color  = "y") # sarı renk
plt.show()

plt.plot(y, linestyle = "dashed", color = "g") # yeşil renk
plt.show()

# Multiple lines (çoklu çizgiler)

x = np.array([23, 18, 31, 10])
y = np.array([56, 23, 10, 75])

plt.plot(x)
plt.plot(y)
plt.show()

# Labels (etiketler)

x = np.array([23, 18, 31, 10])
y = np.array([56, 23, 10, 75])
plt.plot(x, y)

# Başlık ekleme
plt.title("BAŞLIK")

# X eksenini isimlendirme
plt.xlabel("X EKSENİ")

# Y eksenini isimlendirme
plt.ylabel("Y EKSENİ")

plt.grid()
plt.show()

# Subplots

# Çoklu grafikler oluşturabiliriz.

# plot 1

x = np.array([1, 3, 13, 25, 55, 100])
y = np.array([4, 8, 12, 23, 45, 77])
plt.subplot(1, 2, 1)
plt.title("1. GRAFİK")
plt.plot(x, y, color = "b")

# plot 2
x = np.array([4, 34, 56, 66, 100])
y = np.array([4, 8, 12, 77, 143])
plt.subplot(1, 2, 2)
plt.title("2. GRAFİK", color = "b")
plt.plot(x, y, color = "y")




