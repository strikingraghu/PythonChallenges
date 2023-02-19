"""
Python’s memory allocation and deallocation method is automatic. The user does not have to preallocate or deallocate memory similar to using dynamic memory allocation in languages such as C or C++. 
Python uses two strategies for memory allocation: 

 - Reference counting
 - Garbage collection
"""

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
