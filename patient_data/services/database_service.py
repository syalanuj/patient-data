from patient_data.models.provider import Provider
'''
Created on 09-Nov-2017

@author: anujsyal

    patient_data.services.database_service
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Database service to interact with database

'''

class DatabaseService:
    """ Database service to interact with database, it uses sql-alchemy 
        at the backend
    """
    def __init__(self,db):
        """ Constructur to intitialize sql-alchemy database object
        ARGS:
            db (SqlAlchemy): sqlalchemy database object
        """
        self.db = db
    
    def save(self, obj):
        """ Save object into database
        ARGS:
            obj (SqlAlchemy.Model): Sqlalchemy models
        """
        self.db.session.add(obj)
        self.db.commit()
    
    def queryProviders(self,query_params):
        """ Filter providers based on query parameters
        ARGS:
            query_params (dictionary): provider query parameters
        RETURNS:
            Returns filtered providers
        """
        #providers = Provider.query.filter_by(**query_params)
        print(query_params["max_discharges"])
        query = Provider.query
        if query_params["max_discharges"] is not None:
            query = query.filter(Provider.total_discharges <= query_params["max_discharges"])
        if query_params["min_discharges"] is not None:
            query = query.filter(Provider.total_discharges >= query_params["min_discharges"])
        if query_params["max_average_covered_charges"] is not None:
            query = query.filter(Provider.average_covered_charges <= query_params["max_average_covered_charges"])
        if query_params["min_average_covered_charges"] is not None:
            query = query.filter(Provider.average_covered_charges >= query_params["min_average_covered_charges"])
        if query_params["max_average_medicare_payments"] is not None:
            query = query.filter(Provider.average_medicare_payments <= query_params["max_average_medicare_payments"])
        if query_params["min_average_medicare_payments"] is not None:
            query = query.filter(Provider.average_medicare_payments >= query_params["min_average_medicare_payments"])
        if query_params["state"] is not None:
            query = query.filter(Provider.state.ilike(query_params["state"]))
        return query.limit(1000).all()
    
