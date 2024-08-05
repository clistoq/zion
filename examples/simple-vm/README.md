Instruction how to create a new domain using `zion`.
Actual capabilities are very limited.

## Prerequisites

You need to download the Debian 12 ISO image from the official website and put it in previously created `iso` directory.
```bash
  curl -L --verbose --output $HOME/libvirt/iso/debian12.iso "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.6.0-amd64-netinst.iso"
```

## Usage

```bash
  zion volume create-storagepool libvirt #path is currently half hardcoded; it will bind to $HOME/libvirt/images
  zion volume create debian12 libvirt
  zion domain create debian12 debian12 libvirt debian12 #name, volume, storagepool, iso_name
```

[![asciicast](https://asciinema.org/a/z8aGrvxkc9JhSmxgjIT8gPZkA.svg)](https://asciinema.org/a/z8aGrvxkc9JhSmxgjIT8gPZkA)
