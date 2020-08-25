import click

@click.group()
def Clientes():
    """Adminitración de Clientes Importante"""
    pass


@Clientes.command()
@click.pass_context
def crear(contexto, nombre, compania, email, cargo):
    """Crear un Nuevo Cliente"""
    pass


@Clientes.command()
@click.pass_context
def listar(ctx):
    """Listar todos los Cientes"""
    pass


@Clientes.command()
@click.pass_context
def actualizar(ctx, clientes_uid):
    """Actualixzar Clientes"""
    pass


@Clientes.command()
@click.pass_context
def Eliminar(ctx, clientes_uid):
    """Eliminar Clientes"""
    pass


all = Clientes