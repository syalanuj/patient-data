'''
Created on 10-Nov-2017

@author: anujsyal

    patient_data
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Imports all dependencies and initialize flask app

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_restful.representations.json import output_json
import config

class BaseApi(Api):
    """ Custom base api to provide exceptional handling
        and logging
    """
    def handle_error(self, e):
        """ Flask-Restful's error handler renders it
        """
        if not hasattr(e, 'data'):
            e.data = e

        return super(BaseApi, self).handle_error(e)

# Initialize flask app and api
app = Flask(__name__, static_url_path='',static_folder='client/dist')
api = BaseApi(app)

#Load application configurations from config module
app.config.from_object(config.ENV)
db = SQLAlchemy(app)

# Import models,services, apis and views which will be served by the application
#Models
from patient_data.models.provider import Provider

#Services
from patient_data.services.database_service import DatabaseService
from patient_data.services.provider_service import ProviderService

#Initialize service with Dependency Injection
database_service = DatabaseService(db)
provider_service = ProviderService(database_service)


#Import APIs
from patient_data.apis.provider_apis.provider_api import ProviderApi
from patient_data.views import home


#Handle paths that has no routes in the application
# This creates issues in depoloyment
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return 'url not found: %s' % path

# Handle errors in json format
@api.representation('application/json')
def output_json_exception(data, code, *args, **kwargs):
    """Render exceptions as JSON documents with the 
        exception's message."""
    if isinstance(data, Exception):
        data = {'status': code, 'message': str(data)}

    return output_json(data, code, *args, **kwargs)