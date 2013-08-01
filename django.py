""" Django notes

djangoproject.com
> tar xzvf Django-1.5.1.tar.gz
> cd Django-1.5.1
> sudo python setup.py install

# Check if django installed correctly
> python -c "import django; print (django.get_version())"

# Creating a project, avoid names that are the same as built-in Python or Django components
> django-admin.py startproject mysite

# manage.py and django-admin.py 
# 	https://docs.djangoproject.com/en/1.5/ref/django-admin/

# Start the development server
> python manage.py runserver [port=8000]
# Can also do: python manage.py runserver 0.0.0.0:8000

# Database setup
# Edit stuff in mysite/settings.py
> python manage.py syncdb

## The following is for a "Poll"
	# Creating models
	> python manage.py startapp polls

	# Playing with the API
	> python manage.py shell

"""

"""
Other shenanigans to install :
# : brew, git, postgresql, psycopg

# Installing brew
> ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
> brew doctor

# Installing git
> brew install git

# Installing postgresql (9.2.4)
> brew install postgresql
# Since there's always an error when doing psql for the first time,
# 	http://ionrails.com/2012/06/03/installing-postgresql-on-a-mac-lion/

	# Create Database Cluster
	> initdb /usr/local/var/postgres

	# Create LaunchAgents directory if it doesn’t exist already
	> mkdir -p ~/Library/LaunchAgents

	# Setup file that allows you to Stop/Start the Postgres Server
	> cp /usr/local/Cellar/postgresql/9.2.4/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents

	# Start up PostgreSQL server when your system boots
	> launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

	# Create Database User
	> createuser your_db_user_name
	Shall the new role be a superuser? (y/n) n
	Shall the new role be allowed to create databases? (y/n) n
	Shall the new role be allowed to create more new roles? (y/n) n

	# Create Development and Test Databases
	createdb -Oyour_db_user_name -Eutf8 your_project_development
	createdb -Oyour_db_user_name -Eutf8 your_project_test

	# Set Postgres database passwords for Development Database
	> psql -U your_db_user_name your_project_development
	=> ALTER USER your_db_user_name WITH PASSWORD ‘whateverpasswordyouwant’;

	Set Postgres database passwords for Test Database
	> psql -U your_db_user_name your_project_test
	=> ALTER USER your_db_user_name WITH PASSWORD ‘whateverpasswordyouwant’;

	(You can set the default database by export'ing PGDATABASE environment variable
		in ~/.bashrc)
	export PGDATABASE=mydatabasename

# Installing psycopg (2.5.1)
# Download source package from http://www.initd.org/psycopg/download/
> cd ~/Downloads/psycopg2-2.5.1
> sudo python setup.py install
# Type in password



"""


























