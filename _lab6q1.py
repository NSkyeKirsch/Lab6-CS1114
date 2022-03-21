name = "Grace Hooper";

exp_1 = name[1];
exp_2 = name[len(name)-1];
exp_3 = name[:6];

print("1:",exp_1,exp_2,exp_3);

new_str = "";
name_2 = "alan turing";

new_str = name_2[0].upper() + name_2[1:5] + name_2[5].upper() + name_2[6:len(name_2)];

exp_1 = new_str[:4];
exp_2 = new_str[5:len(new_str)]

print("2:", exp_1,exp_2);

s_q1 = "Computer Science";

exp_1 = s_q1[:len(s_q1):2];
exp_2 = s_q1[:4] + " " + s_q1[9:12];

print("3:",exp_1,exp_2);

place = "Bletchley Park, England";

exp_1 = place[16:len(place)];
exp_2 = place[8::-1]

print("4:",exp_1,exp_2)

