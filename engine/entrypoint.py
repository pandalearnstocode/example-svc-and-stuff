import typer
from src.addition.addition import add_numbers as _add_numbers

app = typer.Typer()


@app.command()
def add_numbers(num1: int, num2: int):
    result = _add_numbers(num1, num2)
    typer.echo(f"The sum of {num1} and {num2} is {result}")


if __name__ == "__main__":
    app()
