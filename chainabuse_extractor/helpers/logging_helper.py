import logging

from rich.logging import RichHandler

from chainabuse_extractor.helpers.string_constants import PACKAGE_NAME


log = logging.getLogger(PACKAGE_NAME)
log.setLevel('DEBUG')
rich_stream_handler = RichHandler(rich_tracebacks=True)
rich_stream_handler.setLevel('DEBUG')
log.addHandler(rich_stream_handler)
