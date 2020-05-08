import os

class Config:

    '''
    class facilitates the creation of app configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    

class DevConfig(Config):

    '''
    class inherits general configurations from Config class
    '''
    DEBUG = True

class ProdConfig(Config):

    '''
    class inherits general configurations from config class
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}