import pickle

obj = pickle.load(open("banner.p", "rb"))

for l in obj:
    line = ""
    for tup in l:
        line += tup[0]*tup[1]
    print line
