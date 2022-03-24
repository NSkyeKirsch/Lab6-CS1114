input_str = input("Please enter a phrase: ");
input_str = input_str.lower();
final_str = input_str + " is{0} a sentence length palindrome";

test_str = "";

for char in input_str:
    if(char.isalpha()):
        test_str += char;

is_palindrome = True;
#print(test_str);
for letter in range(len(test_str)):
    if(test_str[letter] != test_str[len(test_str)-(letter+1)]):
        is_palindrome = False;

#print(is_palindrome);
print(final_str.format("") if is_palindrome else final_str.format(" NOT"));

