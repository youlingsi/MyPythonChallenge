import urllib.request
from urllib.parse import quote_plus, unquote_to_bytes
import bz2

# check the url and return the content as string.
def checkURL(url):
    web = urllib.request.urlopen(url);
    byt = web.read();
    text = byt.decode("utf8");
    web.close()
    info = web.getheader("Set-Cookie");
    indx1 = info.find("=") + 1;
    indx2 = info.find(";");
    return [text, info[indx1:indx2]];

# generate the number after the next nothing is.
def findNumber(text):
    indx = text.find("the next busynothing is");
    num = text[indx+24:];
    return num;

preText = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=";
strNum = "12345";
count = 0;
txt = "";
info ="";
while (True) :
    print(count);
    txt = checkURL(preText + strNum)[0];
    info += checkURL(preText + strNum)[1];
    print(txt);
    strNum = findNumber(txt)
    if not(strNum.isdigit()):
        break
    count += 1;

"""
not sure why part, maybe has something to to with the decoding
outcome:
is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

"""
res = urllib.parse.unquote_to_bytes(info.replace("+", " "));
print(res);
print(bz2.decompress(res).decode());

'''
phone call part, from level13
Mozart's father: Leopold Mozart

'''

import xmlrpc.client
web = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php");
print(web.phone("Leopold"));

"""
communicate with the web site
"""
url = "http://www.pythonchallenge.com/pc/stuff/violin.php";
msg = "the flowers are on their way";
req = urllib.request.Request(url, headers = {"Cookie": "info=" + quote_plus(msg)});
print(urllib.request.urlopen(req).read().decode());
