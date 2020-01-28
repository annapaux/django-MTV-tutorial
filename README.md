# Welcome!

This app mainly serves the purpose to show all modules of the 'Model View Controller' design, or in Django's case, the 'Model Template View' structure. Features such as superuser or authentication are not used in this app.

To run this app, download the zip file, navigate to the folder and run the following commands

optionally create a virtual environment
`python3 -m venv 'coffee-venv'`
`source coffe-venv/bin/activate`

navigate to: .../coffee-app/coffee_project
`python manage.py runserver`

Open the website in the browser: http://127.0.0.1:8000/


![alt text](https://github.com/annapaux/django-coffee-MTV/blob/master/coffee_img.png)

# Replicate this app

### Tutorial Resources
Below are mainly commands for replicating the website. Fore more information on functionalities look at the documentation and the below tutorials:

Tutorial for initial set up:
https://djangocentral.com/create-a-hello-world-django-application/

A detailed (though occasionally outdated) tutorial:
https://www.tutorialspoint.com/django/django_quick_guide.htm
Relevant sections: Views, Templates, Django Template Language (DTL), Other Data Manipulation


## 1 - Set up a Django project
```
mkdir coffee
cd coffee
python3 -m venv 'coffee-venv'
source coffe-venv/bin/activate

pip install Django
mkdir coffee-app
cd coffee-app

django-admin startproject coffee_project
```

At this point you should be able to see a django starter page on http://127.0.0.1:8000/
Click 'ctrl + c' to stop the server. (NOT 'z')

## 2 - Create a Django app
```
python manage.py startapp app
```
In `settings.py` add `'app'` to `INSTALLED_APPS`

Open the `views.py` file and have it look like this:
```
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!')
```

Open the `urls.py` file and have it look like this:
```
from django.contrib import admin
from django.urls import path
# imported views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # configured the url
    path('',views.index, name="index")
]
```

Run  `python manage.py runserver` and visit http://127.0.0.1:8000/ to see 'Hello World' on the web page.


## 3 - Create template
Create a templates folder in your app and add an `index.html` file such that the path looks like `coffee-app/coffee_project/app/templates/index.html`.

Paste in the following. The {{ today }} variable refers to the today variable that will be defined in a method in `views.py`. The {% for user in users %} loop iterates over the list of users that also will be defined in `views.py`
```
<html>

   <body>
      <h1>Hello there!</h1>
      <p>Today is {{ today }} </p>
      Time for coffee!

      <h3>Current users:</h3>
      {% for user in users %}
        <p> {{ user.name }} who you can contact at {{ user.email }} </p>
      {% endfor %}
   </body>

</html>

```

## 4 - Create view
In `app/views.py` change the file to look like the below. The index function renders data in the form of a dictionary to the previously specified template (`index.html`). The `User` model will be created later when we generate fake data. We query it here to get all the current users and feed it to the template, which then iterates over it with a for loop.
```
from django.shortcuts import render
from django.http import HttpResponse

from app.models import User
import datetime

def index(request):
    today = datetime.datetime.now().date()
    users = User.objects.all()
    data = {'today':today, 'users':users}
    return render(request, "index.html", data)

```

## 5 - Models
In `app/models.py` edit the file to look like the below. We import Django's models class, and generate a model, that can be understood like a table in the database. Each specified variable is a column (name, email, phone).

```
from django.db import models

class User(models.Model):

   name = models.CharField(max_length = 50)
   email = models.CharField(max_length = 50)
   phone = models.IntegerField()

   class Meta:
      db_table = "user"

```

Run the following from the command line. Every time a change is made to the database, the changes need to be migrated.
```
python manage.py makemigrations
python manage.py migrate
```

To generate fake entry data, do the following:
Open Django's shell:
```
$python manage.py shell
```
In the shell run the following commands:
```
from app.models import User
u = User()
u.name = 'Maria'
u.email = 'maria@gmail.com'
u.phone = '0123456789'
u.save()

u = User()
u.name = 'Nguyen'
u.email = 'nguyen@gmail.com'
u.phone = '2345678901'
u.save()
```
Exit the shell with `ctrl+z`. Migrate the data and start the server. Navigate to http://127.0.0.1:8000/ to see your entries.

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Tada!
You have a Model-View-Control or Model-Template-View application!
