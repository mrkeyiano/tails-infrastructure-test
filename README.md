#### **ASSIGNMENT**
Your first assignment is to help Fido, a junior developer at Tails.com. Fido picked up a story in the backlog of building and deploying an API to determine if a dog's tail is going to wag when given a command. Fido needs your help to bring this service to production.

----

##### SETUP GUIDE

- Make sure docker is running on your machine
- Run below command in the application root folder


         docker-compose up


- Application is accessible on http://127.0.0.1:7777
----
##### CHANGELOG:

- corrected inconsistent variable naming convention in `app.py`
- added parameterized query support to protect against SQLite injection `app.py` 
- added try except statement to catch runtime exceptions when input command doesnt exist `app.py`
- used a lighter debian base image for the dockerfile `Dockerfile` this should reduce build time significantly
- exposed the port (7777) for flask
- passed the --host parameter to enable external access to the flask application, this answers your question on `why it doesnt work in docker`
- commented out unused python packages to reduce build time




----

##### QUESTIONS:


- q: If you had chosen to spend more time on this test, what would you have done differently?
  
  a: use nginx to serve the application and also use uwsgi to run the flask app for concurrency

- q: What part did you find the hardest? What part are you most proud of? In both cases, why?

  a: the sqlite security part reminded me of how important it is to reveiw code for security vulnerabilies and i love fixing bugs and loopholes


- q: What is one thing we could do to improve this test?

  a: add commands to the wag_or_not.sqlite file 

