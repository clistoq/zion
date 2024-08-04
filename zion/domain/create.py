import sys

import click
import libvirt

from zion.hypervisor import hypervisor


@click.command()
def create():
    xml_desc = """
    <domain type='qemu'>
      <name>debian12_vm</name>
      <memory unit='KiB'>1048576</memory>
      <vcpu placement='static'>1</vcpu>
      <os>
        <type arch='x86_64' machine='pc-i440fx-2.9'>hvm</type>
        <boot dev='cdrom'/>
      </os>
      <devices>
        <disk type='file' device='disk'>
          <driver name='qemu' type='qcow2'/>
          <source file='/var/lib/libvirt/images/debian12_vm.qcow2'/>
          <target dev='vda' bus='virtio'/>
        </disk>
        <disk type='file' device='cdrom'>
          <driver name='qemu' type='raw'/>
          <source file='/tmp/debian-12.6.0-amd64-netinst.iso'/>
          <target dev='hda' bus='ide'/>
          <readonly/>
        </disk>
        <interface type='network'>
          <mac address='52:54:00:6b:3c:58'/>
          <source network='default'/>
          <model type='virtio'/>
        </interface>
      </devices>
      <metadata>
        <install>
          <autostart>true</autostart>
          <kickstart>
            <file>/tmp/debian12-preseed.cfg</file>
          </kickstart>
        </install>
      </metadata>
    </domain>
    """

    conn = hypervisor.open_connection()

    try:
        dom = conn.createXML(xml_desc, 0)
        if dom is None:
            click.echo("Failed to create the domain", file=sys.stderr)
            sys.exit(1)
        click.echo("Domain has been created")
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(f"Failed to create the domain: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
