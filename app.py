'''
Created on 09-Nov-2017

@author: anujsyal

    patient_data.app
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Main application start, loads API urls

'''
import logging
from logging.handlers import RotatingFileHandler

from patient_data import ProviderApi, app, api

# for wsgi application
application = app

def initialize_routes():
    """ Initialize API routes of application
    """
    api.add_resource(ProviderApi, '/api/providers')


if __name__ == '__main__':
    initialize_routes()
    handler = RotatingFileHandler('AppLogs.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.debug = True
    app.run(host='0.0.0.0', port=6800)