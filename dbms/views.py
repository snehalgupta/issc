from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subtask
from .serializers import SubtaskSerializer

# Create your views here.

class Exportlist(APIView):
	def get(self, request):
		subtasks = Subtask.objects.filter(status="NA")
		i = subtasks[0]

		i.status="A"

		serializer = SubtaskSerializer(i)
		return Response(serializer.data)
