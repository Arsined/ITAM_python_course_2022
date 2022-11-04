from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Student(BaseModel):
    id: str
    name: str
    group: str


@app.get("/student/all/")
def get_all():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


@app.post("/student/add/")
def add_student(student: Student):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    data[student.id] = [student.name, student.group]
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
    return "success"


@app.get("/student/{student_id}/")
def get_student(student_id: str):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return {student_id: data[student_id]}

@app.put("/student/update/")
def update_student(student: Student):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    data[str(student.id)] = [student.name, student.group]
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
    return "success"


import uvicorn


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)