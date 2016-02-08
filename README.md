# Lotto Check Service (made for Onyo`s Admissional Challenge)

This is a Lotto Check Service made for Onyo`s Admissional Challenge and does not have any production application whatsoever. But it works, of course ;)

### Development setup

To setup this project to development, you need to clone this project, create and activate a virtualenv, install the dependencies and setup databases.

First, install some OS dependencies. This differs from distro to distro, so I will only tell how to do it on Ubuntu 14.04:

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install python-dev libncurses-dev python-setuptools postgresql-9.5 postgresql-server-dev-9.5 git
```

After that, you need to install the virtualenv package through pip:

```
sudo easy_install pip
sudo pip install virtualenv
```

Then, we can install our project :)

```
git clone https://github.com/lucianoratamero/onyo-challenges.git
virtualenv onyo-challenges
cd onyo-challenges
source bin/activate
pip install -r requirements.txt
```

#### Databases setup

Before running migration to prepare your databases schema, you need to create ana_db and bob_db databases on postgres.

```
sudo -u postgres createdb ana_db
sudo -u postgres createdb bob_db
```

With the databases created, you need to configure the username and password to access postgresql databases. I usually use the role 'postgres', changing it's password to a random one.

```
sudo -u postgres psql
\password postgres
[the-password-you-want]
[the-password-you-want-again]
\q
```

Then, export the username and password as DB_USER and DB_PASS so our Django apps know how to connect to postgresql databases. I usually export both using the postactivate script, which is executed each time you activate this virtualenv. What you need to do is this:

```
export DB_USER=postgres && echo 'export DB_USER=postgres' >> bin/postactivate
export DB_PASS=[the-password-you-set-into-postgres] && echo 'export DB_PASS=[the-password-you-set-into-postgres]' >> bin/postactivate
```

Phew! Almost done! Now, all you need to do is to run the migration commands:

```
python manage.py migrate
python manage.py migrate --database=ana_db
python manage.py migrate --database=bob_db
```

If you have problems with postgresql peer authentication (as always ><), follow [these steps](http://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge) to fix it.

...aaaand that's it! To run the tests:

```
python manage.py test
```

To run you local server:

```
python manage.py runserver
```

### Deploying to heroku

To deploy this app to heroku, there's no need to be able to run the project locally - you just need to have cloned this project and have [heroku toolbelt installed](https://toolbelt.heroku.com/debian) =)

But before deploying, you need to [create and configure a new heroku app](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote), so we can deploy to it. Remember your created heroku app name, it will be **very** important.

Then, you need to [set heroku configs accordingly](https://devcenter.heroku.com/articles/config-vars#setting-up-config-vars-for-a-deployed-application), so heroku knows which Django settings to use. The available options are 'config.heroku.ana.settings', 'config.heroku.bob.settings' and 'config.heroku.all.settings', to deploy Ana, Bob or All.

```
heroku config:set -a [heroku-app-name] DJANGO_SETTINGS_MODULE=[path.to.settings]
```

Then, push the changes to your heroku app:

```
git push heroku master
```

After pushing changes to heroku and with the app running, you need to setup your databases.

#### Heroku databases

First, you need to migrate to the default database, used by Django for most everything, except for API specific models.

```
heroku run -a [heroku-app-name] python manage.py migrate
```

Beyond the basic django database, for each API you want to host, you need to setup that app's database too **(except if running all, since it does not need different databases)**.

```
heroku run -a [heroku-app-name] python manage.py migrate --database=[django-app-name]_db
```

Since it is completely decoupled from Bob, ff you are hosting Ana Django app, you need to pass to it Bob's API URL, even if it is running at the same host.

```
heroku config:set -a [heroku-app-name] CURRENT_BOB_API_URL=[full-url-to-bob]
```
