import re

#open the file
my_file = open('regex_sum_515213.txt')

#read all the contents of the file
text = my_file.read()
number_regex = '[0-9]+'
#match the numbers and store in a list
numbers = re.findall(number_regex,text)

total=0
for num in numbers:
    total+=int(num)

print(total)    
