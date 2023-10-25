import typer
from src.create_svc import create_calculation as _create_calculation

app = typer.Typer()


@app.command()
def create_calculation(num1: int, num2: int, result: int):
    result = _create_calculation(num1, num2, result)
    typer.echo(f"Calculation created: {result}")


if __name__ == "__main__":
    app()
