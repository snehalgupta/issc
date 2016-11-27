import urllib.request

import json

import subprocess

import time

import sqlite3

def gettask(path_to_files):
	i=0

	while(i<10):
		try:
			print("Getting a task...")
			#url="http://snehalgupta.pythonanywhere.com"
			url="http://127.0.0.1:8000"
			#print(url+"/export")
			obj=urllib.request.urlopen(url+"/export/localmin")
			#obj2=obj.read()
			#obj3=obj2.decode("utf-8")

			#f = urllib2.urlopen(url)
			data = obj.read()
			print(data)
			try:
				data=data.decode('utf-8')
				obj3 = data[:data.find('}')+1]
				dict = obj3
				#print("Got Taskid - "+dict['taskid'], "Task - "+dict['task'])
				if dict=={'alltasks':'done'}:
					print("Hurray! all tasks of this project are done!")
					break
			except :#ZeroDivisionError:
				pass

			with open(path_to_files+'task.db', "wb+") as code:
				code.write(data)

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
			
			try:
				cnfm=urllib.request.urlopen(url+"/igot/localmin/"+tid)
			except:
				pass

			#print(url+"/igot/primenos/"+str(dict['taskid']))


			statfile = open(path_to_files+"projstat.txt", "w")

			statfile.write("havT") #We are assuming once the user runs the app, he is willing to run the project until it is completed.
			statfile.write("comF")
			statfile.write("uplT")

			statfile.close()

			#subprocess.call(["python3", "app.py"])

			break

		except ZeroDivisionError:
			print("There seems to be a problem with the connection")
			print("Retrying....")
			i+=1
			time.sleep(3)
			pass

if __name__=='__main__':
	gettask('')