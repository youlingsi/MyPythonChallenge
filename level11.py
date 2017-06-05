from PIL import Image, ImageDraw
img = Image.open("level11_cave.jpg");
w = img.width;
h = img.height;
odd = Image.new("RGB", (w//2, h//2));
even = Image.new("RGB", (w//2, h//2));
oddDraw = ImageDraw.Draw(odd, "RGB");
evenDraw = ImageDraw.Draw(even, "RGB");

for i in range(w):
    for j in range(h):
        p = img.getpixel((i,j));
        if (i + j)% 2 == 1:
            oddDraw.point((i//2, j//2), p);
        else:
            evenDraw.point((i//2, j//2), p);

odd.save("level11_odd.jpg");
even.save("level11_even.jpg");
