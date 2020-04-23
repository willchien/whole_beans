# Whole Beans Marketplace ☕️🌿

## Related installations
django version: 3.0.3 <br />
sudo apt-get install libssl-dev <br />
python -m pip install -U channels <br />
sudo apt-get install redis-server <br />
python -m pip install channels_redis <br />

## To get things started
Run ```python manage.py runserver``` in root directory to start the server. <br />
Then connect to ```localhost:8000``` <br />
<u><b>Important Note: </b></u> Settings are not changed. will not run on deployment environment 

### Database
* to make changes to database: "python manage.py makemigrations"
* to migrate: "python manage.py migrate"
* username and password of admin is "username" & "password"
* a random user that you can use is username=pikachu & password=123

### Superuser
connect to ```localhost:8000/admin``` <br />
username: ```beanmaster``` <br />
password: ```welovebeans``` <br />

### Notes
* Ignore .idea directory in root directory. .idea is for IDE specific use.
