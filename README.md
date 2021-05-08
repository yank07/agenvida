# agenvida
Horario espiritual On-Line version app



```bash

sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev

virtualenv venv
source venv/bin/activate
pip install -r requierements.txt

```

Start a Django project

First, we need to create a directory for your project.

$ mkdir myfolderproject

$ cd myfolderproject

This directory will contain both the virtual environment and the Django application. We create a new virutal environment, called myenv:

$ virtualenv myenv

$ source myenv/bin/activate

where the second line activates the virtual environment. Anytime, you can exit the virtual environment typing deactivate.

In order to install Django, we will use the django-toolbelt, which includes the following packages:

– django

– psycopg2

– gunicorn (WSGI server)

– dj-database-url (a Django configuration helper)

– dj-static (a Django static file server)

With your virtual environment active:

$ pip install django-toolbelt

By the time I wrote this post, the version of Django installed was Django 1.6.1.

Finally, let’s create the Django project:

$ django-admin.py startproject myproject .

The dot at the end indicates that the app will be installed without creating an additional folder.

Dependencies

One importand and useful thing is to have different virtual environments for developing, production and testing. Inside myprojectfolder, create a requirements folder with the requirements files for developing, testing and production:

$ mkdir requirements

$ touch requirements/{common.txt,dev.txt,prod.txt,test.txt}

First, we will write the packages on the actual environment (which will be used for production) to the common.txt file:

$ pip freeze > requirements/common.txt

And then, add the following line to the other .txt files:

-r common.txt

followed by the packages needed for that environment. This line tells pip to include the dependencies in that file. Here, there are some examples of packages and the environment in which they usually belong:

Common: django, django-ajaxice, django-pagination, django-tastypie, South

Dev: django-debug-toolbar

Prod: gunicorn, psycopg2

Test: coverage, nose

After setting your requirements, create another virtual environment for developing and for testing.

$ virtualenv devenv

$ virtualenv testenv

Activate each of them and install the dependencies indicated in each requirement file. For example, for the developing environment:

$ source devenv/bin/activate

$ pip install -r requirements/dev.txt

Django settings

Open your settings.py file and change or add the following lines to configure the static files:

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = False
TEMPLATE_DEBUG = DEBUG
STATIC_URL = ‘/static/’
STATIC_ROOT = ‘staticfiles’
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, ‘static’),
)
Edit this file with your production database configuration. For more information on how to set PostgreSQL on your computer and on Heroku take a look at this post.

Create two different setting files for development and testing, located at the same level of settings.py.

touch development_settings.py test_settings.py

These files will contain the settings that are specific to this environment, but also import all the global settings (which in this case is the file settings.py). Write, in each of these files:

# -*- coding: utf-8 -*-

from .settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

Note: the dot before settings is not a typo :-) And after these lines, redefine the Database parameters for your development and testing environments. Again, if you are using PostgreSQL check this post.

To use each file correctly, we need to indicate it to the corresponding virtual envirnoment. For the development environment, append this to your bin/activate script:

DJANGO_SETTINGS_MODULE=”myproject.development_settings”

export DJANGO_SETTINGS_MODULE

In the script bin/activate of the virtual environment for testing:

DJANGO_SETTINGS_MODULE=”myproject.test_settings”

export DJANGO_SETTINGS_MODULE

OS X Mavericks Error: When working with these virtual environments, if you run

$ python manage.py validate

you might see an error with something like:

Referenced from: myvirtualenv/lib/python2.7/site-packages/psycopg2/_psycopg.so

Reason: image not found

To solve this error, open the bin/activate script and add the following line:

export DYLD_LIBRARY_PATH=/Library/PostgreSQL/9.*/lib
where you should replace * for your PostgreSQL version.

