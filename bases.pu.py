class otherdata2:
    pass

class otherdata:
    email =''
    phone =''
    
    
class person:
    name = ''
    address = ''
    
class employee(otherdata,person,otherdata2):
    employeeid = 0
    

class doctor (employee):
    pass
print(otherdata.__bases__)
print(".................")
print(person.__bases__)
print(".................")
print(employee.__bases__)
print(".................")
print(doctor.__bases__)


b


