str_in = "My userID is john17 and my 4 digit pin in 1234 which is secret";

arr = str_in.split();
final_str = "";

for item in arr:
    final_item = "";
    letters = False;
    for char in range(len(item)):
        if item[char].isalpha():
            letters = True;
    if letters == False:
        for i in range(len(item)):
            final_item += "x";
    else:
        final_item += item;

    final_str += final_item + " ";

print(final_str);
