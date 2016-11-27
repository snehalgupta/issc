from urllib.request import urlopen

import json

import subprocess

import time

def gettask(path_to_files):
	i=0

	while(i<10):
		#try:
		print("Getting a task...")
		#url="http://snehalgupta.pythonanywhere.com"
		url="http://127.0.0.1:8000"
		#print(url+"/export")
		obj=urlopen(url+"/export/primenos")
		obj2=obj.read()
		obj3=obj2.decode("utf-8")

		dict = json.loads(obj3)
		print(dict)
		try:

			if dict['alltasks']=='done':
				print("Hurray! all tasks of this project are done! (or assigned)")
				break
		except:
			pass
		print("Got Taskid - "+dict['taskid'], "Task - "+dict['task'])


		#json string breakdown

		

		#print(string)

		file = open(path_to_files+"task.txt","w")

		file.write(dict['taskid'])
		file.write(":")
		file.write(dict['task'])
		file.close()
		print(dict)

			
		try:
			cnfm=urlopen(url+"/igot/primenos/"+str(dict['taskid']))
		except:
			pass

		statfile = open(path_to_files+"projstat.txt", "w")

		statfile.write("havT") #We are assuming once the user runs the app, he is willing to run the project until it is completed.
		statfile.write("comF")
		statfile.write("uplT")
		statfile.close()

		#subprocess.call(["python3", "app.py"])

		break

		'''except:
			print("There seems to be a problem with the connection")
			print("Retrying....")
			i+=1
			time.sleep(3)
			pass'''
