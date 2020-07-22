import time
from enum import IntEnum

import psutil
from fastapi import APIRouter

from config import settings
from api_v1 import models


router = APIRouter(IntEnum)

class HealthStatus(IntEnum):
    PASS = 0
    WARN = 1
    FAIL = 2


def cpu_health() -> dict:
    """
    cpu_health checks the current percent of CPU usage and
    returns it as a HealthComponent

    Returns
    -------
    dict
        A valid HealthComponent dictionary
    """
    cpu_percent = psutil.cpu_percent(interval=0.1)
    status = HealthStatus.PASS
    if 71 <= cpu_percent <= 95:
        status = HealthStatus.WARN
    elif cpu_percent > 95:
        status = HealthStatus.FAIL
    return {
        "component_type": "system",
        "metric_value": cpu_percent,
        "metric_unit": "percent",
        "status": status.name,
        "timestamp": time.time()
    }

def memory_health() -> dict:
    """
    memory_health checks the current percent of memory usage and
    returns it as a HealthComponent

    Returns
    -------
    dict
        A valid HealthComponent dictionary
    """
    memory_percent = psutil.virtual_memory().percent
    status = HealthStatus.PASS
    if 81 <= memory_percent <= 95:
        status = HealthStatus.WARN
    elif memory_percent > 95:
        status = HealthStatus.FAIL
    return {
        "component_type": "system",
        "metric_value": memory_percent,
        "metric_unit": "percent",
        "status": status.name,
        "timestamp": time.time()
    }


@router.get("/healthcheck", response_model=models.HealthResponse)
async def healthcheck():
    all_status = []
    current_cpu_health = cpu_health()
    all_status.append(HealthStatus[current_cpu_health["status"]])

    current_memory_health = memory_health()
    all_status.append(HealthStatus[current_memory_health["status"]])

    health_details = {
        "cpu:utilization": [
            current_cpu_health,
        ],
        "memory:utilization": [
            current_memory_health
        ]
    }
    
    return {
        "status": HealthStatus(max(all_status)).name,
        "version": ".".join(settings.VERSION),
        "details": health_details
    }
