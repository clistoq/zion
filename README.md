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

### MacOS

```bash
  brew install qemu libvirt
  brew services start libvirt
```
### Ubuntu/Debian

```bash
  sudo apt update
  sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
  sudo systemctl start libvirtd
  sudo systemctl enable libvirtd #if you want to start libvirtd on boot (not necessary)
```
> [!TIP]
> You can check if libvirt is running by executing `systemctl status libvirtd`

## Installation

```bash
  git clone https://github.com/clistoq/zion
  cd zion
  pip install .
```

## Usage

```bash
  zion --help
  Usage: zion [OPTIONS]

  Options:
    --help  Show this message and exit.
```

## Development

### Running the tests

To be added!

### Day 0 - Project setup

- [x] Setuptools configuration
- [x] Project structure
- [x] Init package

### Day 1 - CLI

- [x] Create a CLI application
- [ ] Create structure of CLI commands

### Day 2 - Virtual Machines

#### Hypervisors

- [ ] CLI command group `hypervisors`
- [ ] CLI command `state`

#### Domains

- [ ] CLI command group `domains`
- [ ] CLI command `list`
- [ ] CLI command `create`
- [ ] CLI command `delete`
- [ ] CLI command `start`
- [ ] CLI command `stop`
- [ ] CLI command `describe`
- [ ] Prepare test cases

#### Networking

- [ ] CLI command group `networks`
- [ ] CLI command `list`
- [ ] CLI command `create`
- [ ] CLI command `delete`
- [ ] CLI command `describe`
- [ ] Prepare test cases

#### Storage

- [ ] CLI command group `storage`
- [ ] CLI command `list`
- [ ] CLI command `create`
- [ ] CLI command `delete`
- [ ] CLI command `describe`
- [ ] Prepare test cases

#### Cloning

- [ ] CLI command in `domains` group `clone`
- [ ] Prepare test cases

### Day 3 - Package installation in running VM

- [ ] CLI command `install` in group `domains`
- [ ] Prepare test cases

### Day 4 - Virtual Machines Advanced

#### Snapshots

#### Kickstart configuration

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
