#Load variable from a file. Userstat.txt
#USerstat.txt has first line as whether user wants to choose more projects, and next lines has names of all projects user has chosen.


#We have to create a login function here for the user, else, how would the app know which userfile to download.?
#For now let's simply ask the user for his username, and not the whole login process

import urllib.request
a=True
while(a):

	try:
		username = input("Please enter you username - ")
		a=False
		url = 'http://127.0.0.1:8000/download_userfile/'+username+'/'

		obj=urllib.request.urlopen(url)
	except:
		print("Oops! wrong username, Try again!")
		a=True
	

import sys
import time
from importlib import reload
'''zip = ZipFile('file.zip')
zip.extractall()'''

data = obj.read()
with open('Userstat_'+username+'.txt', "wb+") as code:
	code.write(data)

code.close()

#urllib.request.urlretrieve(url,'Userstat_'+username+'.txt') it's in python2
 
file = open('Userstat_'+username+'.txt',"r")
l=file.readlines()
uid = l[0][0]
l1=l[1:]
file.close()
print("All of your chosen projects will run one by one")
print("Projects you have chosen are:")
ind=1
donecount=0
for i in l1:
	a = str(ind)+" - "+i[i.find('-')+1:]
	print(a)
	if '(done)' in a:
		donecount+=1
	ind+=1

if donecount==len(l1):
	print("Congratulations!!\n All the tasks of all the projects you are contributing to,")
	print("Are done! Hurray!")



chind = int(input("Choose index of project to start with"))
print("Projects will be run from Project "+str(chind)+" in above order, one by one")
print("Note, the program will keep running until you close this application")
#originalsyspath = sys.path

'''for i in range(len(l)):
		prid=i[:i.find('-')-1]

		sys.path.insert(0, './'+prid+'_files')
'''


while(1>0):
	for j in range(chind, len(l)):
		i=l[j]
		if ' (done)' in i:
			continue
		elif ' (wait)' in i:
			print('Tasks for '+i+' are all assigned but not completed.')
			print('Tasks maybe available after about 60 seconds, so sleeping for 60 seconds....')
			time.sleep(60)
		prid=i[:i.find('-')]
		

		sys.path.insert(0, './'+prid+'_files')
		print(sys.path)
		import projman
		reload(projman)
		print("Currently doing - "+i[i.find('-')+1:]+" ...")
		projman.runproj(username)
		sys.path.remove('./'+prid+'_files')


	file = open('Userstat_'+username+'.txt',"r")
	l=file.readlines()
	uid = l[0][0]
	l1=l[1:]
	file.close()
	chind = 1
	donecount=0
	for i in l1:
		a = str(ind)+" - "+i[i.find('-')+1:]
		print(a)
		if '(done)' in a:
			donecount+=1
		ind+=1

	if donecount==len(l1):
		print("Congratulations!!\n All the tasks of all the projects you are contributing to,")
		print("Are done! Hurray!")
		break

	print("Note, the program will keep running until you close this application")

print("The program will now exit")

#print("Do you want to chose more projects?('f') Or do you want to delete projects from your list?('d')")
#chosen=input()
