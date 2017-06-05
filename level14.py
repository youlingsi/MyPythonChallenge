from PIL import Image, ImageDraw
img = Image.open("level14_wire.png");
print(img.size);
p = [];
for i in range(img.width):
    px = (img.getpixel((i, 0)));
    p.append(px);

im = Image.new("RGB", (100,100));
draw = ImageDraw.Draw(im, "RGB");

"""
Generate a sequence of the cordinate (i,j) of the outside spirl (conterclockwise)
1. Start from the left up point
2. l = Number of the element in each line/column (perfect square matrix)
3. n = the number of circle inwards. (the most outside on is 0, the one layer inside is 1)
"""
def seqGenerator(l, n):


    #sequence of the to line exluding the last element on the right
    s1 = [(n + j, n) for j in range(0,l)];
    del s1[-1];

    #sequence of the right column excluding the last element at the bottom
    s2 = [(n +l-1, n + i) for i in range(0,l)];
    del s2[-1];

    #sequence of the bottom line (right to left) excluding the last element on the left
    s3 = [(n+j,n + l-1) for j in range(l-1, 0, -1)];

    #sequence of the left column (bottom to top) excluding the last element at the top
    s4 = [(n, n + i) for i in range(l-1, 0, -1)];

    sq = s1 + s2 + s3 + s4;
    return sq;

"""
An alternative way of generate the sequence of the cordinate
1. define four different types of delta for different sides
2. for each side the delta value will add for l - 1 times (l = number of elements in each side)
3. start from "(n,n)". (n = the cordinate of the stat point.

"""
def seqGeneraterAl(l,n):
    delta = [(1,0), (0,1), (-1, 0), (0, -1)];
    #Change the delta will change the direaction and start point of the spirl

    sq = [];
    i = n;
    j = n;
    for step in delta:
        for count in range(l-1):
            i += step[0];
            j += step[1];
            sq += [(i,j)];
    return sq;


n = 0;
l = 100;

seq = [];
while l > 0:
    if l != 1: # Does not need this condition for the alternative method.
        seq += seqGeneraterAl(l,n);
    else:
        seq.append((n,n));
    l -= 2;
    n += 1;

for indx in range(len(seq)):
    draw.point(seq[indx], p[indx]);

im.show();
