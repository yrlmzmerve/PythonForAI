# Numpy Basics

import numpy as np

# Array Oluşturma
array = np.array([1,2,3,4,5,6,7,8])
print(array.shape)

a = array.reshape(2,4) # 2x4'lük array
print(a.shape)
print(a.ndim) # kaç boyutlu oldugunu bildirir


print("Data Type: ", a.dtype.name)
print("Size:", a.size)
print("Type:", type(a))

array1= np.array([[1,4],[2,5],[3,6]])
# 1 4
# 2 5 
# 3 6

# append() işlemi memoriyi yorar
# programın çalışmasını yavaşlatır
# liste.append(4)

zeros = np.zeros((3,4))
zeros[0,0] = 5

ones = np.ones((3,4))

# boş array oluşturma
np.empty((3,4))

# 10 dan basla 50 e kadar 5 er aralıklarla
a = np.arange(10,50,5) # 10, 15, 20, 25, 30, 35, 40, 45

# 10 dan baslayarak 50 dahil araya 20 tane sayı
# Her sayı aralığı eşit
a = np.linspace(10,50,20)

# %% Numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b) # [5 7 9]
print(a-b) # [-3 -3 -3]
print(a**2) # [1 4 9]

print(np.sin(a))

print(a<2) # [ True False False]


a = np.array([[1,2,3],[4,5,6]]) # 2x3 
b = np.array([[1,2,3],[4,5,6]])

# element wise product
print(a*b)
#  array([[ 1,  4,  9],
#        [16, 25, 36]])

# matrix product
# matrix carpımında;
#ilk matrixinsutun sayısı 
# ikinci matrizin satır sayısına eşit olmalıdır.
# orn: [2,4] * [4,5] gibi

print(b.T)
#array([[1, 4],
#       [2, 5],
 #      [3, 6]])


a.dot(b.T)
# array([[14, 32],
#       [32, 77]])

print(np.exp(a))

a = np.random.random((5,5)) # 0'la 1 aradında random sayılar

print(a.sum())
print(a.max())
print(a.min())


print(a.sum(axis=0)) # columları toplar
print(a.sum(axis=1)) # rowları toplar

print(np.sqrt(a)) # karakkökünü alır
print(np.square(a)) # a**2


print(np.add(a,a)) # a+a


# %% Indexing and slicing

import numpy as np
array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1

print(array[0]) # 1 

print(array[0:4]) # 1 2 3 4

#Arrayi ters çevirme
reverse_array = array[::-1]
print(reverse_array) # [7 6 5 4 3 2 1]


array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1]) # 7

#tüm satır ve istenen sutunu 
print(array1[:,1]) # 2 7


print(array1[1,1:4]) # [7 8 9]

#En son satırı alma
print(array1[-1,:]) # [ 6  7  8  9 10]

#En son sütunu alma
print(array1[:,-1]) # [ 5 10]

# %%
# Shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# flatten
a = array.ravel() # 3x3'lük arayı tek satırlık arraya cevirme
#  array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Tekrar 3x3'lük matrixe çevirme
array2 = a.reshape(3,3) # çevirir kaydetmez
# resize çevirir ve kaydeder

arrayT = array2.T
# array([[1, 4, 7],
#       [2, 5, 8],
#       [3, 6, 9]])

print(arrayT.shape) # (3,3)


array5 = np.array([[1,2],[3,4],[4,5]])
array5.resize((2,3))
# array([[1, 2, 3],
#       [4, 4, 5]])


# %% Stacking arrays

# iki arrayi birleştirme
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# veritical
#array([[1, 2],
#       [3, 4]])
#array([[-1, -2],
#       [-3, -4]])
array3 = np.vstack((array1,array2))

# horizontal
#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]

array4 = np.hstack((array1,array2))

#%% Convert and copy

liste = [1,2,3,4]   # list

# listeden arraye geçme
array = np.array(liste) #np.array

#Arrayden listeye geçme
liste2 = list(array)

# Copy
a = np.array([1,2,3])

b = a # a arrayıyle aynı yeri gösterir
b[0] = 5 # a'nın da c'nınde 0.elemanı değişir
c = a

d =  np.array([1,2,3])

e = d.copy() # yeni bir alan yaratır

f = d.copy()




















