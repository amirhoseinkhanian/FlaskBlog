import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


class Development(Config):
    Debug = True


class Production(Config):
    Debug = False
