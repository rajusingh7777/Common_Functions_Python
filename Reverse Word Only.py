# Reverse words only of a Sentence

s = "Hello World, I Am Here"
p= s.split()  # str.split(): It split string at whitespace without any argument
# print(p)
for i in p:
    print(i[::-1],' ',end='')