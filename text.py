n = int(input())
d = dict()
for j in range(0,n):
    s = input()
    d[j] = s 
for v in d:
    s = d[v]
    k = s.split("-")
    m = list()
    for i in range(1,len(k)+1):
        m.append(k[-i])
    t = " "
    for x in m:
        t = t + x 
        if x != m[-1]:
            t = t + "-"
    print(t)
