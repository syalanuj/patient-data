'''
Created on 10-Nov-2017

@author: anujsyal

    patient_data.model.ipps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Provider data model

'''
from patient_data import db

class Provider(db.Model):
    """ Provider data model
        Inpatient Prospective Payment Systems Providers(IPPS)
        Sql alchemy orm model
    """
    __tablename__ = "provider"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provider_id = db.Column(db.Numeric,nullable=True)
    name = db.Column(db.String(100),nullable=False)
    drg_definition = db.Column(db.String(200),nullable=True)
    street_address = db.Column(db.String(200),nullable=True)
    city = db.Column(db.String(45),nullable=True)
    state = db.Column(db.String(2),nullable=True)
    zip_code = db.Column(db.Integer,nullable=True)
    hospital_referral_region_description = db.Column(db.String(100),nullable=True)
    total_discharges = db.Column(db.Integer,nullable=True)
    average_covered_charges  = db.Column(db.Numeric,nullable=True)
    average_total_payments  = db.Column(db.Numeric,nullable=True)
    average_medicare_payments  = db.Column(db.Numeric,nullable=True)

    def __init__(self, data):
        self.provider_id = data["provider_id"]
        self.name = data["name"]
        self.drg_definition = data["drg_definition"]
        self.street_address = data["street_address"]
        self.city = data["city"]
        self.state = data["state"]
        self.zip_code = data["zip_code"]
        self.hospital_referral_region_description = data["hospital_referral_region_description"]
        self.total_discharges = data["total_discharges"]
        self.average_covered_charges = data["average_covered_charges"]
        self.average_total_payments = data["average_total_payments"]
        self.average_medicare_payments = data["average_medicare_payments"]
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'provider_id': float(self.provider_id),
            'name': self.name,
            'drg_definition': self.drg_definition,
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'hospital_referral_region_description': self.hospital_referral_region_description,
            'total_discharges': self.total_discharges,
            'average_covered_charges': float(self.average_covered_charges),
            'average_total_payments': float(self.average_total_payments),
            'average_medicare_payments': float(self.average_medicare_payments)
        }