# tmdb
sample project accessing [The Movie Database's API](https://www.themoviedb.org/documentation/api?language=en)

## Installation
### python 3
This project uses python 3, because it's 2019 and python 3 has been around for 10 years. Please don't start new projects in python 2!

If you _don't_ use a virtualenv, you may need to adjust the commands below, using `pip3` instead of `pip`, and `python3` instead of `python`. Depends on your setup.

### Install python dependencies with pip
Consider using a [virtualenv](https://virtualenv.pypa.io/en/latest/) so you don't mess up dependencies on other projects on the same machine.

Once you've activated your virtualenv, or if you decide not to use one, install dependencies via pip:  
```pip install -r requirements.txt```

### Initting Django
If you're familiar with Django, you're probably thinking "ok now I need to run migrations." You don't. This project doesn't have a database, and we aren't using Django's baked-in admin.

All you need to do is fire up Django's local testing server with ```python tmdb/manage.py runserver```, and then open [http://localhost:8000/](http://localhost:8000/) in your browser of choice.
