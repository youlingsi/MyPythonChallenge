import xmlrpc.client
from PIL import Image
import requests

web = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php");
checkMethod = web.system.methodHelp("phone");
print(checkMethod);
evil = requests.get("http://www.pythonchallenge.com/pc/return/evil4.jpg", auth = ("huge", "file")).content;
print(evil);
phone = web.phone("Bert");
print(phone);

"""
555 means fake number in US. So the key is Italy.

"""
