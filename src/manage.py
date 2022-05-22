import asyncio

import typer

from src.utils.db_manager import db_upgrade, db_downgrade
app = typer.Typer()


@app.command()
def upgrade():
    typer.echo(typer.style("start upgrade cmd", bold=True))
    asyncio.run(db_upgrade())
    typer.echo(typer.style("The Migrations runs successfully", fg=typer.colors.GREEN, bold=True))


@app.command()
def downgrade():
    typer.echo(typer.style("start downgrade cmd", bold=True))
    asyncio.run(db_downgrade())
    typer.echo(typer.style("The Migrations runs successfully", fg=typer.colors.GREEN, bold=True))


if __name__ == "__main__":
    app()
