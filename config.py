import os

class Config():
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        pass
        #raise Exception

class DevelopmentConfig(Config):
    DEBUG = True
    if os.environ.get('DEVELOPMENT_DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URL')
    else:
        pass
        #raise Exception

class TestingConfig(Config):
    TESTING = True
    if os.environ.get('TEST_DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    else:
        pass
        #raise Exception

class ProductionConfig(Config):
    DEBUG = False
    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URL')
    else:
        pass
        #raise Exception

config = {
                'development': DevelopmentConfig,
                'testing': TestingConfig,
                'production': ProductionConfig,
                'default': DevelopmentConfig
                }
