import sys

import click
import libvirt

from zion import hypervisor


@click.command()
@click.argument("vm_name", type=str, required=True)
@click.argument("new_vm_name", type=str, required=True)
def duplicate(vm_name, new_vm_name):
    conn = hypervisor.open_connection()

    try:
        dom = conn.lookupByName(vm_name)
        if dom is None:
            click.echo(f"Failed to find the domain {vm_name}", file=sys.stderr)
            sys.exit(1)
        xml_desc = dom.XMLDesc()
        new_dom = conn.createXML(xml_desc.replace(vm_name, new_vm_name), 0)
        if new_dom is None:
            click.echo(
                f"Failed to create the domain {new_vm_name}", file=sys.stderr
            )
            sys.exit(1)
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to duplicate the domain {vm_name}: {e}", file=sys.stderr
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
