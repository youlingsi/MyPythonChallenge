#Detect small letters that are possible to form the pattern
def findLowLetter(line):
    index = 3
    indexList = [];
    #find lower case letters and check if the lower case letter posite between index 3 to len(line)-4
    while index < len(line)-4:
        if line[index].islower():
            indexList.append(index);
        index += 1;
    return indexList;

#check if the pattern is matched.
def patternDetect(line, lst):
    indxList = [];
    if lst != []:
        for indx in lst:
            if (line[indx -3:indx].isupper()) and (line[indx + 1:indx + 4].isupper()):
                if (indx - 4 < 0) and line[indx + 4].islower():
                    indxList.append(indx);
                elif (indx + 4 > len(line)-1) and (line[indx -4].islower()):
                    indxList.append(indx);
                elif (line[indx - 4].islower()) and (line[indx + 4].islower()):
                    indxList.append(indx);
    return indxList;


# read in the file.
fileName = "level03_data.txt"
fileObj = open(fileName,"r")
allList = [];
#search line by line.
for line in fileObj:
    iList = findLowLetter(line);
    allList = patternDetect(line, iList);
    if (allList != []):
        for n in allList:
            if(n>3) and (n < len(line) - 4):
                print(line[n-4:n+4]);
            elif (n<4):
                print(line[n-3:n+4]);
            elif (n>len(line-5)):
                print(line[n-4:n+3]);
