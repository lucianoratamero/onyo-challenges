# Lotto Check Service (made for Onyo`s Admissional Challenge)

This is a Lotto Check Service made for Onyo`s Admissional Challenge and does not have any production application whatsoever. But it works, of course ;)

### Development setup

To setup this project to development, you need to clone this project, create and activate a virtualenv, install the dependencies and setup databases.

Before running anything, be sure to have postgresql 9.4 installed.

```
git clone git@github.com:lucianoratamero/onyo-challenges.git
virtualenv onyo-challenges
cd onyo-challenges
source bin/activate
pip install -r requirements.txt
```

#### Database setup

Before running migration to prepare your databases schema, you need to create ana_db and bob_db databases on postgres.
This differs from distro to distro, but probably you just need to run the following commands:

```
createdb ana_db
createdb bob_db
```

If you don't have the privileges to do that, try running with "sudo -u postgres" before each command.

With the databases created, all you need to do is to run the migration commands:
```
python manage.py migrate
python manage.py migrate --database=ana_db
python manage.py migrate --database=bob_db
```

And that's it! To run the tests:

```
python manage.py test
```

To run you local server:

```
python manage.py runserver
```

### Deploying to heroku

To deploy this app to heroku, first you need to [create and configure your heroku app](https://devcenter.heroku.com/articles/git).

To deploy only one API Django app or all of them, you need to [set heroku configs accordingly](https://devcenter.heroku.com/articles/config-vars#setting-up-config-vars-for-a-deployed-application), so heroku knows which Django settings to use.

```
heroku config:set -a [heroku-app-name] DJANGO_SETTINGS_MODULE=[path.to.settings]
```

After pushing changes to heroku and with the app running, you need to setup your databases.

#### Heroku databases

First, you need to migrate to the default database, used by Django for most everything, except for API specific models.

```
heroku run -a [heroku-app-name] python manage.py migrate
```

Beyond the basic django database, for each API you want to host, you need to setup that app's database too.

```
heroku run -a [heroku-app-name] python manage.py migrate --database=[django-app-name]_db
```

#### Ana specific settings

Ana API Django app depends on a Bob host, so it can retrieve tickets data. Since everything is decoupled, it is necessary to point to Bob's API URL by setting an environment variable.

```
heroku config:set -a [heroku-app-name] CURRENT_BOB_API_URL=[full-url-to-bob]
```
