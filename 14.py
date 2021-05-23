from array import *
arr = array('i',[])

n = int(input("enter lenth of array."))
for i in range(n) :
    x= int(input("enter value."))
    arr.append(x)
print(arr)

#search for value.
val = int(input("enter a value for search."))
k=0
for e in  arr :
    if e==val :
        print(k)
    k+=1

#2nd method to search index

print(arr.index(val))