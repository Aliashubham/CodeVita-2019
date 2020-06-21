def Deno(tem):
    l=[]
    s=1
    k=1
    l.append(s)
    while(k<tem):
        s+=1
        l.append(s)
        k+=l[-1]
    print(len(l))        

t=int(input())
n=[]
for _ in range(t):
    n.append(list(input().rstrip().split()))
    
t_len=len(n)
for i in range(0,t_len):
    temp=str(n[i])
    e=temp.replace("[","")
    m=e.replace("'","",2)
    p=m.replace("]","")
    tem=int(p)
    Deno(tem)