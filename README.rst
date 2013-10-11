{{ project_name|title|lower }}
========================

django-admin.py startproject --template=https://github.com/3atmospheres/django-project-template/archive/master.zip --extension=py,rst,html your_awesome_project_name

Getting Started
---------------

First, create the virtual environment:

    $ mkvirtualenv {{ project_name|title|lower }}

In the `{{ project_name|title|lower }}` directory, install the dependencies using pip and the `requirements.txt` file:

    ({{ project_name|title|lower }}) $ cd {{ project_name|title|lower }}
    ({{ project_name|title|lower }}) $ pip install -r requirements.txt

This will take care of the base requirements for your project.

Next, you'll need to create the PostgreSQL database called `{{ project_name|title|lower }}` and grant the `user` with all privileges to the database.  Fill in the `user` and `password` of your choosing in the `{{ project_name|title|lower }}/settings/local.py` file.

Depending on how you manage your PostgreSQL setup locally, we will omit these steps as it will vary from user to user.

After you have created the database and properly granted the `user` specified in `local.py` with the correct privileges, you should be able to sync the database and create the core tables, as well as create your local superuser for the application:

    ({{ project_name|title|lower }}) $ python manage.py syncdb

And now you should be all set to start coding your application!
