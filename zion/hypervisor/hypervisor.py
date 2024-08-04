import sys

import libvirt


def open_connection():
    conn = libvirt.open("qemu:///system")
    if conn is None:
        print("Failed to open connection to qemu:///system", file=sys.stderr)
        exit(1)
    return conn


def close_connection(conn):
    conn.close()
