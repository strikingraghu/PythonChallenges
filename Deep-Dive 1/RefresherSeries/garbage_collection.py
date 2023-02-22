"""
Python’s memory allocation and deallocation method is automatic. The user does not have to preallocate or deallocate
memory similar to using dynamic memory allocation in languages such as C or C++.
Python uses two strategies for memory allocation: 

 - Reference counting
 - Garbage collection
"""

import ctypes
import gc

i = 0


def create_cycle():
    x = {}
    x[i + 1] = x
    print(x)


collected = gc.collect()
print("Garbage collector: collected %d objects." % collected)

print("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()
print("Garbage collector: collected %d objects." % collected)


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"


class A:
    def __init__(self):
        self.b = B()
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __int__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))


gc.disable()
my_var = A()
print(hex(id(my_var)))
print('a: \t{0}'.format(hex(id(my_var))))
print('a.b: \t{0}'.format(hex(id(my_var.b))))
print('b.a: \t{0}'.format(hex(id(my_var.b.a))))

a_id = id(my_var)
b_id = id(my_var.b)

print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

gc.collect()
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))
