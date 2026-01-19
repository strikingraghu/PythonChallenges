# Taking input in Python for learning purposes!

name = input("Enter your name: ")
print("Hello, have a great day, " + name + "!")

# Example of formatted string (f-string)
person = "Angelina"
age = 25
city = "Bengaluru"
print(f"{person} is {age} years old and lives in {city}.")

# Taking mulple inputs in a single line
name, age = input("Enter your name and age: ").split()
print("Entered Name: ", name)
print("Entered Age: ", age)

# Print the input values
flower_color = input("What is the color of the Rose flower? ")
print(flower_color)
