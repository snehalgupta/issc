from django.db import models

# Create your models here.

class Subtask(models.Model):
      projectid=models.CharField(max_length=50, default = "primenos")
      taskid=models.CharField(max_length=20)
      status=models.CharField(max_length=20)
      task=models.CharField(max_length=10)
      result=models.CharField(max_length=10, default='0')   
      def __str__(self):
          return self.taskid
       
