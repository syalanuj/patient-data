'''
Created on 10-Nov-2017

@author: anujsyal

    patient_data.apis.provider_apis.provider_api
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Provider API endpoint

'''
from flask import jsonify, request
from flask_restful import Resource
from patient_data import provider_service

class ProviderApi(Resource):
    """ Provider API Endpoint for list of of providers
    """
    def get(self):
        """ Get list of providers based on query parameters
        URL_Sample:
            /providers?max_discharges=5&min_discharges=6&max_average_covered_charges=50000
                &min_average_covered_charges=40000&min_average_medicare_payments=6000
                &max_average_medicare_payments=10000&state=GA
        Query Parameters:
            max_discharges (int): The maximum number of Total Discharges
            min_discharges (int): The minimum number of Total Discharges
            max_average_covered_charges (Float): The maximum Average Covered Charges 
            min_average_covered_charges (Float): The minimum Average Covered Charges
            max_average_medicare_payments (Float): The maximum Average Medicare Payment
            min_average_medicare_payments (Float): The minimum Average Medicare Payment
            state (String): The exact state that the provider is from
        Returns (JSON):list of providers
        """
        try:
            print(request.args.get('min_average_medicare_payments'))
            filtered_providers = provider_service.queryProviders(
                                request.args.get('max_discharges'),
                                request.args.get('min_discharges'),
                                request.args.get('max_average_covered_charges'),
                                request.args.get('min_average_covered_charges'),
                                request.args.get('max_average_medicare_payments'),
                                request.args.get('min_average_medicare_payments'),
                                request.args.get('state'))
            return jsonify([provider.serialize for provider in filtered_providers])
        except Exception as err:
            Exception(err)
        
