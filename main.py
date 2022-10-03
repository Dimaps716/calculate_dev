from fastapi import FastAPI
from pydantic import BaseModel
from src.calculate import calculate


class User_Input(BaseModel):
	operation: str
	x: float
	y: float


# Creating a new FastAPI object.
app = FastAPI()


@app.post("/calculate")
def operate(input_user: User_Input):
	"""
	`operate` takes a `User_input` object and returns the result of `calculate` with the `operation`, `x`, and `y`
	attributes of the `User_input` object
	**param** input: User_input
	**type** input: User_input
	**return** The result of the calculation.
	"""
	return calculate(input_user.operation, input_user.x, input_user.y)

