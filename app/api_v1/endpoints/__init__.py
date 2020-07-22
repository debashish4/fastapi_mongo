from fastapi import APIRouter

from .healthcheck import router as hc_router
from .fastapiPrac import router as rroot
from .students import router as student_router
from .expenseTracker import router as expense_tracker_router

router = APIRouter()

__all__ = ["router"]

router.include_router(hc_router)
router.include_router(rroot)
router.include_router(student_router)
router.include_router(expense_tracker_router)
# Include all the endpoint routers for this app.