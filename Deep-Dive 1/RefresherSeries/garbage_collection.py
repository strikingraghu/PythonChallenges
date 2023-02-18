"""
Python’s memory allocation and deallocation method is automatic. The user does not have to preallocate or deallocate memory similar to using dynamic memory allocation in languages such as C or C++. 
Python uses two strategies for memory allocation: 

 - Reference counting
 - Garbage collection
"""

import gc


def create_cycle():
    x = []
    for a in range(1,6):
        x.append(x)
        print(x, a)
        print(gc.get_threshold())
        collected = gc.collect()
        print("Garbage collector: collected", "%d objects." % collected)


create_cycle()
