import os
import logging


# The base directory of the application.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Semantic versioning of the application.
VERSION = ("1", "0", "0")

# Add application specific settings here.

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'short': {
            'class': 'logging.Formatter',
            'format': '%(levelname)-s: %(message)s',
        },
        'long': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)s: %(levelname)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'long',
            'filename': 'logs/test.log',
            'backupCount': 10,
            'maxBytes': 50000000
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'short',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        "test": {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': 0
        }
    }
}
