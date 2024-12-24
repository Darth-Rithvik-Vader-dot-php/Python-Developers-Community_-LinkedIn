## first example
# type matching - Buildin Types
a = 10
print isinstance(a, int)) # True
b = 10.1
print(isinstance(b, int)) # Flase

## second example
# Checks from tuple of types
# True only if one of the type is matched
a = {'k': ' value'}
print(isinstance(a, (dict, list))) #True
b = [1,2,3]
print (isinstance(b, (dict, list))) #True
c= 10
print(isinstance(c, (dict, list))) #False

## third example
# none type check
a = None
print (isinstance(a, type(None)))

## fourth example
# inheritance checks are done with isinstance
class A:
    pass

class B(A):
    pass

a = A()
b = B()
print(isinstance(a,A)) #True
print(isinstance(b,A)) #True
print (isinstance(a,B)) #False
