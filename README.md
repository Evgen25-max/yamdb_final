# Yambd. Yandex Praktikum - sprint 11
Implementation of the API for the YaMDb service - a database of reviews of movies, books, and music.
The YaMDb project collects user reviews of works of art. The works are divided into categories: "Books", "Movies", " Music»

## Functionality:
Full description of the functional part of the implemented API: see **/redoc/**.    
Receiving the confirmation code by email. Subsequent authorization with a JWT token.
Different user roles: administrator/moderator/user.
CRUD for: title, category, genre, review, comment.

What I used:
- [Django Version: 3.0.5](https://www.djangoproject.com/)
- [Django REST Version: 0.8.6](https://www.django-rest-framework.org/)
- [Simple JWT Version: 4.3.0](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [PostgreSQL Version: 13.1](https://www.postgresql.org/docs/13/release-13-1.html)

## Pre-installation
You need to install [docker](https://www.docker.com/products/docker-desktop "use the link if necessary") on your server 
## Getting Started

- Clone the repository to your server.
-  Create your own **.env** file. You can use the **.env.Example** file as a base. In the file, you must specify the data for the correct operation of the Django framework and the postgresql database:
   * DJANGO_SECRET_KEY
   * DB_ENGINE   
   * DB_NAME   
   * POSTGRES_DB
   * POSTGRES_USER
   * POSTGRES_PASSWORD
   * DB_HOST
   * DB_PORT
- Go to the root folder of the project and run the following commands (use ```sudo``` if superuser rights are required):
  - ```docker-compose up```
  - Log in to your container with the ```docker exec-it <CONTAINER ID> bash```    
    command, where <CONTAINER ID> is the container ID named "infra_sp2_web_1". Get your <CONTAINER ID>    
    with the ```docker container ls``` command.
    - Apply django migrate ```python manage.py migrate```    
    - Create superuser: ```python manage.py createsuperuser```   
    - Load the initial data, *if necessary*: ```python manage.py loaddata fixtures.json```
   
Use a request ```http://localhost:8000/api/v1/titles/``` to make sure everything works.
### Author:
- GitHub:  [github.com/Evgen25-max](https://github.com/Evgen25-max)


![example workflow file path](https://github.com/Evgen25-max/yamdb_final/workflows/yamdb_final-app/badge.svg)

