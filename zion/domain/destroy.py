import sys

import click
import libvirt

from zion.hypervisor import hypervisor


@click.command(help="Delete a domain.")
@click.argument("domain_name", type=str, required=True)
def destroy(domain_name):
    conn = hypervisor.open_connection()

    try:
        dom = conn.lookupByName(domain_name)
        if dom is None:
            click.echo(
                f"Failed to find the domain {domain_name}", file=sys.stderr
            )
            sys.exit(1)
        dom.undefine()
        click.echo(f"Domain {domain_name} has been destroyed")
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to destroy the domain {domain_name}: {e}", file=sys.stderr
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
