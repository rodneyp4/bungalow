# Bungalow Listing
A barebone Django server providing CRUD API endpoints to listings.

## Running Locally
Make sure you have Python 3.7
```sh
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
## CSV import command
```sh
$ python manage.py ingestcsv challenge_data.csv
```

## API Docs
[See here](api.v1.md)

---

## My Notes
1. This is a pretty barebone project, I mostly followed tutorials on Django and Django-rest-framework website
1. There's intentionally no tests, no auth, etc.
1. I made a few assumptions about the data type and format in the csv file, since it's weekend I don't want to bother you guys, but I think mostly it's harmless and easy to change should we need to.
1. Data are stored in default sqlite3 db.
1. I haven't touched python in the past two yrs, but I do enjoy the language.