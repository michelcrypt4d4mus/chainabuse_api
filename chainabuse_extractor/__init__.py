from chainabuse_extractor.api import Api
from chainabuse_extractor.reports_request import ReportsRequest
from chainabuse_extractor.helpers.argument_parser import parse_args


def get_chainabuse_reports():
    args = parse_args()
    api = Api()
    reports_request = ReportsRequest()

