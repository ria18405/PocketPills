## POCKETPILLS

#### APPLICATION: 

POCKETPILLS is an online medical facility where our registered users will get the pleasure and ease of e-consultancy by highly specialised and rated doctors. In case of a need for a physical diagnostic, doctors can also schedule an appointment. Users get the facility to purchase the prescribed medicines easily with door to door delivery service available at affordable rates.


#### STAKEHOLDERS

* **User** demanding prescription and purchasing medicines

* **Company** accessing database to check and maintain the stock of medicines and available specialised doctors. 

* **Doctors** dealing with their patients and scheduling their appointments.

* **Small Pharmacy Retailers** who will have the facility to purchase medicines at wholesale rate from the website. 

* **Delivery Agencies** who will need the delivery details of the recipient. 

* **Diagnostic Labs** needing access to a patient’s medical details and the required lab facility needed. 


#### Setting up the system:

1. Run Healthcare_7.sql
2. Run DataEntry1.sql
3. Run indexing.sql
4. `sudo make` the excetuable file in Chatbox folder, and replace the executable file in CLI folder.
5. Change the password in Line 6 of [CLI/CLI.py](https://github.com/ria18405/PocketPills/blob/master/CLI/CLI.py)
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


![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img1.png)
![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img2.png)
![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img3.png)
![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img4.png)

CHAT SYSTEM:

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img5.png)


Company and their Market-Share:

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img6.png)

Tests and their Market-Share:

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img7.png)

DeliveryAreas and their Market-Share:

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img8.png)

Bar-Chart for Drug ID=16

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img9.png)

Bar-Chart for Delivery Agency ID=25:

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img10.png)

Bar-Chart for Doctor ID=3

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/img11.png)

ER DIAGRAM

![Image description](https://github.com/ria18405/PocketPills/blob/master/assets/er.png)

