# Embedded file name: vnc_bypass.py
import socket


def assign(service, arg):
    if service == "vnc":
        return True, arg


def audit(arg):
    ip, port = arg
    debug("[VNC] vnc://%s:%d", ip, port)
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.settimeout(10)
        socket_obj.connect((ip, port))
        sock_read = socket_obj.recv(12)
        if sock_read[:3] == "RFB":
            ooo0OO, min = [int(II1) for II1 in sock_read[3:-1].split(".")]
            socket_obj.send("RFB 003.008\n")
            socket_obj.recv(2)
            socket_obj.send("\x01")
            if socket_obj.recv(4) == "\x00\x00\x00\x00":
                security_hole("vnc://%s:%d (Protocol:%d.%d)" % (ip, port, ooo0OO, min))
        socket_obj.close()
    except:
        pass


if __name__ == '__main__':
    from dummy import *

    audit(assign("vnc", ("128.199.254.244", 5901))[1])

    # KEY---d289da3e7b9c736756e3429c23db20228f8e3547d3a4b540da1f86aaf22ff02f---
