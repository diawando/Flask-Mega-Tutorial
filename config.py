import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-gues'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \ 
    'postgresql://postgres:lavie@localhost:5432/mega_tuto'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    