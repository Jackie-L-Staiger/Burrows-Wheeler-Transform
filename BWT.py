# Burrows-Wheeler Transform Construction Problem

filename = '/Users/jlsta/PycharmProjects/HW_2/HW_2_Files/BurrowsWheelerstr.txt'  # put string here
file = open(filename, mode='r')  # Open the file for reading

with open(filename) as f:
    string = f.readline()
#print("Original string:", string)

burrows_wheeler_matrix = []

# Make a list of all the possible arrangements
for char in string:
    new_string = string[-1] + string[0:len(string) - 1]
    burrows_wheeler_matrix.append(new_string)
    string = new_string

# Sort the strings in the list:
burrows_wheeler_matrix.sort()
#print("Matrix: ", burrows_wheeler_matrix)

# Last column is the Burrows-Wheeler transform:
transform = ""
for i in range(len(string)):
    transform += burrows_wheeler_matrix[i][len(string) - 1]
print("Burrows-Wheeler Transform: ", transform)
