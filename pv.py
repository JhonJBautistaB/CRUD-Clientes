import click
from clients import commands as clientes_commandos


@click.group()
@clic.pass_context()
def cli(ctx):
    ctx.obj = {}

cli.add_command(clientes_commandos.all)