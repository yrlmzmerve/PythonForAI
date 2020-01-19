# %% Class ve Constructor

class Employee:
    
    zam_orani=1.5
    counter=0
    
    #contructor
    def __init__(self, isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@gmail.com"
        Employee.counter = Employee.counter+1
        
    def giveNameSurname(self):
        return self.isim+" "+self.soyisim
    
    def zamYap(self):
        self.maas=self.maas*self.zam_orani
        
        
employee_1=Employee("Berra","Erdem",3000) #1
print(employee_1.giveNameSurname()) # Berra Erdem
print("ilk maas: ",employee_1.maas) #3000
employee_1.zamYap() 
print("zamli maas: ",employee_1.maas) #4500


print(employee_1.counter)
employee_2=Employee("Merve","Y",4500)
print(employee_2.counter) #2


employee_3=Employee("Büşra","Akcadag",4000)
employee_4=Employee("Esila","Güclü",2700)
employee_5=Employee("Gül","Tokdemir",10500)


liste = [employee_1,employee_2,employee_3, employee_4, employee_5]
max_maas=-1
index=-1
for each in liste:
    if each.maas > max_maas:
        max_maas=each.maas
        isim=each.isim
        soyisim=each.soyisim
        index=each # indexi tutar
print("En yüksek maaş alan: ",isim+" "+soyisim)























