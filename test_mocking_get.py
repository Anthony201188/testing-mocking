import unittest
from unittest.mock import patch # <- Why do we have to import this specific modlue when we ahave imported the whole of unittest
#from datetime import datetime

from mocking_get import get_data,url


class TestGet(unittest.TestCase):
    @patch("mocking_get.requests")
    def test_get_data_success(self, mock_requests):
        mock_requests.get.return_value.status_code = 200
        mock_requests.get.return_value.json.return_value = {"Message":"Success"}
        self.assertEqual(get_data(url),{"Message":"Success"} )
    
    @patch("mocking_get.requests")
    def test_get_data_fail(self, mock_requests):
        mock_requests.get.return_value.status_code = 404
        #mock_requests.get.return_value.json.return_value = {"Message":"Not found"}
        self.assertIsNone(get_data(url))




    

 
     


#print(date)
