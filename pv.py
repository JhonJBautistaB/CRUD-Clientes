import click
from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {} #Se crea el diccionario despues de enviar el contexto
    ctx.obj['clients_table'] = CLIENTS_TABLE

cli.add_command(clients_commands.all) #Realiza la operación que se invoca desde  commands