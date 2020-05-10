import os

class Config:

    '''
    class facilitates the creation of app configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    

class DevConfig(Config):

    '''
    class inherits general configurations from Config class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:pixie01@localhost/partage'

    DEBUG = True

class TestConfig(Config):

    '''
    class inherits general configurations from config class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:pixie01@localhost/partage_test'

class ProdConfig(Config):

    '''
    class inherits general configurations from config class
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}