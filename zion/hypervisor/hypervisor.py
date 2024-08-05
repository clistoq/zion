import sys

import click
import libvirt


def open_connection():
    conn = libvirt.open("qemu:///system")

    if conn is None:
        print("Failed to open connection to qemu:///system", file=sys.stderr)
        exit(1)

    return conn


def close_connection(conn):
    conn.close()


@click.command(
    help="Show human-readable status information about the hypervisor."
)
def status():
    conn = open_connection()

    try:
        hostname = conn.getHostname()
        version = conn.getVersion()
        hypervisor_type = conn.getType()
        lib_version = conn.getLibVersion()
        max_vcpus = conn.getMaxVcpus(None)
        max_memory = conn.getFreeMemory()  # TODO: count usable amount of memory

        click.echo(f"Hypervisor Hostname: {hostname}")
        click.echo(f"Hypervisor Version: {version}")
        click.echo(f"Hypervisor Type: {hypervisor_type}")
        click.echo(f"Libvirt Version: {lib_version}")
        click.echo(f"Maximum VCPUs: {max_vcpus}")
        click.echo(f"Maximum Memory: {max_memory} KiB")
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to get the status of the hypervisor: {e}", file=sys.stderr
        )
        sys.exit(1)
    finally:
        close_connection(conn)
