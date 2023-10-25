from pydantic import BaseModel


class CalculationBase(BaseModel):
    num1: int
    num2: int


class Calculation(BaseModel):
    num1: int
    num2: int
    result: float
