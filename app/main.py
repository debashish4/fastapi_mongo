import os
import sys

from collections import namedtuple

# Add the current application to path
# This allows import without any prefix dots.
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Do not move these imports to top
from api_v1.endpoints import router as app_v1
from core.utils import setup_application

SubApp = namedtuple("SubApp", ["prefix", "router"])

# Add all the SubApp for registration
sub_applications = [
    SubApp("/api/v1", app_v1)
]


app = setup_application(
    title="test",
    description="test desc",
    sub_applications=sub_applications
)

