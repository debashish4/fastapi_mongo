from enum import IntEnum
from enum import Enum
import psutil
from typing import List, Optional, Dict
from fastapi import APIRouter
from pydantic import BaseModel
from db.mongodb import mydb



expenseTrackerCol =  mydb["expense_tracker"]
router = APIRouter(IntEnum)



#POST INCOME

class Income(BaseModel):
    amount: int
    category: str
    date: str
    paymentMode: str

class Amount(BaseModel):
    totalIncome: int


# ADD TOTAL AMOUNT
@router.post("/addIncome")
def addIncome(totalIncome: Amount):
    print(totalIncome)
    # expenseTrackerCol.find({"totalIncome": {$gt: 0}})
    expenseTrackerCol.insert_one(dict(totalIncome))


# # ALL INCOME LIST
# @router.post("/addIncomeList")
# def addIncomeList(income: List(Income)):
#     print(income)
#     expenseTrackerCol.insert_one(dict(income))



