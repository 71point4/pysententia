import requests
import json

from ._checkfunctions import check_params, check_response, validate_response
from ._params import parameters

def _sent_index(self, host, headers, params):
    """Pull a specific media sentiment index method"""

    endpoint =  (
            f"index?source={params['source']}&"
            f"model={params['model']}&"
            f"topic={params['topic']}&"
            f"freq={params['freq']}&"
            f"dict={params['dict']}&"
            f"aggr={params['aggr']}"
    )

    response = requests.get(f"{self.host}{endpoint}", headers=self.headers)

    return validate_response(response)

def sent_index(self, **kwargs):
    """Pull a specific media sentiment index method"""
    req_params      = parameters['sent_index']['req_params']
    # Check params
    params = check_params(req_params, kwargs)

    return _sent_index(self, self.host, self.headers, params)
