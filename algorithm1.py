print("(вместо a^-1 и b^-1 используются c и d соответственно)")
s = list(input("Слово w = "))

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
    def f(l,s):
        if s == []:
            return l
        else:
            c = s[0]
            s = s[1:]
            a = g[c]
            ll = {}
            for s1 in list(l.keys()):
                for s2 in list(a.keys()):
                    if (len(s1)+len(s2) <n):
                        ll[s1+s2] = ll.get(s1+s2, 0) + l[s1]*a[s2]
            return f(ll,s)
    l = f({"":1},s)
    sum = 0
    for x in list(l.values()):
        sum+=abs(x)
    if sum == 1:
        b = True
    else:
        b = False
    n+=1
    if (n>20):
        break
print("Слово w лежит в gamma_n, n < ",end="")
print(n-1,end=".\n")
print("Сумма членов f(w), степень которых меньше ",end="")
print(n-1,end=":\n")
for s in list(l.keys()):
    if s == "":
        print(l[s],end = "")
    elif len(s)<n:
        x = l[s]
        if x<0:
            if x<-1:
                print(x,end="")
            else:
                print("-",end="")
            print(s,end="")
        if x>0:
            print("+",end="")
            if x>1:
                print(x,end="")
            print(s,end="")
input()