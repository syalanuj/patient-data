'''
Created on 09-Nov-2017

@author: anujsyal

    patient_data.services.provider_service
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Provider service for interaction between api layer and database service

'''

class ProviderService(object):
    """ Provider Service 
    """

    def __init__(self, database_service):
        """ Initialization of database service
        """
        self.database_service = database_service
    
    def queryProviders(self,max_discharges,min_discharges,
                max_average_covered_charges, min_average_covered_charges,
                max_average_medicare_payments, min_average_medicare_payments,
                state):
        """ Query providers from database service by building query_params
        ARGS:
            max_discharges (int): The maximum number of Total Discharges
            min_discharges (int): The minimum number of Total Discharges
            max_average_covered_charges (Float): The maximum Average Covered Charges 
            min_average_covered_charges (Float): The minimum Average Covered Charges
            max_average_medicare_payments (Float): The maximum Average Medicare Payment
            min_average_medicare_payments (Float): The minimum Average Medicare Payment
            state (String): The exact state that the provider is from
        Ret
        """
        # We can skip query parameters dictionary as we are not using dynamic **query_params
        query_params = {}
        query_params["max_discharges"] = max_discharges
        query_params["min_discharges"] = min_discharges
        query_params["max_average_covered_charges"] = max_average_covered_charges
        query_params["min_average_covered_charges"] = min_average_covered_charges
        query_params["max_average_medicare_payments"] = max_average_medicare_payments
        query_params["min_average_medicare_payments"] = min_average_medicare_payments
        query_params["state"] = state

        return self.database_service.queryProviders(query_params)