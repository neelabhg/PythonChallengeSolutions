from collections import defaultdict
d = defaultdict(int)
f = open("mess.txt", "r")
text = f.read()
letters = ['a','e','i','l','q','u','t','y']
string = ""

for c in text:
    d[c] += 1
    if c in letters:
        string += c

print d
print string
