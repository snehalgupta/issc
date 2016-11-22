from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import subprocess
import time

def upload(path_to_files):

	count=0
	cnfm=True
	while (count<15):
		file = open(path_to_files+"result.txt", "r")

		s=file.read()

		tid=s[:s.find(":")]
		
		file.close()

		print("Uploading Results of T Id"+tid+"...")

		#url="http://snehalgupta.pythonanywhere.com/done/"+str(tid)+"/"+str(res)
		url="http://127.0.0.1:8000/done/localmin/"+str(tid)+"/"

		#print(url)

		file = open('result.txt', 'r')
		a = file.read()
		print(str(file),a)
		post_fields = {'file': a }     # Set POST fields here

		try:

			request = Request(url, urlencode(post_fields).encode())
			json1 = urlopen(request).read().decode("utf-8")
			print(json1)
			D = json.loads(json1)
			#print(dict)
			if (D['conv']=='True'):
				print("Uploaded Results for T Id"+tid)
				break

			statfile = open(path_to_files+"projstat.txt", "w+")

			statfile.write("havF")
			statfile.write("comF")
			statfile.write("uplT")

			statfile.close()

		except:
			print("There seems to be some problem with the connection")
			print("Please check your connection")
			print("Retrying......")
			pass

		'''obj=urlopen(url)
		obj2=obj.read()
		obj3=obj2.decode("utf-8")'''

		
		count+=1
		time.sleep(5)
		#subprocess.call(["sleep","5s"])




	'''statfile = open("localmin_files/projstat.txt", "w+")

	statfile.write("havF")
	statfile.write("comF")
	statfile.write("uplT")

	statfile.close()'''

	#subprocess.call(["python3", "app.py"])

if __name__=='__main__':
	upload('')