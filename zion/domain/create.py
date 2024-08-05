import os
import sys

import click
import libvirt

from zion.hypervisor import hypervisor


@click.command(help="Create a new domain.")
@click.argument("name", type=str, required=True)
@click.argument("volume_name", type=str, required=True)
@click.argument("storage_pool_name", type=str, required=True)
@click.argument("iso_name", type=str, required=True)
def create(name, volume_name, storage_pool_name, iso_name):
    conn = hypervisor.open_connection()

    try:
        pool = conn.storagePoolLookupByName(storage_pool_name)
        if pool is None:
            click.echo(
                f"Failed to find the storage pool {storage_pool_name}",
                file=sys.stderr,
            )
            sys.exit(1)

        vol = pool.storageVolLookupByName(volume_name + ".img")
        if vol is None:
            click.echo(
                f"Failed to find the volume {volume_name} in the storage pool {storage_pool_name}",
                file=sys.stderr,
            )
            sys.exit(1)

        vol_path = vol.path()

        xml_desc = f"""
            <domain type='qemu'>
              <name>{name}</name>
              <memory unit='GiB'>2</memory>
              <vcpu placement='static'>1</vcpu>
              <os>
                <type arch='x86_64' machine='pc-i440fx-2.9'>hvm</type>
                <boot dev='cdrom'/>
              </os>
              <devices>
                <disk type='file' device='disk'>
                  <driver name='qemu' type='qcow2'/>
                  <source file='{vol_path}'/>
                  <target dev='vda' bus='virtio'/>
                </disk>
                <disk type='file' device='cdrom'>
                  <driver name='qemu' type='raw'/>
                  <source file='{os.path.expanduser("~")}/libvirt/iso/{iso_name}.iso'/>
                  <target dev='hda' bus='ide'/>
                  <readonly/>
                </disk>
                <interface type='network'>
                  <mac address='52:54:00:6b:3c:58'/>
                  <source network='default'/>
                  <model type='virtio'/>
                </interface>
                <graphics type='vnc' port='-1' autoport='yes' />
              </devices>
            </domain>
            """

        dom = conn.defineXML(xml_desc)
        if dom is None:
            click.echo("Failed to define the domain", file=sys.stderr)
            sys.exit(1)
        click.echo("Domain has been created")

        dom.create()
        click.echo(f"Domain {name} has been started")
        sys.exit(0)

    except libvirt.libvirtError as e:
        click.echo(f"Failed to create the domain: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
