# remind-me-later

# How to run
- Install all packages ``pip install -r requirements.txt``
- perform migration ``python manage.py migrate`` and ``python manage.py makemigrations``
- Run the project ``python manage.py runserver``


# API 
- ``GET`` ``/api/reminders/``
- ``POST`` ``/api/reminders/``
  - Post arguments:
    - ``message`` : required
    - ``remind_date`` : required, format ``"YYYY-MM-DD"``
    - ``remind_time`` : required, format ``"HH:MM:SS"``


  


