from icecream import ic

def myfunction(value):
    if value % 2 == 0:
        ic()   #IC returns more information from an execution
        return True
    else:
        ic()   #IC returns more information from an execution
        return False
    
print(myfunction(10))
print(myfunction(11))
print(myfunction(12))

ic.disable()

print(myfunction(10))
print(myfunction(11))
print(myfunction(12))

ic.enable()

print(myfunction(10))
print(myfunction(11))
print(myfunction(12))