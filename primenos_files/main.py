"This is the main file for the prime numbers task"

from math import sqrt
#import subprocess

def dotask():

	file = open("primenos_files/task.txt","r")

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
	
	print("T Id"+tid+"done")
	statfile = open("primenos_files/projstat.txt", "w")

	statfile.write("havF")
	statfile.write("comT")
	statfile.write("uplF")

	statfile.close()

	outfile = open("primenos_files/result.txt", "w")

	outfile.write(str(count)+":"+tid)

	outfile.close()

	#subprocess.call(["pwd"])
	#subprocess.call(["ls"])
	#subprocess.call(["sleep","2"])

	#subprocess.call(["python3", "app.py"])
