# Rummager-API

Rummager is an application for dumpster divers to share their "hauls" of treasures that they find on their adventures!

# Local setup 

1. Clone this repository and `cd` into the directory in the terminal
2. Run `pipenv shell`
3. Run `pipenv install`
4. Run migrations and make migrations
5. Seed database with python3 manage.py loaddata {table name} 

LoadData in this order:
1. users
2. divers
3. tokens
4. dumpsters
5. tags
6. hauls
7. items

Now run the command:
python3 manage.py runserver

# Rummager ERD

Link to ERD: [ERD](https://drawsql.app/nss-6/diagrams/rummager#)