def hammingDistance(x, y):
    xb = "{0:b}".format(x)
    yb = "{0:b}".format(y)
    dist = 0

    maxlen = max(len(xb), len(yb))
    xb = xb.zfill(maxlen)
    yb = yb.zfill(maxlen)

    for n in range(len(xb)):
        dist += abs(int(xb[n]) - int(yb[n]))

    return dist

if __name__ == "__main__":
    x = 1
    y = 4
    res = hammingDistance(x, y)
    print(res)


