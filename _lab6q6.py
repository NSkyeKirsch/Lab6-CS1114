in_str = "Hello darkness my old friend".lower();

final_str = "";
test_arr = in_str.split();
i = 0;

for item in test_arr:
    new_str = "";
    if i % 2 == 0:
        item = item.upper();
    i += 1;
    for char in range(len(item)-1, -1, -1):
        new_str += item[char];
    final_str += new_str + " ";

print("Old phrase:", in_str);
print("New phrase:", final_str);
