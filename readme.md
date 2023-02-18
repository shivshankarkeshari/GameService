
```sh
$ git clone https://github.com/shivshankarkeshari/GameService.git
$ cd GameService
$ python  -m venv env
$ source env/bin/activate
(venv) $ python -m pip install -U pip setuptools
(venv) $ pip install -U -r requirements.txt
(venv) $ python manage.py makemigration
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
swagger API:-->  http://127.0.0.1:8000/api/v1/swagger/
```
