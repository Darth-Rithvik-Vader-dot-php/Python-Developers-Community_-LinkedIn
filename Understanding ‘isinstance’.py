# type matching - Buildin Types
a = 10
print isinstance(a, int)) # True
b = 10.1
print(isinstance(b, int)) # Flase
1
# Checks from tuple of types
2
# True only if one of the type is matched
3
a = {'k': ' value'}
4 print(isinstance(a, (dict, list))) #True
5
b = [1,2,31
6
print (isinstance(b, (dict, list))) #True
7
c= 10
8
print(isinstance(c, (dict, list))) #False
1
# none type check
2
a = None
3
print (isinstance(a, type(None)))
1 # inheritance checks are done with isinstance
2 class A:
3
pass
4
5
class B(A):
6
pass
7
8
a = A()
9
10
print(isinstance(a,A)) #True
11
print(isinstance(b,A)) #True
12
print (isinstance(a,B)) #False
