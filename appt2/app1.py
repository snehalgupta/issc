#Load variable from a file. Userstat.txt
#USerstat.txt has first line as whether user wants to choose more projects, and next lines has names of all projects user has chosen.


#We have to create a login function here for the user, else, how would the app know which userfile to download.?
#For now let's simply ask the user for his username, and not the whole login process

username = input("Please enter you username - ")

import sys
import urllib.request
from importlib import reload
'''zip = ZipFile('file.zip')
zip.extractall()'''
url = 'http://127.0.0.1:8000/download_userfile/'+username+'/'

obj=urllib.request.urlopen(url)
#obj2=obj.read()
#obj3=obj2.decode("utf-8
#f = urllib2.urlopen(url)
data = obj.read()
with open('Userstat_'+username+'.txt', "wb+") as code:
	code.write(data)

code.close()

#urllib.request.urlretrieve(url,'Userstat_'+username+'.txt') it's in python2
 
file = open('Userstat_'+username+'.txt',"r")
l=file.readlines()
uid = l[0][0]
l1=l[1:]
print("All of your chosen projects will run one by one")
print("Projects you have chosen are:")
ind=1
for i in l1:
	print(str(ind)+" - "+i[i.find('-')+1:])
	ind+=1

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
		prid=i[:i.find('-')]

		sys.path.insert(0, './'+prid+'_files')
		print(sys.path)
		import projman
		reload(projman)
		print("Currently doing - "+i[i.find('-')+1:]+" ...")
		projman.runproj(username)
		sys.path.remove('./'+prid+'_files')

	chind = 1
	print("Note, the program will keep running until you close this application")

#print("Do you want to chose more projects?('f') Or do you want to delete projects from your list?('d')")
#chosen=input()
