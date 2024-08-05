Command line application to manage virtual machines and their components across different infrastructures: local, cloud,
hybrid and hypervisors: qemu, kvm, others.

To be added: codecov, asciinemaa

Table of Contents
=================

* [Features](#features)
* [Prerequisites](#prerequisites)
  * [MacOS](#macos)
  * [Ubuntu/Debian](#ubuntu-debian)
* [Installation](#installation)
* [Usage](#usage)
* [Development](#development)
  * [Running the tests](#running-the-tests)
  * [Day 0 - Project setup](#day-0---project-setup)
  * [Day 1 - CLI](#day-1---cli)
  * [Day 2 - Virtual Machines](#day-2---virtual-machines)
  * [Day 3 - Package installation in running VM](#day-3---package-installation-in-running-vm)
  * [Day 4 - Virtual Machines Advanced](#day-4---virtual-machines-advanced)
  * [Day 5 - Automation for Continuous pipelines](#day-5---automation-for-continuous-pipelines)
  * [Day Z - Future](#day-z---future)

## Features

* Manage virtual machines with different hypervisors (currently only qemu)
* Manage networks (currently only qemu)
* Manage storage (currently only qemu)
* Cloning of virtual machines (currently only qemu)
* Automated OS installation of virtual machine (TBD)
* Package installation during OS installation (TBD)

## Prerequisites

> [!NOTE]
> If you are using a different distribution, please refer to the official documentation of the distribution.

### Ubuntu 24.04

```bash
  mkdir -p $HOME/libvirt/{iso,images}
  sudo apt update
  sudo apt install qemu-kvm libvirt-dev libvirt-daemon-system libvirt-clients bridge-utils pkg-config python3 python3-pip
  sudo setfacl -m u:$USER:rw /etc/libvirt/qemu
  sudo setfacl -m u:libvirt-qemu:rx $HOME/libvirt
  sudo systemctl start libvirtd
  sudo systemctl enable libvirtd #if you want to start libvirtd on boot (not necessary)
```
> [!TIP]
> You can check if libvirt is running by executing `systemctl status libvirtd`

## Installation

```bash
  git clone https://github.com/clistoq/zion
  cd zion
  sudo apt install python3-venv #if you want to use virtualenv; not needed
  python3 -m venv venv #follow up to the previous step
  source venv/bin/activate #follow up to the previous step
  pip install .
```

## Usage

[![asciicast](https://asciinema.org/a/Ig3VWkZEAesdPHx99a86XePkf.svg)](https://asciinema.org/a/Ig3VWkZEAesdPHx99a86XePkf)

Main help:
```bash
  Usage: zion [OPTIONS] COMMAND [ARGS]...

  Command line application to manage virtual machines and their components in
  local environment with QEMU hypervisor.

  Options:
    --help  Show this message and exit.

  Commands:
    domain  Commands to manage domains.
    hypervisor  Commands to manage the hypervisor.
    volume  Commands to manage storage pools and volumes.
```

Hypervisor help:
```bash
  Usage: zion hypervisor [OPTIONS] COMMAND [ARGS]...

  Commands to manage the hypervisor.

  Options:
    --help  Show this message and exit.

  Commands:
    state  Show human-readable status information about the hypervisor.
```

Domain help:
```bash
  Usage: zion domain [OPTIONS] COMMAND [ARGS]...

  Commands to manage domains.

  Options:
    --help  Show this message and exit.

  Commands:
    create    Create a new domain.
    delete    Delete a domain.
    duplicate Duplicate a domain.
    list      List all domains.
    start     Start a domain.
    status    Show human-readable status information about a domain.
    stop      Stop a domain.
```

Volume help:
```bash
  Usage: zion volume [OPTIONS] COMMAND [ARGS]...

  Commands to manage storage pools and volumes.

  Options:
    --help  Show this message and exit.

  Commands:
    create              Create a volume within a storage pool.
    create-storagepool  Create a new storage pool.
    delete              Delete a volume from a storage pool.
    delete-storagepool  Delete a storage pool.
    list                List volumes in the storage pool.
    list-storagepools   List all storage pools.

```

### Examples

Here you can find instruction how to provision simple domain with zion.
[simple-vm](examples/simple-vm/README.md)

## Development

### Running the tests

To be added!

### Day 0 - Project setup

- [x] Setuptools configuration
- [x] Project structure
- [x] Init package

### Day 1 - CLI

- [x] Create a CLI application
- [x] Create structure of CLI commands

### Day 2 - Virtual Machines

#### Hypervisors

- [x] CLI command group `hypervisors`
- [x] CLI command `status`

#### Domains

- [x] CLI command group `domains`
- [x] CLI command `list`
- [x] CLI command `create`
- [x] CLI command `delete`
- [x] CLI command `start`
- [x] CLI command `stop`
- [x] CLI command `status`
- [ ] Prepare test cases

#### Networking

- [ ] CLI command group `networks`
- [ ] CLI command `list`
- [ ] CLI command `create`
- [ ] CLI command `delete`
- [ ] CLI command `describe`
- [ ] Prepare test cases

#### Storage

- [x] CLI command group `storage`
- [x] CLI command `list`
- [x] CLI command `create`
- [x] CLI command `delete`
- [x] CLI command `describe`
- [ ] Prepare test cases

#### Cloning

- [x] CLI command in `domains` group `duplicate`
- [ ] Prepare test cases

### Day 3 - Package installation in running VM

- [ ] CLI command `install` in group `domains`
- [ ] Prepare test cases

### Day 4 - Virtual Machines Advanced

#### Interactive commands

- [ ] Add options to commands to remove hardcoded paths, etc.

#### Snapshots

#### Kickstart/Preseed configuration

#### Config file support

#### Hypervisor configuration support

### Day 5 - Automation for Continuous pipelines

- [ ] Align Dockerfile
- [ ] Prepare showcase
- [ ] Prepare CI/CD pipeline example

### Day Z - Future

- [ ] Add support for other hypervisors
- [ ] Add TUI
- [ ] Add `fzf` support inside TUI
- [ ] Add real time stats for all components
