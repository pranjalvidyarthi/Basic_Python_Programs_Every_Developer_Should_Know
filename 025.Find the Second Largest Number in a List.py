# Find the Second Largest Number in a List
numbers = list(map(int, input('Enter numbers separated by spaces: ').split()))
unique_number = list(set(numbers)) #Remove duplicates
unique_number.sort(reverse=True)

if len(unique_number) < 2:
    print('No second largest number found.')
else:
    print('Second largest number : ', unique_number[1])