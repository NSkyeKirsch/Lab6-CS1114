input_string = input("Please enter your phrase: ");
new_string = "";

for char in range(len(input_string)-1, -1, -1):
    new_string += input_string[char];

print(new_string);