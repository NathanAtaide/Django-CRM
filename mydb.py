# Python 3.11 

#python -m venv virt

# Baixando bibliotecas
# (virt) C:\Coding\CRMDjango>pip install mysql

# (virt) C:\Coding\CRMDjango>pip install django

# (virt) C:\Coding\CRMDjango>pip install mysql-connector-python

# (virt) C:\Coding\CRMDjango>pip install mysql-connector - NÃO INSTALAAAAAA


# Criando projeto e aplicação
# (virt) C:\Coding\CRMDjango>django-admin startproject dcrm

# (virt) C:\Coding\CRMDjango>cd dcrm

# (virt) C:\Coding\CRMDjango\dcrm>python manage.py startapp website

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = '1520')



#prepare a cursor object

cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crmdb")

print("All done")


#Execute this file to create this db using this python mydb.py
#Migrate build your db with python manage.py migrate

# create superuser winpty python manage.py createsuperuser - Usa winpty por causa do windows, se for mac ou linux não precisa - admin - administrator@

#python manage.py runserver


#git config --global user.name "Nathan Ataide"

#git config --global user.email "nathanataidebomfim@gmail.com"

#git config --global push.default matching

#git config --global alias.co checkout

#git init

