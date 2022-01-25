# This is simple project like TaskBook

This project is use Python, Django, Django REST Framework and Postgresql
Using simple email sender.

# Table of Contents:
    testtaskDisoftproject - main project
    account - account app
    task_app - task app
# How to Install and Run the Project:
    To install and run project successfully you should have:
        python version >= 3.7
        Django >= 4.0
            django-rest_framework
        psycopg2 >= 2.9.3

To run this project locally, you need to download this repository. Install previous libraries. Connect this project to your database.
Then complete all migrations and create a superuser:
            python manage.py makemigrations
            python manage.py migrate
            python manage.py collectstatic
            python manage.py createsuperuser
After that open the CLI in your project folder, and run the server.
        python manage.py runserver
Or you can run this project with docker. But firstly you must edit docker-compose.yml(chang all environment variable for this project).
After that just need to open the console, write this command:
    docker-compose build
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py collectstatic
    docker-compose run web python manage.py createsuperuser
 and run docker compose:
    docker-compose up

Url address to use on localhost
To use all api url you should also be registered and have token.
Using Postman variable which you can take from 'New task variable.postman_environment.json'
for creating or editing new task used json like this
{
    "title": "New Some text Title",
    "content": "Some text for task",
    "whom_entrusted": [
        1,
        2
    ]
}
# For task #
{{localhost}}{{tasks}}{{task_view}}<title> - view one task
{{localhost}}{{tasks}}{{task_view}}<title>/update - edit task
{{localhost}}{{tasks}}{{task_view}}<title>/delete - delete task
{{localhost}}{{tasks}}{{task_create}} - create new task
{{localhost}}{{tasks}}{{all_tasks}} - view all tasks
# For create and take a token #
{{localhost}}{{account}}register - register new user
{{localhost}}{{account}}login - login and take toke
Or enter url manually
# task url
http://localhost:8000/api/task_view/<title> - view one task
http://localhost:8000/api/task_view/<title>/update - edit task
http://localhost:8000/api/task_view/<title>/delete - delete task
http://localhost:8000/api/task/create - create new task
http://localhost:8000/api/tasks/all_tasks - view all tasks
# For create user and take a token #
http://localhost:8000/api/account/register - register new user
http://localhost:8000/api/account/login - login and take toke

Code formatted with Black.
After creating a new task, the message is sent by mail to those people who have to complete the task.