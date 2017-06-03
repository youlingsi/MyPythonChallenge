fileName = "level02_data.txt";
fileobj = open(fileName,"r");
txtOutput = "";
for line in fileobj:
    for l in line:
        if l.isalpha():
            txtOutput += l;
print(txtOutput);
