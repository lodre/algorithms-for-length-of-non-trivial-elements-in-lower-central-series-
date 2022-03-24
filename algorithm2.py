
li = int(input("Вести поиск по словам длины: "))
lt = ["a","b","c","d"]
m = 0
sr = []
gg = {"a":"c","b":"d","c":"a","d":"b"}
for _ in range(li-1):
    lr = []
    for x in lt:
        for c in ["a","b","c","d"]:
            if gg[c]!=x[len(x)-1]:
                y = x+c
                if (max(y.count("a")+y.count("b"),y.count("c")+y.count("d"))<=li//2):
                    lr.append(y)
    lt = lr
ltt = [list(x) for x in lt]
count = 0
fast = {}
for i in range(10+2*li):
    fast[i] = {"":{"":1}}
for s in lt:
    n = 2
    b = True
    while(b):
        g = {'a': {},'b': {},'c': {},'d': {}}
        g['a'][""] = 1
        g['a']["x"] = 1
        g['b'][""] = 1
        g['b']["y"] = 1
        k = 0
        i = 1
        while(k<n):
            g['c'][k*"x"] = i
            g['d'][k*"y"] = i
            k+=1
            i*=-1
        def mul(dict1, dict2):
            d = {}
            for s1 in list(dict1.keys()):
                for s2 in list(dict2.keys()):
                    if (len(s1)+len(s2)<n):
                        d[s1+s2] = d.get(s1+s2, 0) + dict1[s1]*dict2[s2]
            return d
        def f(l,s,st):
            i = len(s)
            while(s[:i] not in fast[n].keys()):
                i-=1
            s1 = s[:i]
            if s1!="":
                l = mul(l,fast[n][s1])
            s = s[i:]
            if s == "":
                return l
            else:
                st = st+s1
                c = s[0]
                ss = s[1:]
                a = g[c]
                ll = mul(l,a)
                if len(s)<=li//2:
                    fast[n][st] = l
                return f(ll,ss,st+c)
        l = f({"":1},s,"")
        sum = 0
        for x in list(l.values()):
            sum+=abs(x)
        if sum == 1:
            b = True
        else:
            b = False
        n+=1
        if (n>20):
            n = 0
            break
    if n-2 == m:
        sr.append(s)
    if n-2>m:
        sr = [s]
        m = n-2
sr = [list(s) for s in sr]
srr = []
for s in sr:
    i = 0
    while(i<len(s)):
        if(s[i]=="a"):
            break
        if(s[i]=="c"):
            for i in range(len(s)):
                if s[i] == "a":
                    s[i] = "c"
                elif s[i] == "c":
                    s[i] = "a"
            break
        i+=1
    i = 0
    while(i<len(s)):
        if(s[i]=="b"):
            break
        if(s[i]=="d"):
            for i in range(len(s)):
                if s[i] == "b":
                    s[i] = "d"
                elif s[i] == "d":
                    s[i] = "b"
            break
        i+=1
    i = 0
    while(i<len(s)):
        if(s[i]=="a"):
            break
        if(s[i]=="b"):
            for i in range(len(s)):
                if s[i] == "a":
                    s[i] = "b"
                elif s[i] == "b":
                    s[i] = "a"
                elif s[i] == "c":
                    s[i] = "d"
                elif s[i] == "d":
                    s[i] = "c"
            break
        i+=1
    sum = ""
    for x in s:
        sum = sum + x
    if sum not in srr:
        srr.append(sum)
print("Слово данной длины может лежать в gamma_n, n <",end = "")
print(m+1)
print("Примеры слов из gamma_"+str(m),end = ":\n")
i = 0
for x in srr:
    if i>6:
        break
    print(x)
    i+=1
print("(вместо a^-1 и b^-1 используются c и d соответственно)")
input()