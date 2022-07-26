# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestQuantumCodeController(BaseTestCase):
    """QuantumCodeController integration test stubs"""

    def test_grover_circuit(self):
        """Test case for grover_circuit

        Get the circuit implementation of Grover Algorithm
        """
        headers = { 
        }
        response = self.client.open(
            '/circuit/grover',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_random_circuit(self):
        """Test case for random_circuit

        Get the circuit implementation for random numbers
        """
        query_string = [('api_token', 'api_token_example')]
        headers = { 
        }
        response = self.client.open(
            '/circuit/random',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
