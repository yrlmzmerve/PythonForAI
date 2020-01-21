# %% PANDAS

#Dataframeler için oluşturulmuş bir kütüphanedir

# Pandasın faydaları : 
# 1) Pandas,dataframeler için hizli ve etkili
# 2) csv ve text dosyalarına acip inceleyip sonucları bu dosya tiplerine rahat bir sekilde kaydedebilir.
# 3) Pandas, kayıp data (missin data) için isimizi kolaylastirir
# 4) reshape yapip datayi daha etkili bir sekilde kullanılır
# 5) Slicing indexing kolay -> 25 yasından buyuk kısılerı secmek gibi
# 6) time series data analizinde cok yardimci
# 7) Pandas hiz acisindan optimize edilmis hizli bir kutuphanedir

import pandas as pd

dictionary = {"NAME":["Berra","Merve","Büsra","Burak","Berat","Mustafa"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)


head = dataFrame1.head()
tail = dataFrame1.tail()

# %%
# Pandas Basic Method

print(dataFrame1.columns) # Sütunların isimlerini verir

print(dataFrame1.info()) # dataframe hakkında bilgi verir

print(dataFrame1.dtypes) # her sütunun type bilgisini verir

print(dataFrame1.describe())  # sayısal sutunların bilgisini verir
# numeric feature = columns (age,maas)

# %% Indexing and Slicing


print(dataFrame1["AGE"]) #asagıdakıyle aynı
print(dataFrame1.AGE) #yukarıdakıyle aynı

#Dataframe'e yeni sutun ekleme 
# sutun adı: yeni feature
# sutun degerleri : -1 ,-2, .. -6
dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.loc[:, "AGE"]) #♠ tüm satırları al, sadece AGE sütunundakileri

print(dataFrame1.loc[:3, "AGE"])

print(dataFrame1.loc[:3, "AGE":"NAME"])

print(dataFrame1.loc[:3, ["AGE","NAME"]])

#   AGE   NAME
#0   15  Berra
#1   16  Merve
#2   17  Busra
#3   33  Burak

print(dataFrame1.loc[::-1,:]) # satırları ters ceir, tüm sutunları al

#       NAME  AGE  MAAS
# 5  Mustafa   66   220
# 4    Berat   45   110
# 3    Burak   33   350
# 2    Büsra   17   240
# 1    Merve   16   150
# 0    Berra   15   100

print(dataFrame1.loc[:,:"NAME"])

#       NAME
# 0    Berra
# 1    Merve
# 2    Büsra
# 3    Burak
# 4    Berat
# 5  Mustafa

print(dataFrame1.loc[:,"NAME"])

#integer location / NAME 'in indexi yazılır
print(dataFrame1.iloc[:,0])

# 0      Berra
# 1      Merve
# 2      Büsra
# 3      Burak
# 4      Berat
# 5    Mustafa

# %% filtering

filtre1 = dataFrame1.MAAS > 200

filtrelenmis_data = dataFrame1[filtre1]

filtre2 = dataFrame1.AGE <20

dataFrame1[filtre1 & filtre2]

print(dataFrame1[dataFrame1.AGE > 60])

# %% List comprehension


import numpy as np

ortalama_maas = dataFrame1.MAAS.mean()

# ortalama_maas_np = np.mean(dataFrame1.MAAS)


dataFrame1["maas_seviyesi"] = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.MAAS]


#for each in dataFrame1.MAAS:
#    if(ortalama_maas > each):
#        print("dusuk")
#    else:
#        print("yukse")
        

dataFrame1.columns


dataFrame1.columns = [ each.lower() for each in dataFrame1.columns] # sutun ısımlerını kucuk harfler ile yaz

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] 
                      if(len(each.split())>1) 
                      else each 
                      for each in dataFrame1.columns]

# %% Drop and Concatenating

#axis=1 sutun drop etme
dataFrame1.drop(["yeni_feature"],axis=1,inplace = True)

# dataFrame1 = dataFrame1.drop(["yeni_feature"],axis=1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

# vertical - lt alta ekleme
data_concat = pd.concat([data1,data2],axis=0)

#     name  age  maas maas_seviyesi
# 0    Berra   15   100         dusuk
# 1    Merve   16   150         dusuk
# 2    Büsra   17   240        yuksek
# 3    Burak   33   350        yuksek
# 4    Berat   45   110         dusuk
# 1    Merve   16   150         dusuk
# 2    Büsra   17   240        yuksek
# 3    Burak   33   350        yuksek
# 4    Berat   45   110         dusuk
# 5  Mustafa   66   220        yuksek


# horizontal

maas = dataFrame1.maas
age = dataFrame1.age

#yan yana birleştirme
data_h_concat = pd.concat([maas,age],axis=1)
 
#    maas  age
# 0   100   15
# 1   150   16
# 2   240   17
# 3   350   33
# 4   110   45
# 5   220   66


# %% Transforming data

dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.age]

# apply()

def multiply(age):
    return age*2
    
dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)




