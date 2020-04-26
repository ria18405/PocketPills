## POCKETPILLS

#### Setting up the project:

1. Run Healthcare_7.sql
2. Run DataEntry1.sql
3. Run indexing.sql
4. `sudo make` the excetuable file in Chatbox folder, and replace the executable file in CLI-&-Front-End/CLI folder.
5. Change the password in Line 6 of CLI-&-Front-End/CLI/CLI.py
6. `pip install mysql-connector-python`
7. Command line interface is ready to run.

#### Front End Components:

1. Enter into `my_env` virtual environment by running 

            `source my_env/bin/activate`
            
2. Change the password at 2 places: 

    *   Line 84 of [my_project/settings.py](https://github.com/ria18405/PocketPills/blob/master/my_project/my_project/settings.py) 
    *   Line 8 of [articles/views.py](https://github.com/ria18405/PocketPills/blob/master/my_project/articles/views.py)    
       
3. Run `python manage.py runserver`

4. If there are any unapplied migrations, run `python manage.py migrate`

5. Check the local site at `http://127.0.0.1:8000/`