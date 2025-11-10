# Legacy.py
 
 ## Visual studio setup for my python project
 ### Extensions to install

 1. python (by microsoft) for linting & debugging 
 2. pylance  Fast language server(type checking)
 3. python indent or Black Formatter or autopep8
 4. autoDocstring, generates docstrings
 5. Isort, automatically sorts imports
 6. Gitlens , git insights and clean versioning control
 7. Docker conteinerization
 8. Thunder Client  or REST Client for Testing Apis

 ### Python Environment Setup Guide

 #### Check Python Version (Need 3.9+)

  ```bash
  python --version
  # or
  python3 --version

  ```
 #### Create virtual environment

  ```bash
  python -m venv venv
  ```
 #### Activate the virtual environment
 1. Windows:
  ```bash
  venv\Scripts\activate
   ```
 2. Mac or Linux:
  ```bash
  source venv/bin/activate
  ```
 #### Install tools 
 ```bash
 pip install (package name,pname,pname) ie django
  ```

 #### Dependencies
 1. save dependencies to file
   ```bash 
   pip freeze > requirements.txt
    ```
 2. Install from requirements.txt
   ```bash
   pip install -r requirements.txt
    ```
    ---------------------------------
 ### Deactivate environment
    ```bash
    deactivate
    ```
    ----------------------------------
 #### Check installed packages
    ```bash
    pip list
    ```
--------------------------------------

### Initial Setup Commands
   1. create project folder

    ```bash
     mkdir project name
    ```
    2. change directory into it

      ```bash
      cd project name
      ```
    3. create virtual env
      ```bash
      python -m venv venv
      ```
    4. Activate it 
      ```bash
      source venv/bin/activate
      ```
    5. create folder structure

    clinic-backend/
│
├── src/
│   ├── __init__.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py        # env & constants loader
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── exceptions.py      # custom app exceptions
│   │   └── logger.py          # basic logging setup
│   │
│   ├── domain/                # pure OOP business entities
│   │   ├── __init__.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   │
│   ├── repositories/          # DB access layer
│   │   ├── __init__.py
│   │   ├── base_repo.py       # abstract base repo (interfaces)
│   │   └── appointment_repo.py
│   │
│   ├── services/              # business logic layer
│   │   ├── __init__.py
│   │   └── scheduling_service.py
│   │
│   ├── api/                   # REST-like layer
│   │   ├── __init__.py
│   │   ├── controllers.py     # request handlers
│   │   └── routes.py          # endpoint mapping
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── connection.py      # DB connection pool (psycopg2 / placeholder)
│   │
│   └── app.py                 # entrypoint – wires config, DB, and routes
│
├── tests/
│   └── test_scheduling_service.py
│
├── .env                       # local environment vars
├── requirements.txt
├── main.py                    # starts the app (calls src.app)
└── README.md

    



 