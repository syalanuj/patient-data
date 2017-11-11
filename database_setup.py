import pandas as pd
from patient_data import db
from patient_data import Provider
from patient_data.common.constants import constants as const

def init_schema():
    """ Initialize database schema using sql_alchemy create all
    """
    db.create_all()
    print("Database Schema created")

def load_data():
    """ Load data from csv to database
    """
    data_frame = pd.read_csv("""data_source/Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv""", encoding="utf-8")
    provider_dict = {}
    count = 0
    #Iterate over dataframe
    for row_index,row in data_frame.iterrows():
        provider_dict["provider_id"] = row[const.PROVIDER_KEY_MAP["provider_id"]]
        provider_dict["name"] = row[const.PROVIDER_KEY_MAP["name"]]
        provider_dict["drg_definition"] = row[const.PROVIDER_KEY_MAP["drg_definition"]]
        provider_dict["street_address"] = row[const.PROVIDER_KEY_MAP["street_address"]]
        provider_dict["city"] = row[const.PROVIDER_KEY_MAP["city"]]
        provider_dict["state"] = row[const.PROVIDER_KEY_MAP["state"]]
        provider_dict["zip_code"] = row[const.PROVIDER_KEY_MAP["zip_code"]]
        provider_dict["hospital_referral_region_description"] = row[const. \
                                    PROVIDER_KEY_MAP["hospital_referral_region_description"]]
        provider_dict["total_discharges"] = row[const.PROVIDER_KEY_MAP["total_discharges"]]
        provider_dict["average_covered_charges"] = row[const.PROVIDER_KEY_MAP["average_covered_charges"]].lstrip('$')
        provider_dict["average_total_payments"] = row[const.PROVIDER_KEY_MAP["average_total_payments"]].lstrip('$')
        provider_dict["average_medicare_payments"] = row[const.PROVIDER_KEY_MAP["average_medicare_payments"]].lstrip('$')
        provider = Provider(provider_dict)
        db.session.add(provider)
        db.session.commit()
        count = count + 1
    
    print("Data Load completed, rows loaded: " + str(count))

if __name__ == '__main__':
    init_schema()
    load_data()