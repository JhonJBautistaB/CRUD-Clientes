import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Adminitración de Clientes Importante"""
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The Client name')
@click.option('-c', '--company', type=str, prompt=True, help='The Client company')
@click.option('-e', '--email', type=str, prompt=True, help='The Client email')
@click.option('-p', '--position', type=str, prompt=True, help='The Client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Crear un Nuevo Cliente"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """Listar todos los Cientes"""
    pass


@clients.command()
@click.pass_context
def update(ctx, clientes_uid):
    """Actualixzar Clientes"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, clientes_uid):
    """Eliminar Clientes"""
    pass


all = clients