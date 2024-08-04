import click

from zion.domain import create, destroy, duplicate, helpers


@click.group()
def cli():
    pass


@cli.group("domain")
def domain():
    pass


domain.add_command(create.create)
domain.add_command(destroy.destroy)
domain.add_command(duplicate.duplicate)
domain.add_command(helpers.list)
domain.add_command(helpers.status)
