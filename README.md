lang-which
==========

Simple REST service to POST a string and receive the guessed language as response


Installation
------------

1. git clone git://github.com/saz/lang-which.git
2. cd lang-which
3. mkvirtualenv lang-which
4. pip install -r requirements.txt

Usage
-----

1. Starting lang-which
```
    python lang-which.py
```

2. POSTing some data
```
    curl -d text=Hello+World%3F -H "Accept: application/json" http://localhost:8080
```

### Sample Response
```
    saz@serenity:~$ curl -d text=Hello+World%3F -H "Accept: application/json" http://localhost:8080
    {"language": "en"}
    saz@serenity:~$
```
