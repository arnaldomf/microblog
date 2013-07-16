import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD




from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

if not app.debug:
	import logging
	from logging.handlers import SMTPHandler, RotatingFileHandler
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME, MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@'+MAIL_SERVER, ADMINS, 'microblog failure',
		credentials)
	file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	mail_handler.setLevel(logging.ERROR)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.addHandler(mail_handler)
	app.logger.setLevel(logging.INFO)
	app.logger.info('microblog startup')

mail = Mail(app)
from momentjs import momentjs
app.jinja_env.globals['momentjs'] = momentjs


from app import views, models
