# TwoPassword

Password Manager

**Technologies:** Python, Django, SQLite

## Requirements

 * Python >= 3.8
 * Django = 3.1
 * cryptography >= 3.4.7

## Screenshots

You can find the screenshots of the application in the [screenshots](/screenshots) folder.

## Installation

### Getting the source code

Clone the repository
```
$ git clone https://github.com/vchrombie/TwoPassword/
$ cd TwoPassword/
```

### Prerequisites

#### Poetry

Used [Poetry](https://python-poetry.org/docs/) for managing the project.
You can install it following [these steps](https://python-poetry.org/docs/#installation).

### Installation

Install the required dependencies (this will also create a virtual environment)
```
$ poetry install
```

Activate the virtual environment
```
$ poetry shell
```

### Setup

Make and apply the migrations
```
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
```

Create a superuser
```
(.venv) $ python manage.py createsuperuser
```

Run the server
```
(.venv) $ python manage.py runserver
```

## TBA

- [ ] Tests
- [ ] Option to delete a password
- [ ] Paginate the list view
- [ ] Generate a password
- [ ] UI Improvements

## References

- https://docs.djangoproject.com/en/3.1/
- https://devqa.io/encrypt-decrypt-data-python/
