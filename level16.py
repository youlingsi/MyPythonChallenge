from PIL import Image
img = Image.open("level16_mozart.gif");
print(img.size);
imgCrop = img.crop((600,0,640,40));

"""
find unique values in the Image
"""
def findValue(img):
    value = [];
    h = img.histogram();
    for count in h:
        if count > 0:
            value.append(h.index(count));
    return value;

"""
find the pixels value occupy the most continouse pixels which is the pattern of the pink
"""
def findRepeat(img, value):
    lines = list(img.getdata());
    c = [];
    for v in value:
        count = 0;
        indx = lines.index(v);
        while lines[indx] == v:
            count += 1;
            indx += 1;
        c.append(count);
    return (value[c.index(max(c))], max(c));


print(findRepeat(imgCrop, findValue(imgCrop)));

pink = findRepeat(imgCrop, findValue(imgCrop))[0];

"""
Shift each row so that the pink align at the left
"""
sq = list(img.getdata());
newImg = [];
rows = [];
print(sq);

j = 0
while j < img.height:
    rows.append(sq[j*640:(j+1)*640]);
    j += 1;

for row in rows:
    start = row.index(pink);
    r = row[start:] + row[:start];
    newImg += r;

im = Image.frombytes(img.mode,img.size,bytes(newImg));
im.show();

'''
h = img.histogram();
color = [];
for indx in range(len(h)):
    if h[indx] > 500 and h[indx] < max(h):
        color.append([indx, h[indx]]);
print(color, len(color));
'''

'''

'''
'''

n = 0;
for i in range(img.width):
    for j in range(img.height):
        im.putpixel((i,j), seq[n]);
        n+=1;

im.show()

'''
