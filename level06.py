import zipfile

# generate the number after the next nothing is.
def findNumber(text):
    indx = text.find("nothing is");
    if (indx > 0):
        num = text[indx+11:];
    else:
        num = "none";
    return num;

fileName = "level06_channel.zip"
zipObject = zipfile.ZipFile(fileName, "r");
strNum = "90052";
count = 0;
comments = []
while count < 910:
    memContent = zipObject.open(strNum + ".txt", "r").read().decode("utf8");
    memComment = zipObject.getinfo(strNum + ".txt").comment.decode();
    comments.append(memComment);
    print(memContent);
    print(strNum);
    strNum = findNumber(memContent);
    if strNum != "none":
        count += 1;
    else:
        break;
print("".join(comments));
