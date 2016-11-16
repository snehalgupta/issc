import urllib.request

import json

import subprocess

print("Getting a task...")
#url="http://snehalgupta.pythonanywhere.com"
url="http://127.0.0.1:8000"
#print(url+"/export")
obj=urllib.request.urlopen(url+"/export/primenos")
obj2=obj.read()
obj3=obj2.decode("utf-8")

dict = json.loads(obj3)
print("Got Taskid - "+dict['taskid'], "Task - "+dict['task'])


#json string breakdown

if dict=={'alltasks':'done'}:
	print("Hurray! all tasks of this project are done!")
	exit()

#print(string)

file = open("Projectfiles/task.txt","w")

file.write(dict['taskid'])
file.write(":")
file.write(dict['task'])
file.close()
'''
cnfm=urlopen(url+"/igot/"+str(dict['taskid']))

print(url+"/igot/"+str(dict['taskid']))
'''

statfile = open("Projectfiles/projstat.txt", "w")

statfile.write("havT") #We are assuming once the user runs the app, he is willing to run the project until it is completed.
statfile.write("comF")
statfile.write("uplT")

statfile.close()

subprocess.call(["python3", "app.py"])
