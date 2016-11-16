"""
This is the main program file
This will be responsible for managing the download and running of the project programs.
It
downloads the project files if not dowloaded
runs get tasks if task not assigned yet
uploads tasks if not uploaded
"""

import subprocess

file=open('Projectfiles/projstat.txt','r')
l2=file.readlines()
l=l2[0]
file.close()
file1=open('Projectfiles/task.txt','r')
l1=file1.read()
file1.close()

#print(l, l[l.find('v')+1], l[l.find('m')+1], l[l.find('l')+1])
if l[l.find('v')+1]=='F':
	a=False
else:
	a=True
havtask= ((a) and (len(l1)>0))

if l[l.find('m')+1]=='F':
	a=False
else:
	a=True
completed = a

uploaded = l[l.find('l')+1]

#print(havtask,completed,uploaded)



if uploaded=='F':
	subprocess.call(["python3", "Projectfiles/up.py"])

elif havtask:
	subprocess.call(["python3", "Projectfiles/a.py"])

else:
	subprocess.call(["python3", "Projectfiles/getdata.py"])
	#subprocess.call(["python3", "Projectfiles/a.py"])

'''
subprocess.call(["python3", "Projectfiles/getdata.py"])
subprocess.call(["sleep", "2s"])
subprocess.call(["python3", "Projectfiles/a.py"])
'''
