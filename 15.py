# for integer values

from array import *

val= array('i',[10,23,34,56,45])
print(val)
print(val.buffer_info())
print(val.typecode)
print(val.append(1))
print(val)

for e in val :
    print(e)


newarr = array(val.typecode, (a*a for a in val))
print(newarr)