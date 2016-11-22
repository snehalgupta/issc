from urllib.request import urlopen
import json
import subprocess
count=0
cnfm=True
while (cnfm and count<15):
	file = open("result.txt", "r")

	s=file.read()

	res=s[:s.find(":")]
	tid=s[s.find(":")+1:]
	file.close()

	print("Uploading T Id"+tid+"...")

	#url="http://snehalgupta.pythonanywhere.com/done/"+str(tid)+"/"+str(res)
	url="http://127.0.0.1:8000/primenos/done/"+str(tid)+"/"+str(res)+"/"

	#print(url)

	obj=urlopen(url)
	obj2=obj.read()
	obj3=obj2.decode("utf-8")

	dict = json.loads(obj3)
	#print(dict)
	if (dict['conv']=='True'):
		cnfm=False
		print("Uploaded Results for T Id"+tid)
	count+=1
	subprocess.call(["sleep","5s"])




statfile = open("Projectfiles/projstat.txt", "w")

statfile.write("havF")
statfile.write("comF")
statfile.write("uplT")

statfile.close()

subprocess.call(["python3", "app.py"])
