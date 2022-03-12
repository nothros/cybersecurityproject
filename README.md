# cybersecurityproject_part1

This is a project for the CyberSecurityBase- course in the University of Helsinki. 
The main idea was to create a vulnerable Webapp. 

(https://cybersecuritybase.mooc.fi) 

## Installation instructions:
### Database:
You will need **PostgreSQL** to use this.
#### Linux/Windows:
(https://www.postgresql.org/download/)
#### MacOs: 
Postgres.app (https://postgresapp.com/)

After installation (if needed)

After this start postgres connection.
```
start-pg.sh
```
Implement projects Schema to psql.(in the same file with schema)
```
psql <schema.sql
```
### Run project
You will need **Flask** to run this project
(https://flask.palletsprojects.com/en/2.0.x/)

go to the project file
```
source venv/bin/activate 
```
```
pip install flask
```
```
flask <reguirements.txt 
```
and afetr this, run project with
```
flask run
```
Now you can go to website by clicking ctrl+click the link in console
```
* Running on http://xxx.x.x.x:<PORT>/ (Press CTRL+C to quit)
```
