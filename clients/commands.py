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
    client_services = ClientService(ctx.obj['clients_table'])

    client_list = client_services.list_clients()

    click.echo(' ID   |  NAME  | COMPANY  |  EMAIL |  POSITION')
    click.echo('*'*100)

    for client in client_list:
        click.echo('{uid} | {name} | {company} | {email} | {position}'. format(
            uid = client['uid'],
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))


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