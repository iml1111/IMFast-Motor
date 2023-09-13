"""
Application Management Module
"""
import asyncio
import click
from fastapi import FastAPI
from app import create_app
from model import mongodb
from model.mongodb.initializer import ModelInitializer
from settings import Settings

application: FastAPI = create_app(Settings())


@click.group()
def cli():
    """Command Groups"""


@cli.command()
def init_db():
    """Sample command"""
    initializer = ModelInitializer(application.mongodb)
    asyncio.run(initializer.init_model())
    click.echo("DB initialized.")


@cli.command()
def routes():
    """Print all routes"""
    click.echo('# Routes')
    routes = []
    path_len = 0
    method_len = 0
    name_len = 0

    for route in application.routes:
        routes.append((
            route.path, str(route.methods), route.name))
        path_len = max(path_len, len(route.path))
        method_len = max(method_len, len(str(route.methods)))
        name_len = max(name_len, len(route.name))

    click.echo(
        f"{'Path ':=<{path_len + 2}}"
        f"{' Methods ':=<{method_len + 1}}"
        f"{' Name ':=<{name_len + 1}}")
    for route in sorted(routes):
        click.echo(
            f'{route[0]: <{path_len + 2}}'
            f'{route[1]: <{method_len + 2}}'
            f'{route[2]: <{name_len + 2}}')


@cli.command()
def run():
    """Please use 'imfast run'."""
    raise NotImplementedError("Please use 'imfast.sh run'.")


@cli.command()
def prod_run():
    """Please use 'imfast prod-run'."""
    raise NotImplementedError("Please use 'imfast.sh prod-run'.")


@cli.command()
def test():
    """Run tests"""
    raise NotImplementedError("Please use 'imfast.sh test'.")


if __name__ == '__main__':
    cli()
