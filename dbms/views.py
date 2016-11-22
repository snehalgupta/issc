import datetime
from .models import Subtask
from django.http import HttpResponse,JsonResponse
import zipfile
import subprocess

def allot_time():
	file = open('./dbms/time.txt', 'r')
	l=file.readlines()
	now = datetime.datetime.now()
	c=[]
	file.close()
	for k in range(len(l)):
		i=l[k]
		prid = i[:i.find('/')]
		tid = i[i.find('/')+1:i.find(' -')]
		time = i[i.find('> ')+2:]
		time = time.rstrip('\n')
		t = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
		if (now-t)>datetime.timedelta(0,60,0):
			j = Subtask.objects.filter(projectid=prid,taskid=tid)
			subt = j[0]
			subt.status="NA"
			subt.save()
			c.append(k)
	indcompen = 0
	for z in c:
		l.pop(z-indcompen)
		indcompen+=1
	file=open('./dbms/time.txt', 'w')
	for a in l:
		file.write(a)
	file.close()

# Create your views here.
def ExportSubtask(request, prid):
	pid = prid
	subtasks = Subtask.objects.filter(projectid=str(pid), status='NA')
	if len(subtasks)==0:
		allot_time()
		subtasks = Subtask.objects.filter(projectid=str(pid), status='NA')

	if len(subtasks)==0:
		subtaskta = Subtask.objects.filter(projectid=str(pid), status='TA')
		if len(subtaskta)>0:
			response = JsonResponse({'check after':'75 seconds','prid':prid})
			return response
		else:
			response = JsonResponse({'alltasks':'done','prid':prid})
			return response
	else:
		i = subtasks[0]
		i.status="TA"
		i.save()
		t=datetime.datetime.now()
		time=open('./dbms/time.txt', 'a')
		time.write(i.projectid+"/"+i.taskid+" -> "+str(t)+'\n')
		time.close()
		response = JsonResponse({'prid':str(i.projectid),'taskid':str(i.taskid),'task':str(i.task)})
		return response

'''def CnfmDelivery(request, tid):
	deltask=Subtask.objects.filter(taskid=tid)
	if deltask.status=="NA":
		deltask.status="A"
		deltask.save()
	else:
		response = JsonResponse({'alltasks':'done'})
		return response'''

def GetData(request, tid, res, prid):
	entrytid = tid
	entrypid = prid
	entryres = res
	entrylist = list(Subtask.objects.filter(projectid=entrypid,taskid=entrytid))
	entry = entrylist[0]
	entry.result=entryres
	entry.status="C"
	entry.save()
	response = JsonResponse({'tid':str(entrytid),'conv':'True'})
	return response
		

def Download(request):
    zip_file = zipfile.ZipFile('setup_primenos.zip','r')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'setup_primenos.zip'
    return response



def Change(request, prid, tid):
	pid=prid
	id=tid
	subtasks=list(Subtask.objects.filter(projectid=pid, taskid=id))
	i=subtasks[0]
	i.status='A'
	l=open('./dbms/time.txt', 'r')
	m=l.readlines()
	l.close()
	'''l=open('./dbms/time.txt', 'w')
	l.close()'''
	for j in range(len(m)):
		#k=m[j]
		#prid2 = k[:k.find('/')]
		#tid2 = k[k.find('/')+1:k.find(' -')]
		#if(pid!=prid2 and id!=tid2):
		#	l=open('./dbms/time.txt', 'a')
		#	l.write(k)
		#	l.close()
		if (prid+'/'+tid) in m[j]:
			m.pop(j)
			break

	file=open('./dbms/time.txt', 'w')
	for a in m:
		file.write(a)
	file.close()
	i.save()

def GetFile(request,prid,tid):
	entrytid=tid
	if request.method=='POST':
		file = request.POST#['file']
		file1 = open('result_'+tid+'.txt','w+')
		#file1.write(str(file))
		file1.write(file['file'])#.decode("utf-8").decode("utf-8"))
		response = JsonResponse({'tid':str(entrytid),'conv':'True'})
		return response
		#return HttpResponse(str(file))
		#file1 = open('wtest.txt','w')
		#file1.write(file)
		#return HttpResponse("sweet")