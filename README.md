# Currency Exchange Rate App 

This application is build in Django and REST API with deployment script.


## Usage
This app allows users to check exchange rate with different countries.

## Output
Output is in json output.
The query and result is saved in sqlite.

## Installation


### Setting up environment
```
python3 -m venv venv
source env/bin/activate
pip3 install -r requirements.txt
```
## Running application
```
cd randomapi\src
python3 manage.py runserver
```
Create a super user and follow the instructions:
```
python3 manage.py createsuper
```
Finally, run the server:
```
python3 manage.py runserver
```
The app should hosted on [localhost:8000](localhost:8000).

Admin, run on this url and is where you can see query requests:
```
localhost:8000/admin
```
