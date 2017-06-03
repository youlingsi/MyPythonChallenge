from PIL import Image
img = Image.open("level07_oxygen.png");
w = img.width;
h = img.height;
row = [img.getpixel((x, h//2)) for x in range(w)];
eliRow = [];
n = 0
while (row[n][0] == row[n][1]) and (row[n][1]== row[n][2]) and (n < w):
    eliRow.append(row[n][0]);
    n += 7;

print(eliRow);
print("".join(map(chr,eliRow)));
print("".join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121])));
