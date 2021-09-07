import requests
import json

from ._checkfunctions import check_params, check_response, validate_response
from ._params import parameters

def _sent_counts(self, host, headers, params):
    """Pull a specific media sentiment index method"""

    endpoint =  (
            f"counts?source={params['source']}&"
            f"model={params['model']}&"
            f"topic={params['topic']}&"
            f"freq={params['freq']}"
    )

    response = requests.get(f"{self.host}{endpoint}", headers=self.headers)
    return validate_response(response)

def sent_counts(self, **kwargs):
    """Get a count of the number of articles for a specified media source."""
    req_params      = parameters['sent_counts']['req_params']
    # Check params
    params = check_params(req_params, kwargs)

    return _sent_counts(self, self.host, self.headers, params)
