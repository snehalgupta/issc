"This is the main file for the prime numbers task"
import sqlite3
from math import sqrt
#import subprocess
'''	print('hello')
	i=1
	x3=[]
	y3=[]
	x4=[]
	y4=[]
	x1=path_to_files+'task_'+tid+'.db'
	connection=sqlite3.connect("filename.db")
	x2=connection.execute("SELECT x FROM DATA")
	y2=connection.execute("SELECT y FROM DATA")
	for d in x2:
		x4.append(float(d[0]))
	for d in y2:
		y4.append(float(d[0]))
	connection.close()
	while(i>0 and i<(len(x4)-1)):
		if(y4[i]<y4[i+1] and y4[i]<y4[i-1] and i<=(len(x4)-2)):
			y3.append(y4[i])
			x3.append(x4[i])
			i+=2
		else:
			i+=1
	print(x3,y3)
'''
def dotask(path_to_files):

	i=1
	x3=[]
	y3=[]
	x4=[]
	y4=[]
	filename=path_to_files+'task.db'#_'+tid+'.db'
	connection=sqlite3.connect(filename)
	x2=connection.execute("SELECT x FROM DATA")
	y2=connection.execute("SELECT y FROM DATA")
	for d in x2:
		x4.append(float(d[0]))
	for d in y2:
		y4.append(float(d[0]))
	connection.close()
	tid = str(int(x4.pop(0)))
	tid = str(int(y4.pop(0)))
	while(i>0 and i<(len(x4)-1)):
		if(y4[i]<y4[i+1] and y4[i]<y4[i-1] and i<=(len(x4)-2)):
			y3.append(y4[i])
			x3.append(x4[i])
			i+=2
		else:
			i+=1
	print(x4,y4)
	file=open('result.txt', 'w+')
	file.write(tid+'\n')
	for i in range(len(x4)):
		file.write(str(x4[i])+' '+str(y4[i])+'\n')
	
	'''file = open(path_to_files+"task.txt","r")

	s = file.read()

	#print(s[s.find('o')+1:])
	order=10**6

	#print(s)
	fs=s.find(":")+1
	to=s.find('to')

	#print(s[fs:to])


	minval=int(s[fs:to])*order
	maxval=int(s[to+2:])*order
	tid=s[:fs-1]

	print("Working on task T Id"+tid)
	print(str(minval)+"to"+str(maxval))

	file.close()

	i=minval
	count=0
	while (i>=minval and i<=maxval):
		flag=True
		for j in range(2,int(sqrt(i))):
			if i%j==0:
				flag=False
				break

		if flag:
			count+=1

		i+=1
	'''
	print("T Id"+tid+"done")
	statfile = open(path_to_files+"projstat.txt", "w")

	statfile.write("havF")
	statfile.write("comT")
	statfile.write("uplF")

	statfile.close()

	#outfile = open(path_to_files+"result.txt", "w")

	#outfile.write(str(count)+":"+tid)

	#outfile.close()

	#subprocess.call(["pwd"])
	#subprocess.call(["ls"])
	#subprocess.call(["sleep","2"])

	#subprocess.call(["python3", "app.py"])'''

if __name__=='__main__':
	dotask('')