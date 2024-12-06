# Author: Amit
# Date: Nov 15th, 2024
# Description: lists

# Lists store items

# list_var = [item1, item2]

# List of strings
fruits = ["apple", "banana", "orange"]

# List of integers
numbers = [1,2,3,4]


# Both strings and integers
listC = ["apple", 1, "banana", 3]

# Get survival items
item1 = input("Enter the first item: ")
item2 =  input("Enter the second item: ")
item3 = input("Enter the third item: ")

chosen_items = [item1,item2,item3]
print("To survive the deserted island you chose: ", chosen_items)

# Index is the location or position of item
# starts at 0
# from the right it starts at -1

listA = ["Apple", "Banana", "Orange"]
listA[1] = "Pear"
print(listA)

listA[-1] = "Grapes"
print(listA)

# Concatenate = to add together
new_list = chosen_items + listA
print(new_list)

# .append(), .insert(), .remove()

new_list.append("Car") # added to the end
new_list.insert(0,"kiwi") # added at index 0
new_list.remove("Car") # removed car from the list
print(new_list)

# Homework
num_list = [1, 1000, 2, 4, 3, 24, 77, 6, 7, 11, 8]

# remove 3 numbers from the list
num_list.remove(1000)
num_list.remove(24)
num_list.remove(11)

# change the number at 3 and 4
num_list[2] = 3
num_list[3] = 4

# change the number 77 to 5
num_list[6] = 5

# Append or add the numbers 9 and 10 to the end
num_list.append(9)
num_list.append(10)
