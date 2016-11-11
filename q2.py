import SimpleGraphics
L=[]
with open('marklist.txt','r') as F:
    for s in F:
        L.append(s)
count=[0,0,0,0,0,0,0,0,0,0]


for k in L:
    if 0<=k<10:
        count[0]+=1
    elif 10<=k<20:
        count[1]+=1
    elif 20<=k<30:
        count[2]+=1
    elif 30<=k<40:
        count[3]+=1
    elif 40<=k<50:
        count[4]+=1
    elif 50<=k<60:
        count[5]+=1
    elif 60<=k<70:
        count[6]+=1
    elif 70<=k<80:
        count[7]+=1
    elif 80<=k<90:
        count[8]+=1
    elif 90<=k<100:
        count[9]+=1
x=[]
for i in range(5,100,10):
    x.append(i)
MakeWindow(max(x),max(count),10,1,True)
for j in range(len(count)-1):
    DrawLineSegment(x[j],count[j],x[j+1],count[j+1])
ShowWindow()


        
        
