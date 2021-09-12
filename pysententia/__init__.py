from pkg_resources import get_distribution

class Sententia(object):
    r"""
    Wrapper class for the Sententia API.
    Attributes
    ----------
    Fill this space

    Methods
    -------
    Fill this space
    """
    def __init__(self, key):
        r"""
        Initialization method of the :code:`Sententia` class.
        Parameters
        ----------
        key : str
            The API key from the Sententia API.
        host : str
            The base URL of the Sententia API.
        headers:  dict
            header to perform API requests.
        """

        __version__ = get_distribution('pysententia').version

        self.key = key
        self.host = 'https://berapi.71point4.com/v1/'
        self.headers = {
            'accept': 'aplication/json',
            'token': self.key,
            "User-Agent": f"pysententia {__version__}"
        }

    from ._index import sent_index
    from ._counts import sent_counts
    from ._polarity import sent_word_polarity, sent_date_polarity
    from ._checkfunctions import check_params, check_response, validate_response


    

