# Looping options in Python language


generic_list = [1, 2, 3]
print("Generic List (Before while loop execution): ", generic_list)
print("Length of the Generic List provided in this code: ", len(generic_list))
search_value = 4
element_index = 0
while element_index < len(generic_list):
    if generic_list[element_index] == search_value:
        break
    element_index += 1
else:
    generic_list.append(search_value)
print("Generic List (After while loop execution): ", generic_list)
