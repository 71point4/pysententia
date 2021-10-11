import requests
import json

from ._checkfunctions import check_params, check_response, validate_response
from ._params import parameters

def _sent_word_polarity(self, host, headers, params):
    """Get the top 50 most frequently occurring positive and negative words."""

    endpoint =  (
            f"word_polarity?source={params['source']}&"
            f"model={params['model']}&"
            f"topic={params['topic']}&"
            f"freq={params['freq']}&"
            f"dict={params['dict']}"
    )

    response = requests.get(f"{self.host}{endpoint}", headers=self.headers)
    return validate_response(response)

def sent_word_polarity(self, **kwargs):
    """Get the top 50 most frequently occurring positive and negative words."""
    req_params      = parameters['sent_word_polarity']['req_params']
    # Check params
    params = check_params(req_params, kwargs)

    return _sent_word_polarity(self, self.host, self.headers, params)

# ---------------------------------------------------------------------------------
# (sent_date_polarity) Get a count of the number of positive and negative articles.
# ---------------------------------------------------------------------------------

def _sent_date_polarity(self, host, headers, params):
    """Get a count of the number of positive and negative articles."""

    endpoint =  (
            f"word_polarity?source={params['source']}&"
            f"topic={params['topic']}&"
            f"freq={params['freq']}&"
            f"dict={params['dict']}&"
            f"aggr={params['aggr']}"
    )

    response = requests.get(f"{self.host}{endpoint}", headers=self.headers)
    return validate_response(response)

def sent_date_polarity(self, **kwargs):
    """Get the top 50 most frequently occurring positive and negative words."""
    req_params      = parameters['sent_date_polarity']['req_params']
    # Check params
    params = check_params(req_params, kwargs)

    return _sent_word_polarity(self, self.host, self.headers, params)
