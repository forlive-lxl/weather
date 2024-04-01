class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

APPID = "d1dd11200dc0f09e24a600c207a9d2a1"