import os


class Config:
    ROOT = os.getcwd()




class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
}