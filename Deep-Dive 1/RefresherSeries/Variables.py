"""Code to explain details around Python variables"""

import sys
import ctypes

my_int = 10
my_string = 'hello, how are you?'
print("Var ID = ", id(my_int), "|", "Var Size = ", my_int.__sizeof__(), "|", "Hex Value = ", hex(id(my_int)))
print("Var ID = ", id(my_string), "|", "Var Size = ", my_string.__sizeof__(), "|", "Hex Value = ", hex(id(my_string)))

print(sys.getrefcount(my_int))
print(sys.getrefcount(my_string))
print(ctypes.c_long.from_address(id(my_int)).value)
