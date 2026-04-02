# Booleans
# Showing True or False
print(5 > 4)
print(5 == 4)
print(5 < 4)

a = 200
b = 10

if b > a :
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hallo"))
print(bool(""))
print(bool(10))
print(bool(0))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def Func():
    return True

print(Func())

def Func1():
    return True

if Func1():
    print("Yes")
else:
    print("No")

x = 200
print(isinstance(x, int))