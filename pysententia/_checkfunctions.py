import requests
import json
import pandas as pd


# Check params functions -------------------------------------------------------

class Error(Exception):
    """Base class for other exceptions."""

    pass


class RequiredArgMissing(Error):
    """Raised when a required argument is missing."""
    
    pass


def check_params(req_params, args):
    """Describe this method here."""
    params = {}
    # Check required params
    if req_params:
        for key in req_params:
            if key not in args:
                raise RequiredArgMissing(f"Required argument '{key}' is missing.")
            else:
                assert isinstance(args[key], req_params[key]), f"'{key} type must be {req_params[key]}."
            params.update({key: args[key]})
            del args[key]

    return params


# Check API functions ---------------------------------------------------------

def check_response(response):
    try:
        response = response
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:

        print(err, '\n', json.loads(response.text))

        return(json.loads(response.text))
        # pass
        # raise SystemExit()

def validate_response(response):

    if (response.status_code != 200):
            return(json.loads(response.text))

    # Check response
    check_response(response)
    j_response = json.loads(response.text)
    df = pd.DataFrame(pd.json_normalize(j_response))

    return df
