from fastapi import FastAPI
from src.create_svc import create_calculation
from src.models import Calculation, CalculationBase

from engine.src.addition.addition import add_numbers as _add_numbers

app = FastAPI()


def add_numbers(num1: int, num2: int) -> Calculation:
    result = _add_numbers(num1=num1, num2=num2)
    calculation = create_calculation(num1, num2, result)
    return calculation


@app.post("/add/")
def add_numbers_endpoint(calculation: CalculationBase):
    result = add_numbers(calculation.num1, calculation.num2)
    return {"result": result}
