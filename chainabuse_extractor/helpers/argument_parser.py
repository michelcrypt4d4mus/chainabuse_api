from argparse import ArgumentParser, Namespace
from os import environ
from pathlib import Path
from sys import exit

from rich.logging import RichHandler

from chainabuse_extractor.helpers.logging_helper import log
from chainabuse_extractor.helpers.string_constants import PACKAGE_NAME


parser = ArgumentParser(
    description='Get scammer addresses from chainabuse.com reports. ',
    epilog='Epilog.'
)

parser.add_argument('-s', '--since',
                    help='extract transactions up to and including this time (ISO 8601 Format)',
                    metavar='DATETIME')

parser.add_argument('-u', '--until',
                    help='extract transactions starting from this time (ISO 8601 Format)',
                    metavar='DATETIME')

# TODO: this should accept an S3 URI.
parser.add_argument('-o', '--output-dir',
                    help='write transaction CSVs to a file in this directory',
                    metavar='OUTPUT_DIR')

parser.add_argument('-r', '--resume-csv',
                    help='resume extracting to a partially extracted CSV file',
                    metavar='CSV_FILE')

parser.add_argument('-d', '--debug', action='store_true',
                    help='set LOG_LEVEL to DEBUG (can also be set with the LOG_LEVEL environment variable)')


def parse_args() -> Namespace:
    args = parser.parse_args()
    setup_logging(args)
    args.output_dir = Path(args.output_dir or '')
    args.resume_csv = Path(args.resume_csv) if args.resume_csv else None

    if args.since:
        since = str_to_timestamp(args.since)
        log.info(f"Requested records since '{args.since}' which parsed to {since}.")
        args.since = since

    if args.until:
        until = str_to_timestamp(args.until)
        log.info(f"Requested records until '{args.until}' which parsed to {until}.")
        args.until = until

    log.debug(f"Processed arguments: {args}")
    return args


def setup_logging(args: Namespace) -> None:
    log_level = 'DEBUG' if args.debug else environ.get('LOG_LEVEL', 'INFO')
    log.setLevel(log_level)
    rich_stream_handler = RichHandler(rich_tracebacks=True)
    rich_stream_handler.setLevel(log_level)
    log.addHandler(rich_stream_handler)
