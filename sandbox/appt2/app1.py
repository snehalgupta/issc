#Load variable from a file. Userstat.txt
#USerstat.txt has first line as whether user wants to choose more projects, and next lines has names of all projects user has chosen.

import sys
from importlib import reload

file = open("Userstat.txt","r")
l=file.readlines()
uid = l[0]
l1=l[1:]
print("All of your chosen projects will run one by one")
print("Projects you have chosen are:")
ind=1
for i in l1:
	print(str(ind)+" - "+i[i.find('-')+1:])
	ind+=1

chind = int(input("Choose index of project to start with"))
chind-=1
print("Projects will be run from Project "+str(chind)+" in above order, one by one")
print("Note, the program will keep running until you close this application")
#originalsyspath = sys.path

'''for i in range(len(l)):
		prid=i[:i.find('-')-1]

		sys.path.insert(0, './'+prid+'_files')
'''


while(1>0):
	for j in range(chind, len(l1)):
		i=l1[j]
		prid=i[:i.find('-')-1]

		sys.path.insert(0, './'+prid+'_files')
		#print (sys.path)
		import projman
		reload(projman)
		print("Currently doing - "+i[i.find('-')+1:]+" ...")
		projman.runproj()
		sys.path.remove('./'+prid+'_files')

	chind = 0 
	print("Note, the program will keep running until you close this application")

#print("Do you want to chose more projects?('f') Or do you want to delete projects from your list?('d')")
#chosen=input()
