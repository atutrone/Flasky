from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

#Constructors initalized, but no arguments passed to them
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

#App factory begins here:
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) #from_object pulls app_config settings from config.py
    config[config_name].init_app(app)

    #since the app is now defined in line 16, these constructors declared earlier can be initialized:
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #attach routes and error pages here

    return app
