# Django REST API mini project

## Setup

- Make project directory

- Make requirements.txt

```
requirements.txt

django
djangorestframework
environs
```

- Install dependencies: Run:
pip3 install -r requirements.text

- Create new Django project: Run:
django-admin startproject mysite
  
// If the above command doesn't work, try:
python3 -m django startproject mysite

// This should create a new directory called "mysite."
cd mysite

- Create app: Run:
// Notice within the mysite directory, there is a file manage.py. This will help us create the app.
// The command startapp in manage.py takes a name arg. We will name the ap "api."
python3 manage.py startapp api

// A new directory called api should be created within mysite.


### Connecting the app with the Django project


 














