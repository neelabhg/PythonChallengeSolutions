import re
p = re.compile('[^A-Z][A-Z]{3,3}[a-z][A-Z]{3,3}[^A-Z]')
f = open("mess.txt", "r")
text = f.read()
answer = ""
iterator = p.finditer(text)
for match in iterator:
    answer += match.group()[4]

print answer
