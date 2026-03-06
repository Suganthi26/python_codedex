#simplifying loops wiht just one line

numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(numbers)
print(even_numbers)
print(odd_numbers)

#results
#[57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
#[10, 82, 36, 46, 92, 48]
#[57, 89, 13, 23]
