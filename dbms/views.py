import datetime
from .models import Subtask,Project,UserProfile
from django.http import HttpResponse,JsonResponse
import zipfile
import subprocess
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate,login
#from django.views import View
from django.views.generic import FormView
from .forms import UserForm,Projectmgmt
from django.contrib.auth.models import User

path='/home/issc/issc/'

def allot_time():
	file = open(path+'dbms/time.txt', 'r')
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
	file=open(path+'dbms/time.txt', 'w')
	for a in l:
		file.write(a)
	file.close()

# Create your views here.
def ExportSubtask(request, prid):
	pid = prid
	subtasks = Subtask.objects.filter(projectid=str(pid)).filter(status='NA')
	if len(subtasks)==0:
		allot_time()
		subtasks = Subtask.objects.filter(projectid=str(pid)).filter(status='NA')

	if len(subtasks)==0:
		subtaskta = Subtask.objects.filter(projectid=str(pid)).filter(status='TA')
		if len(subtaskta)>0:
			response = JsonResponse({'check after':'60 seconds','prid':prid})
			return response
		else:
			response = JsonResponse({'alltasks':'done','prid':prid})
			return response
	else:
		subtask = subtasks[0]
		ptype = Project.objects.get(projectid=subtask.projectid).project_type
		if (ptype == '1'):

			i = subtask
			i.status="TA"
			i.save()
			t=datetime.datetime.now()
			time=open(path+'dbms/time.txt', 'a')
			time.write(i.projectid+"/"+i.taskid+" -> "+str(t)+'\n')
			time.close()
			response = JsonResponse({'prid':str(i.projectid),'taskid':str(i.taskid),'task':str(i.task)})
			return response
		elif (ptype=='2'):
			i = subtask
			i.status="TA"
			i.save()
			t=datetime.datetime.now()
			time=open(path+'dbms/time.txt', 'a')
			time.write(i.projectid+"/"+i.taskid+" -> "+str(t)+'\n')
			time.close()
			file1 = open(path+pid+'_datafiles/task_'+i.taskid+'.db','rb')
			response = HttpResponse(file1, content_type='application/force-download')
			response['Content-Disposition'] = 'attachment; filename="%s"' % ('task_'+str(i.taskid)+'.db')
			return response


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


def Download(request,prid):
    pid = prid
    zip_file = open((path+'setup_'+pid+'.zip'),'rb')#zipfile.ZipFile('setup_primenos.zip','r')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % ('setup_'+pid+'.zip')
    return response



def Change(request, prid, tid):
	pid=prid
	id=tid
	subtasks=list(Subtask.objects.filter(projectid=pid, taskid=id))
	i=subtasks[0]
	i.status='A'
	l=open(path+'dbms/time.txt', 'r')
	m=l.readlines()
	l.close()
	'''l=open(path+'dbms/time.txt', 'w')
	l.close()'''
	for j in range(len(m)):
		if (prid+'/'+tid) in m[j]:
			m.pop(j)
			break

	file=open(path+'dbms/time.txt', 'w')
	for a in m:
		file.write(a)
	file.close()
	i.save()
	response = HttpResponse("Ok, go on!")
	return response

def user_new(request):
	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			email=form.cleaned_data['email']
			user.set_password(password)
			user.email=email
			user.save()
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('home')
	else:
		form=UserForm()
	return render(request,path+'dbms/templates/dbms/studentregister.html',{'form':form})

def addproject(request):
	u = UserProfile.objects.get(user=request.user)
	proj = u.projects.all()
	projectslist = Project.objects.all()
	#projectlist should have only those projects which are not enrolled in by the user
	for i in proj:
		projectslist=projectslist.exclude(projectid=i.projectid)

	projectid=request.POST.get('dropdown1')

	if request.method == 'GET':
		form=Projectmgmt()

	else:

		a1 = Project.objects.get(projectid=projectid)
		u.projects.add(a1)
		uid = request.user.username
		file1=open(path+'dbms/userstat_'+uid+'.txt','w')
		file1.write(str(u.user)+"\n")
		for project in u.projects.all():
			file1.write(project.projectid+"-"+project.project_name+"\n")
		file1.close()

		return redirect('home')

	return render(request,path+'dbms/templates/dbms/projectmgmt.html',{'form':form, 'projectslist':projectslist})

def delproject(request):
	u=UserProfile.objects.get(user=request.user)
	projectslist=u.projects.all()
	projectid=request.POST.get('dropdown1')

	if request.method == 'GET':
		form=Projectmgmt()

	else:

		a1 = Project.objects.filter(projectid=projectid)[0]
		u.projects.remove(a1)
		uid = request.user.username
		file1=open(path+'dbms/userstat_'+uid+'.txt','w')
		file1.write(str(u.user)+"\n")
		for project in u.projects.all():
			file1.write(project.projectid+"-"+project.project_name+"\n")
		file1.close()
		return redirect('home')
	return render(request,path+'dbms/templates/dbms/projectmgmt1.html',{'form':form, 'projectslist':projectslist})




def download_userdata(request,uid):
	file1 = open(path+'dbms/userstat_'+uid+'.txt','r')
	response = HttpResponse(file1, content_type='application/force-download')
	response['Content-Disposition'] = 'attachment; filename="%s"' % "userstat_"+str(uid)+'.txt'
	return response

def GetFile(request,prid,tid):
	entrytid=tid
	entrypid=prid
	if request.method=='POST':
		filename = list(request.FILES.keys())[0]
		received_file = request.FILES[filename]
		with open(path+prid+'_datafiles/result_'+entrytid+'.txt', 'wb+') as new_file:
			new_file.write(received_file.read())

		s = Subtask.objects.filter(projectid=prid).get(taskid=tid)
		s.status='C'
		s.result=prid+'_datafiles/result_'+entrytid+'.txt'
		s.save()
		response = JsonResponse({'tid':str(entrytid),'conv':'True'})
		return response


