import click

@click.group()
def hello():
    click.echo('Hello World!')

@hello.command()
@click.option('--host', default=1,type=str, help='Host to init')
@click.argument('name')
def initdb(host, name):
    click.echo('Init db %s=%s' % (name, host) )

@hello.command()
def dropdb():
    click.echo('Drop db')

if __name__ == '__main__':
    hello()