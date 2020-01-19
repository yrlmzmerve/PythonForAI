

# %% Variable

# Integer
var1 = 10
var2 = 15

# String
gun ="Pazartesi"

#Float & Double
var3=10.0


# %% String

s = "Bugün günlerden pazartesi"
variable_type=type(s) 
print(s)#str

var1="ankara"
var2="ist"
var3=var1+var2
print(var3) #ankaraist

var4="100"
var5="200"
print(var4+var5) #100200


uzunluk=len(var4+var5)
print(uzunluk) #6

var6=var4+var5
var6[0] # '1'

# %% Numbers

#♠int
int_den=-6

#double / float
float_den=-30.5

float(10) # 10.0

type(int_den)#int

# %% Functions

# 1. built in function
#Daha önceden tanımlanmış fonksiyonlardır.

str1="deneme"
len(str1) # 6
print(str1) # deneme
float(80) # 80.0
int(12.3) # 12

# 2. User default function
#kullanıcının tanımladığı fonk.lar

var1=12
var2=34
a = result(var1,var2)
print(a)     

def result(x,y):
    """
    açıklama eklenebilir
    """
    output= (x+y)*10/100
    return(output)


def deneme():
    print("Bye..")   
deneme()     
  
# 3. Default ve Flexible function

# Default func.
# çemberin çevresi = 2*pi*2
# değişmeyen değerler (pi)
def cember_cevresi(r,pi=3.14):
    output=2*pi*r
    return output
cember_cevresi(3)


# Flexible func.

# *arg = ektra parametre eklenebilir

def hesapla(boy,kilo, *args):
    print(len(args))
    output=boy+kilo
    print("arg",args[0])
    return output

hesapla(1,2,5,45,67)
#daha sonradan tanımlanan 5,45,67 değerleri args'da saklanır

# %% Exercise

#default degerler funcda ortaya yazılmaz
yas=4
name ="Berra"
soyisim = "Erdem"

def exercise(yas, name,*args, ayakkabino=36, ):
    print("İsim: {} , yas: {} , ayakkabı no {}".format(yas,name,ayakkabino))
    print("Yas tipi:",type(yas))
    print(float(yas))
    
    outp=args[0]*yas #"ErdemErdemErdemErdem"
    return outp
    
exercise(yas,name,soyisim)

# "abc"*2 = abcabc


# %% Lambda Function
#amaç daha hızlı funct yazmak
sonuc = lambda var1: var1**2
sonuc(8) #64

#%% List

liste = [2,4,6,8,10,12,14]
liste_str = ["ptesi","sali","cars"]
type(liste_str) #list

liste[1] #4
liste_str[-1] # cars
liste[0:3] # 2,4,6

dir(liste) # liste ile yapılabilecek fonk. sıralar
help(list.append) # append funk ne işe yaradıgı öğrenmek için

liste.append(7)
liste.reverse()
liste # 7,14,12,10,8,6,4,2

liste2=[9,3,5,8,12,1,7]
liste2.sort() #1, 3, 5, 7, 8, 9, 12
liste2

str_int_list=["a",",",5,6]



# %% Tuple

# listelere benzer
# normal parantez kullanılır ( )

t = (1,3,5,7,7,8,6)
t[2] #5
t.count(7) # 2 (7'den kaç tane var)
t.index(8) # 5 (8 elemanının indexini verir)

# %% Dictionary

# listelere benzer
# süslü parantez kullanılır
# 

dictionary={"Ali":32,"Arda":25, "Alp":24, "Oktay":24}
dictionary["Ali"] #32
dictionary.keys() #(['Ali', 'Arda', 'Alp', 'Oktay'])
dictionary.values() #32, 25, 24, 24

def deneme():
    dictionary={"Ali":32,"Arda":25, "Alp":24, "Oktay":24}
    return dictionary

dic = deneme()
type(dic) #dict
dic["Oktay"] #24

# %% Conditionals (if-else statement)

# if-else statements

var1=20
var2=10
if var1>var2:
    print("20, 10'dan büyüktür")
elif var1==var2:
    print("20, 10'a eşittir")
else:
    print("20, 10'dan küçüktür")
    
    
liste = [1,2,3,4,5]
if 6 in liste:
    print("6 elemanı vardır")
else:
    print("6 elemanı yoktur")
    

dictionary={"Ali":32,"Arda":25, "Alp":24, "Oktay":24}
values=dictionary.values()
keys=dictionary.keys()

if 24 in values:
    print("Evet")
else:
    print("Hayır")

# %% Exercise 

# Verilen yılların angi yy oldugu bulma uyg.
# 1649. yıl = 17.yy
# 109 = 2.yy
# 2020 >> yıl >> 1 
    
def year2Century(year):
    
    str_year = str(year)
    leng = len(str_year)

    if leng < 3:
        print("1.yy")
    elif leng==3:
        if(str_year[1:3]=="00"):
            print(int(str_year[0]))
        else:
            print(int(str_year[0])+1)
    else: # tek durum kaldı 
        if str_year[2:4]=="00":
            print(int(str_year[0:2]))
        else:
            print(int(str_year[0:2])+1)
        
    
yil = input("Yılı giriniz: ")
year2Century(yil)

# %% For loop
for each in range(1,11): # 1,2,3,..,10
    print(each) # 1,2,3,..10
    
for each in "ankaraist":
    print(each) # a n k a r a i s t

for each in "ankara ist".split():
    print(each) # ankara ist - boşluklara göre ayırır

list = [3,5,7,8,912,3,21]
sum(list) #959

count=0
for each in list:
    count+=each
print("Liste elemanlarının toplamı: ",count)

# %% While Loop

i=0
while(i<4):
    print(i)
    i+=1 # 0 1 2 3 4

liste = [1,2,3,4,5,6,7,8,9]
sinir = len(liste)
each = 0
count= 0
while(each < sinir):
    count+=liste[each]
    each+=1 # 0,1,2,..,9
print("Listenin toplamı : ",count)


# %% Exercise

# litedeki enküçük sayıyı bulma

min_val=0
liste=[23,67,90,84,31,15,-123,-987]

for each in liste:
    if(each<min_val):
        min_val=each
    else:
        continue
print(min_val)

#2.yol
min(liste) # -987
















