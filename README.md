# Blog Application: Development

Blogcorn is an open-source platform built on the Django Web Framework. It is going to be developed as an ecosystem of reusable Django apps, and starter project templates.

This app was developed as part of the Cornstack ecosystem but is just a Django app and can be used independently.

## Django version

- Django - 1.8.9 LTS

## For developers, From developers

Blogcorn Django app is for developers only who know how to setup virtual environment and Django project.

## Dependencies

There is no dependencies as such. You can setup Blogcorn using virtual environment or Vagrant. Choice is yours.

## Installation

Run the following commands:
```
git clone https://github.com/nescode/blogcorn.git
cd blogcorn
pip install -r requirement.txt
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

To setup static and media for project, just create following folder inside root project folder:
- static
- static_cdn
- media
- media_cdn

## Available features details

- Writing a blog
- Add an image
- Store as draft and publish on later date
- All the default features of Django framework

## Django development company

We are passionate technologists. We offer full stack development and consulting for organizations with Python, Django framework and PostgreSQL. Drop us a line at info@nescode.com to shape your idea.
