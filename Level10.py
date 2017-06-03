from PIL import Image, ImageDraw

#look-and-say sequence

def numGenerator(num):
    strNum = str(num);
    lst = []
    for n in strNum:
        lst.append(n);
    indx = 0;
    lstDigit = "";
    count = 1;
    if len(lst) == 1:
        lstDigit += str(count) + lst[indx];
        return lstDigit;
    while indx < len(lst) - 1:
        if lst[indx] == lst[indx + 1]:
            count += 1;
            if indx == len(lst)-2:
                lstDigit += str(count) + lst[indx];
        else:
            lstDigit += str(count) + lst[indx];
            count = 1;
        indx += 1;
    if lst[-1] != lst[-2]:
        lstDigit += "1" + lst[-1];
    return lstDigit;


a = [1];
n = 0;

while n < 31:
    num = numGenerator(a[n]);
    a.append(num);
    n += 1;

print(len(a[30]));



#a = [1,11,21,1211,111221,]

#len(a[3
