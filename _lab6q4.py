str_1 = input("Enter a string: ");
str_2 = input("Enter a string of the same length: ");

hamming_distance = 0;

for char_i in range(len(str_1)):
    #print(char_i,":",str_1[char_i],",",str_2[char_i]);
    if str_1[char_i] != str_2[char_i]:
        hamming_distance += 1;

print("hamming distance:",hamming_distance);