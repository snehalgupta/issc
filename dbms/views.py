from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subtask
from .serializers import SubtaskSerializer
import subprocess

# Create your views here.

class Exportlist(APIView):
	def get(self, request):
		subtasks = Subtask.objects.filter(status="NA")
		i = subtasks[0]

		i.status="A"
		i.save()
		
		subprocess.call(["python3","../../test.py"])
		serializer = SubtaskSerializer(i)
		return Response(serializer.data)


def GetData(request, tid, res):
	entrytid = tid#request.GET.get(id=tid)
	entryres = res#request.GET.get('nop')
	entrylist = list(Subtask.objects.filter(taskid=entrytid))
	entry = entrylist[0]
	entry.result=entryres
	entry.status="C"
	entry.save()
