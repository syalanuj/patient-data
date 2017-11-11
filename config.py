'''
Created on 09-Nov-2017

@author: anujsyal

    config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Application config

'''
import logging


class Config(object):
    """
    This will contains default values of each configuration item. These values can be overriden
    in the respective environment configuration below
    """
    DEBUG = False
    TESTING = False
    LOG_LEVEL = logging.WARNING
    # Base path of the application being served
    VIRTUAL_DIR = ''
    
class DevelopmentConfig(Config):
    """
    This will contains development values of each configuration item.
    """
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgres://anujsyal@localhost:5432/patient_data"

class StagingConfig(Config):
    """
    This will contains staging values of each configuration item.
    """
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgres://anujsyal@localhost:5432/patient_data"

class ProductionConfig(Config):
    """
    This will contains production values of each configuration item.
    """
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = ""

ENV = StagingConfig

