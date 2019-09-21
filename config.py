import os

class Config:
    """
    This is the class which will contain the general configurations
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    MAIL_PASSWORD='zubeyr525'
    MAIL_USERNAME='zubkayare@gmail.com'
    SECRET_KEY='1234'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://saadiaomar:1234@localhost/zub'
    WEATHER_API = '7af5acbdb838b1560514beb6fdeee3db'

# class ProdConfig(Config):
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
#     SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://saadiaomar:1234@localhost/zub'



class DevConfig(Config):
    SECRET_KEY='1234'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://saadiaomar:1234@localhost/zub'
    DEBUG = True

class TestConfig(Config):
    """
    This is the class which will contain the test configurations
    """
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://saadiaomar:1234@localhost/zub'


config_options = {
'development':DevConfig,
# 'production':ProdConfig,
'tests' : TestConfig
}

    