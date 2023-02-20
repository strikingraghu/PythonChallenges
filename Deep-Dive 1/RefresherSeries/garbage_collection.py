"""
Python’s memory allocation and deallocation method is automatic. The user does not have to preallocate or deallocate memory similar to using dynamic memory allocation in languages such as C or C++. 
Python uses two strategies for memory allocation: 

 - Reference counting
 - Garbage collection
"""

import ctypes
import gc
i = 0


def create_cycle():
    x = {}
    x[i+1] = x
    print(x)

collected = gc.collect()
print("Garbage collector: collected %d objects." % (collected))

print ("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()
print("Garbage collector: collected %d objects." % (collected))



def ref_count(address):
    return ctypes.c_long.from_address(address).value



def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"