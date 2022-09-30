# This is a sample Python script.
from fastapi import FastAPI
from pydantic import BaseModel
from calculate import calculate


class User_input(BaseModel):
	operation: str
	x: float
	y: float


# Creating a new FastAPI object.
app = FastAPI()


@app.post("/calculate")
def operate(input: User_input):
	return calculate(input.operation, input.x, input.y)

