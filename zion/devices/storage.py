import os
import sys
import uuid

import click
import libvirt

from zion.hypervisor import hypervisor


@click.command(help="List volumes in the storage pool.")
@click.argument("storage_pool_name", type=str, required=True)
def list(storage_pool_name):
    conn = hypervisor.open_connection()

    try:
        pool = conn.storagePoolLookupByName(storage_pool_name)
        if pool is None:
            click.echo(
                f"Failed to find the storage pool {storage_pool_name}",
                file=sys.stderr,
            )
            sys.exit(1)

        volumes = pool.listVolumes()
        if not volumes:
            click.echo(
                f"No volumes found in the storage pool {storage_pool_name}"
            )
        else:
            click.echo(volumes)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to list volumes in the storage pool {storage_pool_name}: {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="Create a volume within a storage pool.")
@click.argument("name", type=str, required=True)
@click.argument("storage_pool_name", type=str, required=True)
def create(name, storage_pool_name):
    volume_xml = f"""
        <volume>
          <name>{name}.img</name>
          <allocation>0</allocation>
          <capacity unit="G">10</capacity>
          <target>
            <path>{os.path.expanduser("~")}/libvirt/images/{name}.img</path>
            <format type='qcow2'/>
            <permissions>
              <owner>64055</owner>
              <group>993</group>
              <mode>0744</mode>
              <label>virt_image_t</label>
            </permissions>
          </target>
        </volume>"""

    conn = hypervisor.open_connection()

    try:
        pool = conn.storagePoolLookupByName(storage_pool_name)
        if pool is None:
            click.echo(
                f"Failed to find the storage pool {storage_pool_name}",
                file=sys.stderr,
            )
            sys.exit(1)

        volume = pool.createXML(volume_xml, 0)
        click.echo(volume)
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(f"Failed to create the volume {name}: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="Delete a volume from a storage pool.")
@click.argument("volume_name", type=str, required=True)
@click.argument("storage_pool_name", type=str, required=True)
def delete(volume_name, storage_pool_name):
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

        vol.delete(0)
        click.echo(f"Volume {volume_name} has been deleted")
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to delete the volume {volume_name}: {e}", file=sys.stderr
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="List all storage pools.")
def list_storagepools():
    conn = hypervisor.open_connection()

    try:
        pools = conn.listStoragePools()
        if not pools:
            click.echo("No storage pools found")
        else:
            click.echo(pools)
    except libvirt.libvirtError as e:
        click.echo(f"Failed to list storage pools: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="Create a new storage pool.")
@click.argument("name", type=str, required=True)
def create_storagepool(name):
    strpool_xml = f"""
            <pool type='dir'>
              <name>{name}</name>
              <uuid>{uuid.uuid4()}</uuid>
              <capacity unit='bytes'>4306780815</capacity>
              <allocation unit='bytes'>237457858</allocation>
              <available unit='bytes'>4069322956</available>
              <source>
              </source>
              <target>
                <path>{os.path.expanduser("~")}/libvirt/images</path>
                <permissions>
                  <mode>0755</mode>
                  <owner>64055</owner>
                  <group>993</group>
                </permissions>
              </target>
            </pool>"""

    conn = hypervisor.open_connection()

    try:
        pool = conn.storagePoolDefineXML(strpool_xml, 0)
        pool.setAutostart(1)
        pool.create()
        click.echo(pool)
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to create the storage pool {name}: {e}", file=sys.stderr
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)


@click.command(help="Delete a storage pool.")
@click.argument("storage_pool_name", type=str, required=True)
def delete_storagepool(storage_pool_name):
    conn = hypervisor.open_connection()

    try:
        pool = conn.storagePoolLookupByName(storage_pool_name)
        if pool is None:
            click.echo(
                f"Failed to find the storage pool {storage_pool_name}",
                file=sys.stderr,
            )
            sys.exit(1)

        pool.destroy()
        pool.undefine()
        click.echo(f"Storage pool {storage_pool_name} has been deleted")
        sys.exit(0)
    except libvirt.libvirtError as e:
        click.echo(
            f"Failed to delete the storage pool {storage_pool_name}: {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    finally:
        hypervisor.close_connection(conn)
