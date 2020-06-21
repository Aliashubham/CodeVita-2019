n1,n2=input().split()
n1=int(n1)
n2=int(n2)  
if (n2-n1>=35 and n1>=2 and n2<=100):
    p1=[]
    for i in range(n1,n2+1):
        count=0
        for j in range(2,(i//2 + 1)):
            if(i%j==0):
                count=count+1
                break
        if (count==0 and i!=1):
            p1.append(i)
        
    p1_len=len(p1)
    possible_comb=[]
    for i in p1:
        for j in range(0,p1_len):
            if i==p1[j]:
                pass
            else:
                possible_comb.append(int(str(i)+str(p1[j])))
    se=set(possible_comb)
    comb=list(se)
    
    p2=[]
    for i in comb:
        if i>1:
            for j in range(2,i):
                if (i%j)==0:
                    break
            else:
                p2.append(i)
                
    p2.sort()
    a=p2[0]
    b=p2[-1]
    c=len(p2)
    d=1
    while (d<c):
        a, b =b, a+b
        d+=1
    print(a)