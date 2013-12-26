import urllib2, zipfile, StringIO, re

response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
zfile = zipfile.ZipFile(StringIO.StringIO(response.read()), 'r')

p = re.compile(r"\d+")

def follow_linked_list(val):
    string = zfile.read(val + ".txt")
    print string
    m = p.search(string)
    if m:
        follow_linked_list(m.group())

def collect_comments(val):
    line = zfile.getinfo(val + ".txt").comment
    string = zfile.read(val + ".txt")
    m = p.search(string)
    if m:
        line += collect_comments(m.group())
    return line

#print zfile.read("readme.txt")
#follow_linked_list("90052")
print collect_comments("90052")
zfile.close()
