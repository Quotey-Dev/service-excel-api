


Below is the steps how to get virtual envirionment running and 
set up the pip freeze to get the installed files.



#########################################

USE PYTHON VERSION 3.7.4 

----- Step 1. Dowload from the official site of python
----- Step 2. While installing select "include in path"
----- Step 3. Open simple cmd, check python --version -> If it shows 3.7.4 then it is good
----- Step 4. Install pipenv here
----- Step 5. Go to Quotey folder, run pipenv shell
----- Step 6. run pip install -r requirements.txt
----- Step 7. Run python server.py ( if running on VM ) or
-----       . Run python manage.py runserver ( for running on your own machine )
----- Step 8. Make sure NGINX is running


HOW TO RUN NGINX on Windows?

----- STEP1. Download nginx from http://nginx.org/en/download.html for Windows ( version above or equal 1.19)
----- STEP2. Extract this packages wherever you like, preference is in c:/
----- STEP3. Replace the webproject_nginx.conf file (inside sites-enabled folder of nginx folder), with the same file in current project nginx_waitress/webproject_nginx.conf
----- STEP4. Inside conf folder, replace the file nginx with the nginx in this project which is nginx_waitress/nginx.conf
             Make sure the path for webproject_nginx.conf file is correct as per the location and version of nginx
----- STEP5. double click on nginx.exe this will run the nginx. To double check it, check it on the task manager of windows






#########################################







- (base) C:\Users\darsh\Desktop\localQuotey\Quotey>pip install pipenv
Collecting pipenv
  Downloading https://files.pythonhosted.org/packages/13/b4/3ffa55f77161cff9a5220f162670f7c5eb00df52e00939e203f601b0f579/pipenv-2018.11.26-py3-none-any.whl (5.2MB)
     |████████████████████████████████| 5.2MB 1.7MB/s
Requirement already satisfied: virtualenv in c:\users\darsh\anaconda3\lib\site-packages (from pipenv) (16.7.9)
Requirement already satisfied: certifi in c:\users\darsh\anaconda3\lib\site-packages (from pipenv) (2019.9.11)
Requirement already satisfied: pip>=9.0.1 in c:\users\darsh\anaconda3\lib\site-packages (from pipenv) (19.2.3)
Collecting virtualenv-clone>=0.2.5 (from pipenv)
  Downloading https://files.pythonhosted.org/packages/ba/f8/50c2b7dbc99e05fce5e5b9d9a31f37c988c99acd4e8dedd720b7b8d4011d/virtualenv_clone-0.5.3-py2.py3-none-any.whl
Requirement already satisfied: setuptools>=36.2.1 in c:\users\darsh\anaconda3\lib\site-packages (from pipenv) (41.4.0)
Installing collected packages: virtualenv-clone, pipenv
Successfully installed pipenv-2018.11.26 virtualenv-clone-0.5.3

(base) C:\Users\darsh\Desktop\localQuotey\Quotey>pipenv shell
Loading .env environment variables…
Creating a virtualenv for this project…
Pipfile: C:\Users\darsh\Desktop\localQuotey\Quotey\Pipfile
Using c:\users\darsh\anaconda3\python.exe (3.7.4) to create virtualenv…
[==  ] Creating virtual environment...Already using interpreter c:\users\darsh\anaconda3\python.exe
Using base prefix 'c:\\users\\darsh\\anaconda3'
  No LICENSE.txt / LICENSE found in source
New python executable in C:\Users\darsh\.virtualenvs\Quotey-YRAQ4zp5\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

Successfully created virtual environment!
Virtualenv location: C:\Users\darsh\.virtualenvs\Quotey-YRAQ4zp5
requirements.txt found, instead of Pipfile! Converting…
Success!
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did.
We recommend updating your Pipfile to specify the "*" version, instead.
Launching subshell in virtual environment…
Microsoft Windows [Version 10.0.18362.592]
(c) 2019 Microsoft Corporation. All rights reserved.

(Quotey-YRAQ4zp5) (base) C:\Users\darsh\Desktop\localQuotey\Quotey>pip freeze

(Quotey-YRAQ4zp5) (base) C:\Users\darsh\Desktop\localQuotey\Quotey>pipenv install -r requirements.txt
Requirements file provided! Importing into Pipfile…
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (7219a8)!
Installing dependencies from Pipfile.lock (7219a8)…
  ================================ 19/19 - 00:00:46

(Quotey-YRAQ4zp5) (base) C:\Users\darsh\Desktop\localQuotey\Quotey>pipenv freeze
Usage: pipenv [OPTIONS] COMMAND [ARGS]...
Try "pipenv --help" for help.

Error: No such command "freeze".

(Quotey-YRAQ4zp5) (base) C:\Users\darsh\Desktop\localQuotey\Quotey>pip freeze
asgiref==3.2.3
astroid==2.3.3
colorama==0.4.3
Django==3.0.1
django-admin-tools==0.8.1
djangorestframework==3.11.0
gunicorn==20.0.4
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
mysqlclient==1.4.6
nano==0.9.4
pycodestyle==2.5.0
pylint==2.4.4
pytz==2019.3
six==1.13.0
sqlparse==0.3.0
typed-ast==1.4.0
wrapt==1.11.2

(Quotey-YRAQ4zp5) (base) C:\Users\darsh\Desktop\localQuotey\Quotey>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 24, 2020 - 14:00:33
Django version 3.0.1, using settings 'Quotey.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Not Found: /
[24/Jan/2020 14:00:43] "GET / HTTP/1.1" 404 2157
[24/Jan/2020 14:00:45] "GET /admin HTTP/1.1" 301 0
[24/Jan/2020 14:00:47] "GET /admin/ HTTP/1.1" 200 3044

(Quotey-YRAQ4zp5) (base) C:\Users\darsh\Desktop\localQuotey\Quotey>