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
















