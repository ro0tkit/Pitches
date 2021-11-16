import os

class Config:

    SECRET_KEY='SECRET_KEY'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://luther:luth3r@localhost/pitchh'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitchh'
    SENDER_EMAIL = 'luther.king@student.moringaschool.com'

   
  

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
   
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://luther:luth3r@localhost/pitchh_test'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # connecting to database
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://luther:luth3r@localhost/pitchh'

    DEBUG = True

    #connecting to Gmail
   

  

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}
