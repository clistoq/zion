import sys

import click
import libvirt

from zion.hypervisor import hypervisor


@click.command(help="Show all existing domains.")
def list():
    conn = hypervisor.open_connection()

    try:
        domains = conn.listAllDomains()
        if not domains:
            click.echo("No domains found")
        else:
            domain_names = [dom.name() for dom in domains]
            click.echo(domain_names)
    except libvirt.libvirtError as e:
        click.echo(f"Failed to list domains: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="Show human-readable status information about a domain.")
@click.argument("domain_name", type=str, required=True)
def status(domain_name):
    conn = hypervisor.open_connection()

    try:
        dom = conn.lookupByName(domain_name)
        if dom is None:
            click.echo(
                f"Failed to find the domain {domain_name}", file=sys.stderr
            )
            sys.exit(1)

        state, reason = dom.state()
        state_str = {
            libvirt.VIR_DOMAIN_NOSTATE: "No state",
            libvirt.VIR_DOMAIN_RUNNING: "Running",
            libvirt.VIR_DOMAIN_BLOCKED: "Blocked",
            libvirt.VIR_DOMAIN_PAUSED: "Paused",
            libvirt.VIR_DOMAIN_SHUTDOWN: "Shutting down",
            libvirt.VIR_DOMAIN_SHUTOFF: "Shut off",
            libvirt.VIR_DOMAIN_CRASHED: "Crashed",
            libvirt.VIR_DOMAIN_PMSUSPENDED: "Suspended",
        }.get(state, "Unknown")

        click.echo(
            f"Domain {domain_name} is currently {state_str} (Reason: {reason})"
        )
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to get the status of the domain {domain_name}: {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="Start domain.")
@click.argument("domain_name", type=str, required=True)
def start(domain_name):
    conn = hypervisor.open_connection()

    try:
        dom = conn.lookupByName(domain_name)
        if dom is None:
            click.echo(
                f"Failed to find the domain {domain_name}", file=sys.stderr
            )
            sys.exit(1)

        dom.create()
        click.echo(f"Domain {domain_name} has been started")
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to start the domain {domain_name}: {e}", file=sys.stderr
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="Stop domain.")
@click.argument("domain_name", type=str, required=True)
def stop(domain_name):
    conn = hypervisor.open_connection()

    try:
        dom = conn.lookupByName(domain_name)
        if dom is None:
            click.echo(
                f"Failed to find the domain {domain_name}", file=sys.stderr
            )
            sys.exit(1)

        dom.destroy()
        click.echo(f"Domain {domain_name} has been stopped")
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to stop the domain {domain_name}: {e}", file=sys.stderr
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
