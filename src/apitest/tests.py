from django.test import TestCase
from nose.tools import assert_true
import requests


# Create your tests here.
def test_request_response():
    # Send a request to the API server and store the response.

    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "ZAR", "to": "USD", "q": "1"}

    headers = {
        'x-rapidapi-key': "25249a8914mshd5c96c97d61218cp182c84jsnc57c2ca9d09c",
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)