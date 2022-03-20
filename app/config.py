import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SQLALCHEMY_DATABASE_URI = "postgresql://hhipqvuwxrerzz:ae8a9534ba85593b7d4f8bc536af411d4b1baddcb31bf34f6e5bf3c0d53ba769@ec2-34-224-226-38.compute-1.amazonaws.com:5432/dfk04h2aj1sb6"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_URL')