try:
    a=[]
    for _ in range(int(input())):
         g,c=map(int, input().split())
         h=((c*c)//(2*g))
         a.append(h)
    for i in range(0,len(a)):
        print(a[i])
except:
    pass
