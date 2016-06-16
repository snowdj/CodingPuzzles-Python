a = []
a = [0,1,2,3,4]
print "length of a = ", len(a)

for i in range(1, len(a) + 1):
    print ">>>> i = ", i

    if i >= len(a) or a[i] == '':
        print "a[i] is out of range"
    else:
        print "a[i] = ", a[i]

    if a[:i] == '':
        print "a[:i] is out of range"
    else:
        print "a[:i] = ", a[:i]

    if a[i:] == '':
        print "a[i:] is out of range"
    else:
        print "a[i:] = ", a[i:]