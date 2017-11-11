

##Patient data coding challenge

##Overview
This project sovles the problem stated at 
```
https://gist.github.com/rbrowngt/acea1afc4f8d0871851e5ebb21876baa
```
Purpose is to build a full web application solution with backend API and frontend and deploy at backend

## Application Architecture

### Frameworks
- Server: Python Flask
- Client: Angular 4
###Database
- Postgresql
### Dependencies
#### Server
- Python 3.6
- Postgresql
- pip
- Flask: Backend Framework
- Flask-Restful: Library to build restful apis
- Sqlachemy
- Flask-sqlalchemy
- pandas
- virtualenv
- npm
#### Client
- Angular 4 core libraries

### Directory structure
```
    |-- app.py (App starts from here)
    |-- config.py (Configurations)
    |-- database_setup.py (Database schema generation and data load to database)
    |-- readme.md
    |-- requirements.txt (serverdependencies)
    |-- patient_data
        |-- __init__.py (all imports and flask app init)
        |-- apis (Apis module wise)
            |-- ...
        |-- client (Client side code [Angular4])
            |-- ...
        |-- common (common utilities and constants)
            |-- ...
        |-- services (service layer of application)
            |-- ...
        |-- models (Appliocation models)
            |-- ...
        |-- tests (Unit tests)
            |-- ...
        |-- Views (Link client app to base url)
            |-- ...
```
## Development setup (MAC)
- Install python 3.6
    -  ```brew install python3```
- Install postgresql server
    -  ```brew install postgres```
    - or install using pgadmin

- Clone or unzip the folder
- Go to project Directory 
- Create virtualenv ```virtualenv env```
- Activate virtualenv ```enc/bin/source activate ```
- Install Dependencies from requirements```pip install requirements.txt```
- Setup Database schema and load data ```python database_setup.py ```
- Run application server ```python install app.py```
    This will start the local server and will point to the build of client in dist folder
- Client side setup: go to ```patient_data/client``` folder
- Install angular client ```npm install -g @angular/cli```
- Start client side ```ng serve```
-
## Deployment on Heroku
- ```Heroku login``` and enter your heroku crendentials
- Create new heroku app ```heroku create```
- Start free dev postgresql from admin panel in add ons
- Copy database URI from the admin panel
- Change the database URI in env
- In the created folder clone from the provided git url
- Build the client side code ```ng build --prod```
- Paste your code, commit and push to branch 
    - Copy only dist folder in client
    - ```git commit -a -m "message"```
    - ```git push```
- The installation will be done automatically
- Deploy database
    - ```Heroku run python```
    - In python shell perform following commands
        ```
        >>from database_setup import init_schema, load_data
        >> init_schema()
        >> load_data ()
        ```
- Open the url in web browser```Heroku open```

**Note: Data loaded for 5000 record limit
