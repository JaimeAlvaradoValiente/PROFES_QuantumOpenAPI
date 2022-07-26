# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.quantum import Quantum  # noqa: E501
from openapi_server.test import BaseTestCase


class TestQuantumController(BaseTestCase):
    """QuantumController integration test stubs"""

    def test_find_service_by_category(self):
        """Test case for find_service_by_category

        Finds quantum service by category
        """
        query_string = [('category', ['category_example'])]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/findByCategory',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
