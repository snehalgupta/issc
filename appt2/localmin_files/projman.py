def runproj(username):

	import main,up,getdata

	path='localmin_files/'

	file=open(path+"projstat.txt",'r')
	l2=file.readlines()
	l=l2[0]
	file.close()
	#file1=open(path_to_files+"task.txt",'r')
	#l1=file1.read()
	#file1.close()

	if l[l.find('v')+1]=='F':
		a=False
	else:
		a=True
	havtask= a# and (len(l1)>0))

	if l[l.find('m')+1]=='F':
		a=False
	else:
		a=True
	completed = a

	uploaded = l[l.find('l')+1]

	#print(havtask,completed,uploaded)



	if uploaded=='F':
		up.upload(path)
		#subprocess.call(["python3", "primenos_files/up.py"])

	elif havtask:
		main.dotask(path)
		#subprocess.call(["python3", "primenos_files/main.py"])

	else:
		getdata.gettask(path)
		#subprocess.call(["python3", "primenos_files/getdata.py"])
