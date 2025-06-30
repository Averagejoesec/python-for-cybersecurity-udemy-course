# input a list with commas
numbers = input("Enter numbers separated by commas: ")
numbers_list = numbers.split(", ")

# function that loops through the list and determines the largest number by comparing each item
def main(numbers_list):
    max_number = 0
    for i in numbers_list:
        i = int(i)
        if i > max_number:
            max_number = i

    print(f"The largest number is: {max_number}")

main(numbers_list)