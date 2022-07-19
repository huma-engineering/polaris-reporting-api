import click
from flask import Flask
from flask_batteries_included.helpers.apispec import generate_openapi_spec

from dhos_reporting_api import blueprint_api
from dhos_reporting_api.models.api_spec import dhos_reporting_api_spec


def add_cli_command(app: Flask) -> None:
    @app.cli.command("create-openapi")
    @click.argument("output", type=click.Path())
    def create_api(output: str) -> None:
        generate_openapi_spec(
            dhos_reporting_api_spec, output, blueprint_api.api_blueprint
        )
