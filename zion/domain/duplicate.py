import sys
import uuid

import click
import libvirt

from zion.hypervisor import hypervisor


@click.command(help="Duplicate an existing domain.")
@click.argument("domain_name", required=True)
@click.argument("new_domain_name", required=True)
def duplicate(domain_name, new_domain_name):
    conn = hypervisor.open_connection()

    try:
        dom = conn.lookupByName(domain_name)
        if dom is None:
            click.echo(
                f"Failed to find the domain {domain_name}", file=sys.stderr
            )
            sys.exit(1)
        xml_desc = dom.XMLDesc()

        new_xml_desc = xml_desc.replace(domain_name, new_domain_name)
        new_xml_desc = new_xml_desc.replace(
            f"<uuid>{dom.UUIDString()}</uuid>", f"<uuid>{uuid.uuid4()}</uuid>"
        )

        new_dom = conn.defineXML(new_xml_desc)

        if new_dom is None:
            click.echo(
                f"Failed to create the domain {new_domain_name}",
                file=sys.stderr,
            )
            sys.exit(1)

        click.echo(f"Domain {new_domain_name} has been duplicated")

        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to duplicate the domain {domain_name}: {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
