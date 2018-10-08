# Embedded file name: telnet_crack.py
import sys
import telnetlib
import Queue


def o0OO00(host, port, user, pwd):
    oo = False
    for i1iII1IiiIiI1 in range(10):
        iIiiiI1IiI1I1 = False
        try:
            print("[+%02d] telnet://%s:%s@%s:%d/", i1iII1IiiIiI1, user, pwd, host, port)
            o0OoOoOO00 = telnetlib.Telnet(host, port, timeout=10)
            o0OoOoOO00.expect(["login:", "Username"], 5)
            o0OoOoOO00.write(user + "\n")
            o0OoOoOO00.expect(["Password:"], 5)
            o0OoOoOO00.write(pwd + "\n")
            I11i, O0O, O0O = o0OoOoOO00.expect(["\$", "\x5c\x3e", "\#"], 5)
            o0OoOoOO00.close()
            if I11i != -1:
                oo = True
        except Exception as Oo:
            iIiiiI1IiI1I1 = True
        else:
            pass
        finally:
            if not iIiiiI1IiI1I1:
                return oo

    return


def Ii1IIii11(arg):
    Oooo0000, i11, I11, Oo0o0000o0o0, oOo0oooo00o, oO0o0o0ooO0oO = arg
    try:
        oo = o0OO00(i11, I11, Oo0o0000o0o0, oOo0oooo00o)
        if oo:
            oo0o0O00 = {}
            oo0o0O00["username"] = Oo0o0000o0o0
            oo0o0O00["password"] = oOo0oooo00o or "<empty>"
            oO0o0o0ooO0oO.put(oo0o0O00)
            Oooo0000.stop()
        if oo == None:
            Oooo0000.stop()
    except Exception as Oo:
        pass


def assign(service, arg=None):
    if service == '''telnet''':
        return (True, arg)


def audit(arg):
    i11, I11 = arg
    oo0o0O00 = {}
    if o0OO00(i11, I11, "neverusedusername", "neverusedpassword") == None:
        return
    Oooo0000 = ThreadPool(8,Ii1IIii11)
    iI11 = util.load_password_dict(i11, "database/telnet_user.txt", "database/telnet_pass.txt")
    oO0o0o0ooO0oO = Queue.Queue()
    for iII111ii in iI11:
        Oooo0000.push( (Oooo0000,
                                  i11,
                                  I11,
                                  iII111ii[0],
                                  iII111ii[1],
                                  oO0o0o0ooO0oO))

    Oooo0000.run()
    if not oO0o0o0ooO0oO.empty():
        oo0o0O00 = oO0o0o0ooO0oO.get()
        security_hole("%s:%d telnet password is %s/%s" % (i11,
                                                          I11,
                                                          oo0o0O00["username"],
                                                          oo0o0O00["password"]))


if __name__ == '__main__':
    from dummy import *
    import threadpool

    audit(assign('''telnet''', ("192.168.0.201", 23))[1])

    # KEY---e034570d4d73b2deeed98ff76911c89ff03ae6f0cef61a09f4091b55783c18b2---
