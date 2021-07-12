try:
    a=[]
    for _ in range(int(input())):
        d,x,y,z=map(int, input().split())
        work_x=x*7
        work_yz=(y*d)+(z*(7-d))
        max_prod=max(work_x,work_yz)
        a.append(max_prod)
    for i in range(0,len(a)):
        print(a[i])
except:
    pass
