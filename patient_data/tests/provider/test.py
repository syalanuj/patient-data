import os
import unittest
import tempfile
import ..patient_data
from ..database_setup import init_schema,load_data

class ProviderTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, patient_data.app.config['Database'] = tempfile.mkstemp()
        patient_data.app.testing = True
        self.app = patient_data.app.test_client()
        with patient_data.app.app_context():
            init_schema()
            load_data()
        
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(patient_data.app.config['DATABASE'])
    
    def test_provider_all():
        providers = self.app.get('/providers')
        assert b'Providers data' in providers
    
    def test_provider_filter():
        providers = self.app.get('/providers?state=FL')
        assert b'Providers data filtered by state' in providers
        providers = self.app.get('/providers?max_discharges=30')
        assert b'Providers data filtered by max_discharges = 30' in providers
        providers = self.app.get('/providers?min_discharges=90')
        assert b'Providers data filtered by min_discharges = 90' in providers
        providers = self.app.get('/providers?max_average_covered_charges=7000')
        assert b'Providers data filtered by max_average_covered_charges = 7000' in providers
        providers = self.app.get('/providers?min_average_covered_charges=5000')
        assert b'Providers data filtered by min_average_covered_charges = 5000' in providers
        providers = self.app.get('/providers?max_average_medicare_payments=6000')
        assert b'Providers data filtered by max_average_medicare_payments = 6000' in providers
        providers = self.app.get('/providers?min_average_medicare_payments=3000')
        assert b'Providers data filtered by min_average_medicare_payments = 3000' in providers
        providers = self.app.get('/providers?state=FL')
        assert b'Providers data filtered by sate = FL' in providers

        
if __name__ == '__main__':
    unittest.main()
        




