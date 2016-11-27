import urllib.request

import json

import subprocess

import time

def gettask(path_to_files):
	i=0

	while(i<10):
		try:
			print("Getting a task...")
			#url="http://snehalgupta.pythonanywhere.com"
			url="http://127.0.0.1:8000"
			#print(url+"/export")
			obj=urllib.request.urlopen('http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip')#url+"/export/localmin")
			#obj2=obj.read()
			#obj3=obj2.decode("utf-8")

			#f = urllib2.urlopen(url)
			data = obj.read()
			with open(path_to_files+'name.zip', "wb+") as code:
				code.write(data)

			obj3 = data[:data.find('}')+1]

			dict = json.loads(obj3)
			print("Got Taskid - "+dict['taskid'], "Task - "+dict['task'])


			#json string breakdown

			if dict=={'alltasks':'done'}:
				print("Hurray! all tasks of this project are done!")
				exit()

			#print(string)

			file = open(path_to_files+"task.txt","w")

			file.write(dict['taskid'])
			file.write(":")
			file.write(dict['task'])
			file.close()
			
			cnfm=urlopen(url+"/igot/localmin/"+str(dict['taskid']))

			#print(url+"/igot/primenos/"+str(dict['taskid']))


			statfile = open(path_to_files+"projstat.txt", "w")

			statfile.write("havT") #We are assuming once the user runs the app, he is willing to run the project until it is completed.
			statfile.write("comF")
			statfile.write("uplT")

			statfile.close()

			#subprocess.call(["python3", "app.py"])

			break

		except:
			print("There seems to be a problem with the connection")
			print("Retrying....")
			i+=1
			time.sleep(3)
			pass

if __name__=='__main__':
	gettask('')