
from .models import Subtask
from django.http import HttpResponse,JsonResponse
import zipfile
#import subprocess

# Create your views here.

def ExportSubtask(request):
	subtasks = Subtask.objects.filter(status="NA")
	i = subtasks[0]
	#i.status="A"
	#i.save()
	response = JsonResponse({'prid':str(i.projectid),'taskid':str(i.taskid),'task':str(i.task)})
	return response


def GetData(request, tid, res):
	entrytid = tid
	entryres = res
	entrylist = list(Subtask.objects.filter(taskid=entrytid))
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
	
	
