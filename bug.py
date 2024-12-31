def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will give 0 which is correct

my_list_with_string = [10,20,'a',30]
average_string = calculate_average(my_list_with_string) # This will give an error because we can't sum a string and an integer
print(f"The average of an list with string is: {average_string}")