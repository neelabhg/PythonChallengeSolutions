# I got the hints from the forums
# http://www.pythonchallenge.com/forums/viewtopic.php?f=1&t=20&hilit=level+10+cow
# Specifically,
# Hint 1: Morris 
# Hint 2: hettingertools
# Upon searching the web, I found that the sequence was a
# look-and-say sequence (aka Morris sequence) - http://en.wikipedia.org/wiki/Look-and-say_sequence
# As for Hint 2, when searching for hettingertools, the first link
# points to python's itertools, which gave me a better way to group
# consecutive occurrings (see code)
# And then the puzzle's title, "what are you looking at?" makes sense - look-and-say sequence


from itertools import groupby

a = [1, 11, 21, 1211, 111221]
a = map(str, a)

def get_elem(sequence, i):
    
    # From http://stackoverflow.com/questions/13197668/counting-consecutive-characters-in-a-string
    groups = [[k,len(list(g))] for k, g in groupby(sequence[i-1])]
    
    elem = ""
    for group in groups:
        elem += str(group[1]) + group[0]
    return elem

for i in range(5, 31):
    a.append(get_elem(a, i))

print 'Answer: ', len(a[30])

raw_input('Press a key to exit')
