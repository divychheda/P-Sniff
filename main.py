import click

@click.command()
@click.option('--protocol', default="all", help='The protocol whose traffic you want filtered.')
@click.option('--port', default="all", help='The port whose traffic you want filtered.')
@click.option('--ip', default="all", help='The IP address whose traffic you want filtered.')
def main(protocol, port, ip):
    # sniffer(protocol, port, ip)
    pass
    