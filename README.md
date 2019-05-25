# Setup
    
    virtualenv env -p python3
    . env/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py init_db
    ./manage.py runserver