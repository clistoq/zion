import sys

import click
import libvirt

from zion.hypervisor import hypervisor


@click.command()
def list():
    conn = hypervisor.open_connection()

    try:
        domains = conn.listAllDomains()
        if not domains:
            click.echo("Failed to list domains", file=sys.stderr)
        else:
            domain_names = [dom.name() for dom in domains]
            click.echo(domain_names)
    except libvirt.libvirtError as e:
        click.echo(f"Failed to list domains: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command()
@click.argument("domain_name", type=str, required=True)
def status(domain_name):
    conn = hypervisor.open_connection()

    try:
        dom = conn.lookupByName(domain_name)
        if dom is None:
            click.echo(
                f"Failed to find the domain {domain_name}", file=sys.stderr
            )
        state, reason = dom.state()
        click.echo(state)
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to get the status of the domain {domain_name}: {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
