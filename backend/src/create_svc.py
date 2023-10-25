import sqlite3

from .models import Calculation


def create_calculation(num1: int, num2: int, result: int):
    calculation = Calculation(num1=num1, num2=num2, result=result)
    with sqlite3.connect("calculations.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS calculations (num1 int, num2 int, result int)")
        c.execute("INSERT INTO calculations VALUES (?, ?, ?)", (num1, num2, result))
        conn.commit()
    return calculation
