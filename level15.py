"""
find the number of leap years between the two defined years
"""
def findLeapYear(tar, ref):
    n = 0
    for y in range(tar, ref):
        if y % 400 == 0:
            n += 1;
        elif y % 100 != 0 and y % 4 == 0:
            n += 1;
    return n


"""
find the difference in day of Jan 1st between the target year(tar) and reference year(ref)
"""
def dayofJan1st(tar, ref, refDayIndx):
    day = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"];
    dif = (abs(tar - ref) * 365 + findLeapYear(tar, ref)) % 7;
    indx = refDayIndx + abs(tar-ref)//(tar - ref) * dif;
    if indx > 6:
        indx = indx - 7;
    return day[indx];

year = [];
for i in range(1006, 1996, 10):
    if i % 4 == 0 and i % 100 != 0:
        year.append(i);
    elif i % 400 == 0:
        year.append(i);


for y in year:
    tarDay = dayofJan1st(y, 1996, 1);
    if tarDay == "Thur":
        print(y);

"""
He ain't the youngest, he is the second, so not the latest year in the latest
Year: 1756
date on the calenda is Jan 26, 1756

Buy flowers for tomorrow, so special date is Jan 27, 1756;

It was Mozart's birthday.

"""
