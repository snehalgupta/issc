# issc
A project based on distributive computing.Divides the tasks of a project into smaller independent subtasks and distributes them to several computers via Internet.We did this as Extra Credits project for Systems Management course.

Introduction: One way to solve the problem of computing infrastructure is simply to get a super computer. But nowadays there are too many heavy duty projects in need of computing. It is neither practically possible to give each of them their requirements, nor to overlook their importance. It is however possible to classify their computing needs. Many projects, especially those involving data analysis, or some calculations, can be divided into many smaller independent subtasks. These subtasks can then be distributed to smaller computers, the whole system acting as a supercomputer. This is the basic idea behind our project. Only, we distribute these tasks over the largest network of computers possible - The Internet. To volunteers willing to give the idle time of their running computers towards such projects. The success of a similar project, on a much larger scale - Berkley Open Infrastructure for Network Computing (BOINC), inspired us to work on this project.

Review of Literature / Pre requisites for the project: 
https://tutorial.djangogirls.org/en/ - Tutorial on the basics of Working with Django.

Technology used:
We did our project using Django framework, for the back end of our servers.
For our applications on the volunteers systems, we have built a python application, with multiple modules, on the basis of python 3. This application communicates with the server to exchange task information.
We have used HTML and CSS for the website that is the user interface for the users volunteering to our project. This website helps a great deal in managing user data.


Methodology/Word carried out :

First of all,we created a django project named issc by writing the following command in linux shell:
django-admin startproject issc 
django-admin.py is a script that will create the directories and files for us.
Now we have the following directory structure:
issc
├───manage.py
└───issc
    	settings.py
    	urls.py
    	wsgi.py
    	__init__.py
manage.py is a script that helps with running and management of the site. With it we start a web server on our computer, manage the site database and many other things.
The settings.py file contains the configuration of the website.
The urls.py file contains a list of url patterns of our application.

Then we created an application dbms using the command:
python manage.py startapp dbms
This creates the following directory structure:
issc				     -------------> the root directory of the site
├── dbms			     -------------> The directory for the app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── issc				----------> The main site directory
	├── __init__.py
	├── settings.py
	├── urls.py
	└── wsgi.py

Next, we initialised our database by creating models in models.py. 
Each model corresponds to a database table, and each attribute corresponds to a database column.
We defined three models in models.py:
1.Subtask:This model contains information about the subtasks of all projects. It consists of attributes- projectid,taskid,status,task,result
2.Project:This model contains information about all the projects hosted on our server. It consists of attributes - projectid, project_name, project_desc, project_type
There are two types of projects we currently host - type 1 and type 2. The difference is in the way their subtasks are communicated. Type 1 subtasks are communicated by GET requests, while Type 2 subtasks are communicated by POST requests.
3.UserProfile:This model defines the user profile of a user. The user model in built in django is difficult to customise, and thus it is very convenient to create a new model which is simply linked to the user model. It consists of username and the projects chosen by the user.
Whenever we make changes in models.py,we type the following commands  to make Django know that we have made changes in our model. This is because django does the management of the models in the database, and you need to inform it about the changes you made, so it can adjust its working accordingly.

python manage.py makemigrations dbms    (What are the changes that occured - “migrations”)
python manage.py  migrate			(Apply the migrations (changes) into the database 
                                                                         file.)

We need an admin user to manage the database - add, edit, delete or simply view the data in the database manually.So, we created a superuser snehal10. A superuser/admin is a user account that has control over everything on the site. 
This can be done by the following command:
python manage.py createsuperuser
In order to make our model visible on the admin page, we registered the model by writing the following in admin.py.

from django.contrib import admin
from .models import Subtask

admin.site.register(Subtask)



Next, we run the server by writing the command - python manage.py runserver. This runs a server on our own system, and for our own system only, with the address http://127.0.0.1/. Then, we open the url 127.0.0.1:8000/admin.This is what we get:





Django has in built infrastructure for the very basics of a web app -  like users, admins, model management etc. And so we get our admin interface, from where we will manage the database of our site without having to create this front end.

Next, we have views of our application in views.py. Views are responsible for delivering web pages. Each view is represented by a simple python function. And these functions are, usually, attached to (or rather called by) URLs. These function execute what we want to happen at the back end of a web page, including communications with the user. And, as the name suggests, to program the view of the site.
We have the following functions:

1.ExportSubtask()-This function is for delivering the tasks of type1 projects (GET requests) to the user, or the program that requests. It returns a json string containing a task which is “Not Assigned”. It changes the status of NA(not assigned) tasks to TA(temporarily assigned). If there are zero NA tasks, then it changes the status of tasks which have been temporarily assigned (TA) for more than 60 seconds to NA by calling the allot_time function. This is to ensure no task is blocked.
2.allot_time()-This function changes the status of  tasks which have been temporarily assigned (TA) for more than 60 seconds to NA by making use of time.txt. This file stores information about the TA tasks in the following form:
< projectid > / < taskid > -> < time at which task was assigned or temporarily assigned >
TA tasks basically means those tasks, which although were delivered are not confirmed of reaching the user program. We can’t block tasks by labelling them A without confirmation (this also acts as security against bogus requests)

3.GetData()-This function is for the recieving the results for subtasks of projects of type 1. It takes taskid,result,projectid as a parameter and updates the status of the corresponding subtask  to ‘C’ (completed) and stores the result received as a parameter in the result field of subtask.
4.Download()-This function enables downloading the setup file of the project whose projectid has been passed as a parameter to the function.




5.Change()-This function confirms whether a user got the task. It takes the project id and task id as parameter and changes the status of the corresponding task to “A” and  removes those entries from time.txt whose status has been changed to “A”.

6.user_new():This function is what gives us the user registration page. It returns the webpage userregister.html as a web response. It uses the form created in forms.py to store the input of the user.This function creates a user object with username entered as input to the form displayed on the page


7.addproject():This function returns the webpage projectmgmt.html as a web response. It is the function which works on adding a project to the list of the projects user is contributing to. The webpage projectmgmt.html displays the projectids of the projects available and allows the user to add projects.The projects added by the user get stored in the ‘projects’ field of UserProfile model.


8.delproject():This function returns the web page projectmgmt1.html as a web response.The web page projectmgmt1.html displays the projectids of the projects which have been added by the user 


.
Now, we have the URLs file, where the url linking to the views functions is done. The following are the url patterns we have. 


127.0.0.1:8000/ : maps to the home page.
127.0.0.1:8000/register : maps to the user registration page.
127.0.0.1:8000/login : maps to the login page.
127.0.0.1:8000/logout : maps to the logout page  
127.0.0.1:8000/export/project_id : maps to the ExportSubtask function . 
127.0.0.1:8000/done/project_id/task_id/result : maps to the GetData function .  
127.0.0.1:8000/download/project_id : maps to the Download function .
127.0.0.1:8000/igot/project_id/task_id : maps to the Change function .  
127.0.0.1:8000/addproject : maps to the addproject function .
127.0.0.1:8000/delproject : maps to the delproject function .
127.0.0.1:8000/download_userfile/username : maps to the download_userdata function . 


The backbone for the user interaction in our website. It is a way user can input various types of data, and our views can access it. The forms display and managed by 

We also have to create the project databases - the subtasks, the files to upload/download etc.

Next,we deployed the project using PythonAnywhere by referring to the following tutorial:
https://tutorial.djangogirls.org/en/deploy/


