"""
curl --request GET \
     --url 'https://api.chainabuse.com/v0/reports?orderByDirection=ASC&orderByField=CREATED_AT&before=2022-01-01T02%3A00%3A00&since=2023-01-01T02%3A00%3A00&page=1&perPage=50' \
     --header 'accept: application/json'
"""
import logging
from copy import deepcopy
from dataclasses import dataclass
from os import environ, path
from typing import Any, Dict, Union

import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
from rich.pretty import pprint
from tenacity import after_log, retry, stop_after_attempt, wait_exponential

# load_dotenv() should be called as soon as possible (before parsing local classes) but not for pytest
from dotenv import load_dotenv
load_dotenv()

from chainabuse_extractor.helpers.logging_helper import log
from chainabuse_extractor.reports_request import ReportsRequest


API_URL = 'https://api.chainabuse.com/v0'
REPORTS_URL = path.join(API_URL, 'reports')
JSON_HEADERS = {'Accept': 'application/json'}


class Api:
    def __init__(self) -> None:
        self.api_key = environ['CHAIN_ABUSE_API_KEY']
        log.info(f"API key: {self.api_key} TEST")
        self.auth = HTTPBasicAuth(self.api_key, self.api_key)

    def get_reports(self, request_params: ReportsRequest):
        return self.get_response(REPORTS_URL, request_params.to_params())

    #@retry(wait=wait_exponential(multiplier=1, min=15, max=300), stop=stop_after_attempt(5), after=after_log(log, logging.DEBUG))
    def get_response(self, url: str, params: Dict[Any, Any]):
        log.info(f"Request making with {params}")
        response = requests.get(url, headers=JSON_HEADERS, params=params, auth=self.auth)
        log.info(f"RAW RESPONSE:")
        log.info(dump.dump_all(response).decode('utf-8') + "\n")
        log.info(f"\nJSON data:")
        pprint(response.json())

        if response.status_code == 200:
            return response.json()
        elif response.status_code >= 400:
            raise ValueError(f"Request failed ({response.status_code}): {response.json()['reason']}")
        else:
            raise ValueError(f"Weird response code {response.status_code}!: {response.json()}")
