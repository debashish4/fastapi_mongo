from enum import IntEnum
from enum import Enum
import psutil
from typing import List, Optional, Dict
from fastapi import APIRouter
from pydantic import BaseModel
from db.mongodb import mydb

studentCol =  mydb["students"]
router = APIRouter(IntEnum)

# LIST ALL
@router.get("/list-all-students")
def allStudentData():
    students = studentCol.find({"studentId": 2})
    for student in students:
        print(student)
    # return {"a": "s"}
    
# ADD STUDENTS
class Student(BaseModel):
    studentId: int
    studentName: str
    studentAge: str


@router.post("/addstudents")
def addStudent(students: List[Student]):
    mystudentList = [] 
    for student in students:
        mystudentList.append(dict(student))
    studentCol.insert_many(mystudentList)


#ADD STUDENT
@router.post("/addstudent")
def addStudents(student: Student):
    print("studen data: ", student)
    studentCol.insert_one(dict(student))


# DELETE STUDENT
@router.delete("/deletestudent/{student_id}")
def deleteStudent(student_id: int):
    print("student id", student_id)
    x = studentCol.find_one({"studentId": student_id})
    print("xxxxx is ", x)
    studentCol.delete_one(dict(x))

#DELETE STUDENTS
@router.delete("/deletestudents")
def deleteStudents(student: dict):
   
    studentIds = list(student['ids'])
    print("student ids is: ", studentIds)
    for id in studentIds:
        print("id is", id)
        item = studentCol.find({"studentId": 3})
        print("item", item)
        studentCol.delete_many(dict(item))

