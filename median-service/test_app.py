#!flask/bin/python

"""Tests for microservice."""
import os
import time
import unittest
from flask import json
from app import app

__author__ = "Abhimanyu Nagurkar"
__copyright__ = "Copyright (C) Nginx Inc. All rights reserved."
__license__ = ""
__maintainer__ = "Abhimanyu Nagurkar"
__email__ = "abhimanyu.nagurkar@nginx.com"

class MedianTestCase(unittest.TestCase):
    """Tests for microservice."""

    def setUp(self):
        """Setup the test client."""
        self.app = app.test_client()

    def test_put_integer(self):
        """Test put endpoint"""
        response = self.app.post('/app/api/v1.0/put', data=json.dumps(dict(param=1)), content_type='application/json')
        data = json.loads(response.data)
        assert response.status_code == 201
        assert data['value'] == 1

    def test_put_invalid(self):
        """Test error for invalid input."""
        response = self.app.post('/app/api/v1.0/put', data=json.dumps(dict(param='foo')), content_type='application/json')
        data = json.loads(response.data)
        assert response.status_code == 400
        assert data['message'] == 'integer input expected'

    def test_put_empty(self):
        """Test error for empty input."""
        response = self.app.post('/app/api/v1.0/put')
        data = json.loads(response.data)
        assert response.status_code == 400
        assert data['message'] == 'input expected'

    def test_get_median(self):
        """Test to get median."""
        self.app.post('/app/api/v1.0/put', data=json.dumps(dict(param=1)), content_type='application/json')
        self.app.post('/app/api/v1.0/put', data=json.dumps(dict(param=5)), content_type='application/json')
        self.app.post('/app/api/v1.0/put', data=json.dumps(dict(param=10)), content_type='application/json')

        response = self.app.get('/app/api/v1.0/median')
        data = json.loads(response.data)
        assert response.status_code == 201
        assert data['median'] == 5


if __name__ == '__main__':
    unittest.main()
