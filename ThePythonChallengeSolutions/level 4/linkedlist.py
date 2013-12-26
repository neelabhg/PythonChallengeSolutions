import urllib2, re

p = re.compile(r"\d+")

def getData(val):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(val)
    response = urllib2.urlopen(url)
    return response.read()

def follow_linked_list(val):
    html = getData(val)
    print html
    m = p.search(html)
    if m:
        follow_linked_list(int(m.group()))

follow_linked_list(12345)
