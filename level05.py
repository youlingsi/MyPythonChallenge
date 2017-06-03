import urllib.request
import pickle

# check the url and return the content as string.
def checkURL(url):
    web = urllib.request.urlopen(url);
    byt = web.read();
    text = byt.decode("utf8");
    web.close()
    return byt;

link = "http://www.pythonchallenge.com/pc/def/banner.p";
p = pickle.loads(checkURL(link));
for lst in p:
     #note the way to print the same items multiple times. Join Function
    print("".join([k*v for k,v in lst]));
