import datetime as d
st = d.datetime.now()
for i in range(0, 100):
    print("hello")
et = d.datetime.now()
rt = (et - st).total_seconds()
print(rt)