import pendulum

from chainabuse_extractor.api import Api
from chainabuse_extractor.helpers.logging_helper import log
from chainabuse_extractor.reports_request import ReportsRequest


since = pendulum.datetime(2020, 1, 1)
until = pendulum.datetime(2023, 6, 1)

request = ReportsRequest(
    since=since,
    before=until,
    trusted=True,
    min_loss_amount=10000.0
)

print(request.to_params())
api = Api()
reports = api.get_reports(request)
