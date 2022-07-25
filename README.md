# Primaseru

Primaseru is "Penerimaan Peserta Didik Baru" (in Indonesia) or in English mean <strong>Registering New Students</strong> web app.
As the name suggest Primaseru gonna be primary way for registering a new student at [Vocational High School Telkom Bandung.](https://smktelkom-bdg.sch.id/)

## Quick Start

Make sure <strong>Python 3.7+ is installed</strong> and you can access it from terminal (or cmd or powershell).

### Linux/Unix

```console
$ git clone https://github.com/supimadi/primaseru
$ cd primaseru
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ py manage.py migrate
$ py manage.py runserver
```

### Windows
```console
> git clone https://github.com/supimadi/primaseru
> cd primaseru
> py -m venv venv

> .\venv\Scripts\Activate.ps1 # for powershell or
> .\venv\Scripts\activate.bat # for cmd

> pip install -r requirements.txt
> py manage.py migrate
> py manage.py runserver
```

## Todo

- [ ] Writing Test Unit
- [ ] Refactoring some models
- [ ] Refactoring template

