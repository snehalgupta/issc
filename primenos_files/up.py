from urllib.request import urlopen
import json
import subprocess
import time

def upload():

	count=0
	cnfm=True
	while (count<15):
		file = open("primenos_files/result.txt", "r")

		s=file.read()

		res=s[:s.find(":")]
		tid=s[s.find(":")+1:]
		file.close()

		print("Uploading T Id"+tid+"...")

		#url="http://snehalgupta.pythonanywhere.com/done/"+str(tid)+"/"+str(res)
		url="http://127.0.0.1:8000/primenos/done/"+str(tid)+"/"+str(res)

		#print(url)

		obj=urlopen(url)
		obj2=obj.read()
		obj3=obj2.decode("utf-8")

		dict = json.loads(obj3)
		#print(dict)
		if (dict['conv']=='True'):
			print("Uploaded Results for T Id"+tid)
			break
		count+=1
		time.sleep(5)
		#subprocess.call(["sleep","5s"])




	statfile = open("primenos_files/projstat.txt", "w")

	statfile.write("havF")
	statfile.write("comF")
	statfile.write("uplT")

	statfile.close()

	#subprocess.call(["python3", "app.py"])
