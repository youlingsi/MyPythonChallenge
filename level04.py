import urllib.request

# check the url and return the content as string.
def checkURL(url):
    web = urllib.request.urlopen(url);
    byt = web.read();
    text = byt.decode("utf8");
    web.close()
    return text;

# generate the number after the next nothing is.
def findNumber(text):
    indx = text.find("the next nothing is");
    num = text[indx+20:];
    return num;

preText = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=";
strNum = "12345";
count = 0;
txt = ""
while count < 251 :
    print(count);
    txt = checkURL(preText + strNum);
    print(txt);
    if count == 85:
        strNum = str(int(int(strNum)/2));
        print(strNum);
    else:
        strNum = findNumber(txt);
    count += 1;
