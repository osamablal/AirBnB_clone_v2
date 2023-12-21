# AirBnB_clone_v2:-
Learning Objectives:
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:-

What is Unit testing and how to implement it in a large project
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
How to create a MySQL database
How to create a MySQL user and grant it privileges
What ORM means
How to map a Python Class to a MySQL table
How to handle 2 different storage engines with the same codebase
How to use environment variables

## Usage:-
1- First clone this repository.

2- To run it:
  - Using DBStorage Locate the "console.py" file and run it.
  ```
  $ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
  ```
3- Using FileStorage Locate the "console.py" file and run it.
  ```
  $ ./console.py
  ```
4- This prompt designates you are in the HBnB console.

## Classes:-
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## Command:-
- create
- show
- all
- destroy
- quit-EOF
- help
