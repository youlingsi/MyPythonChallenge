def crack(letter):
    aph = "abcdefghijklmnopqrstuvwxyz";
    n = aph.find(letter);
    if n > -1:
        n = n + 2;
        if n > len(aph)-1:
            n = n-len(aph);
        return aph[n];
    else:
        return letter

oldTxt = "map";
newTxt = "";
for l in oldTxt:
    newTxt = newTxt + str(crack(l));
print(newTxt);
