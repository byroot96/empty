from datetime import datetime
now = datetime.now()


"""


f=open("README.md", "w+")
f.write(f'last update at : {now.strftime("%d/%m/%Y %H:%M:%S")} (UTC)')
f.close()
print(0)
"""

# Using readlines()
file1=open('map.txt','r')
Lines=file1.readlines()

l1=Lines[0].strip().split(" ")
l2=Lines[1].strip().split(" ")
l3=Lines[2].strip().split(" ")
l4=Lines[3].strip().split(" ")
l5=Lines[4].strip().split(" ")
l6=Lines[5].strip().split(" ")
l7=Lines[6].strip().split(" ")

l=min([len(l1),len(l2),len(l3),len(l4),len(l5),len(l6),len(l7)])
c=[]

for i in range(0,l):
    c.append(l1[i])
    c.append(l2[i])
    c.append(l3[i])
    c.append(l4[i])
    c.append(l5[i])
    c.append(l6[i])
    c.append(l7[i])


f=open('last.txt','r')
g=f.readlines()[0].strip()
Line=int(g.split(":")[0])
dayis=int(g.split(":")[1])
f.close()

wd=now.weekday()
#wd=1

if Line==-1:
    if wd==6:
        work=True
    else:
        work=False
else:
    work=True

if work==True and wd!=dayis:
    f=open('last.txt','w')
    f.write(f'{Line+1}:{wd}')
    #Line+=1
    f.close()
    print(1)
else:
    if Line!=-1:
        print(c[Line])
        if c[Line]==1:
            f=open("empty.md", "w+")
            f.write(f'last update at : {now.strftime("%d/%m/%Y %H:%M:%S")} (UTC)')
            f.close()
    else:
        print(0)