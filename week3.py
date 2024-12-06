# Author: Amit
# Date: Nov 22nd, 2024
# Description: Manipulating strings

# Strings: ' ""
# Floats: 1.23
# Integers: 1
# Boolean: True or False
# Snake case: Underscores

repeated_text = "Repeat me! " * 3
print(repeated_text)

text = "Amit"
length = len(text)
print(length)

second_letter = text[1]
print(second_letter)

print(text[-1])
print(text[3])

text = "Hello, World!"

print(text[0:5]) # Hello  
print(text[7:]) # World!
print(text[-3:]) # d!

print(text.strip()) # no whitespace
print(text.upper()) # uppercase
print(text.lower()) # lowercase

text.replace("World", "Amit") # replacing world with name
text.find(",") # what position is , at?

text = "Hi my name is Jill! What is your name?"
index = text.find("Jill") 
print(index)






