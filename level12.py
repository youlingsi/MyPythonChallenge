data = open("level12_evil2.gfx","rb").read();

for i in range(5):
    open("level12_%d.jpg" % i, "wb").write(data[i::5]);

"""
1. When manipulating bytes sequence,
if using only one element from the bytes sequence.
like data[5] here.
It automatically transfer the bytes to integer.
must use a slice of the bytes sequence to mantain the bytes format.

2. the use of list:
x[startAt:endBefore:skip]

"""
