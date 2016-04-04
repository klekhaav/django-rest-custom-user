# Django|REST extended user module 

This is a full Django project with application wich etends basic user model. All Views built with using RESTfull api and latest Bootstrap. 

## Getting Started

To run you need to Python and working virtual environment. Package requirements:

```
Django 1.9.5
django-cors-headers 1.1.0
djangorestframework 3.3.3
python-dateutil 2.5.2
```

### Prerequisities

To start virtual environment you need to run this commands in you terminal

First off all install python and pip

```
$ sudo apt-get install python python-dev pip
$ pip install virtualenv
```

To start and activate you virtual environment:

```
$ cd to/project/directory
$ virtualenv .env
$ source .env/bin/activate
```

If all is ok, you'll see that you command line prefix changed to "(.env)$"


### Installing

Second step to run project is to install all requirement, In project directory you can find requirements.txt file with a list of all packages what you need.
To install them you need to run command:

```
(.env)$ pip install -r requirements.txt
```

After all installation will done you must create database and superuser.

```
(.env)$ python manage.py makemigrations
(.env)$ python manage.py makemigrations accounts
(.env)$ python manage.py migrate
(.env)$ python manage.py createsuperuser
```

Now you have personal superuser :)
Lets start django

```
(.env)$ python manage.py runserver
```

## Take a ride

Now you can take a look at the Django admin panel, just open in you browser address field:

```
localhost:8000/admin
```
and login with you username and password

You can find 2 new fields in User > You_username
 
In the project built RESTfull api view for all users you can visit that page on

```
localhost:8000/api/users_ext
```
But beware to see anything you must be 13 years old, just put you birthday in users field.

There is we have two simple views for users, you can find it at 

list of all users at 

```
localhost:8000/users
```

and detail view for every user by clicking on wrench in the table, or if you know the user id 
 
```
localhost:8000/user/id
```

id - must be an integer value (first user allways has id = 1)

## Authors

* **Oleksandr Klekha** - [klekhaav](https://github.com/klekhaav)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
