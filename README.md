microblog
==============

Flask Tutorial from http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

    $ python2.7 virtualenv.py flask
    $ flask/bin/pip install flask==0.9
    $ flask/bin/pip install flask-login
    $ flask/bin/pip install flask-openid
    $ flask/bin/pip install flask-mail
    $ flask/bin/pip install flask-sqlalchemy
    $ flask/bin/pip install sqlalchemy-migrate
    $ flask/bin/pip install flask-whooshalchemy
    $ flask/bin/pip install flask-wtf
    $ flask/bin/pip install flask-babel
    $ flask/bin/pip install flup
    $ flask/bin/pip uninstall sqlalchemy
    $ flask/bin/pip install sqlalchemy==0.7.9
In config.py, put the result of os.urandom(24) in the place of your SECRET_KEY variable
    $ git checkout HEAD README.md
    $ flask/bin/pybabel extract -F babel.cfg -o messages.pot app
    $ flask/bin/pybabel init -i messages.pot -d app/translations -l es
es = language
