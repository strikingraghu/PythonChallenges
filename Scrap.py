def calculate_hours():
    print()

    incoming_values = [int(x) for x in (input("Enter any 2 numbers: ").split())]
    if len(incoming_values) <= 1:
        print("Please enter 2 integers")
    if len(incoming_values) == 2:
        print("Thanks, you have entered correct values")
    else:
        print("Don't enter more than 2 integers")

    total_sum = incoming_values[0] + incoming_values[1]
    if total_sum < 12:
        print("Results: ", total_sum)
    elif total_sum >= 12:
        result = total_sum % 12
        print("Results: ", result)
    else:
        print("Closing the execution!")


calculate_hours()
