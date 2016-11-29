from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Subtask(models.Model):
      projectid=models.CharField(max_length=50, default = "primenos")
      taskid=models.CharField(max_length=20)
      status=models.CharField(max_length=20)
      task=models.CharField(max_length=10)
      result=models.CharField(max_length=100, default='0')   
      def __str__(self):
          return self.taskid
class Project(models.Model):
	projectid=models.CharField(max_length=20,default=None)#,primary_key=True)
	project_name=models.CharField(max_length=20,default=None)
	project_desc=models.TextField(default=None)
	project_type=models.CharField(max_length=20,default=None)
	#userprofiles=models.ForeignKey("UserProfile",blank=True,null=True, related_name="Users")
	def __str__(self):
		return self.projectid


class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #projects=models.ForeignKey("Project", related_name="Users")
    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs): 
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

#in settings.py

       
