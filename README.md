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
 #### Deactivate environment
    ```bash
    deactivate
    ```
 #### Check installed packages
    ```bash
    pip list
    ```




 