import click

from zion.devices import storage
from zion.domain import create, destroy, duplicate, helpers
from zion.hypervisor import hypervisor


@click.group(
    help="Command line application to manage virtual machines and their components in local environment with QEMU hypervisor."
)
def cli():
    pass


@cli.group(name="hypervisor", help="Commands to manage the hypervisor.")
def hypervisor_group():
    pass


@cli.group(name="domain", help="Commands to manage domains.")
def domain():
    pass


@cli.group(name="volume", help="Commands to manage storage pools and volumes.")
def volume():
    pass


hypervisor_group.add_command(hypervisor.status)


domain.add_command(create.create)
domain.add_command(destroy.destroy)
domain.add_command(duplicate.duplicate)
domain.add_command(helpers.list)
domain.add_command(helpers.status)
domain.add_command(helpers.start)
domain.add_command(helpers.stop)


volume.add_command(storage.list)
volume.add_command(storage.create)
volume.add_command(storage.delete)
volume.add_command(storage.list_storagepools)
volume.add_command(storage.create_storagepool)
volume.add_command(storage.delete_storagepool)
