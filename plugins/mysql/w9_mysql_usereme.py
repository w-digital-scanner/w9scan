# Embedded file name: mysql_user_enum.py
import socket
import sys


def assign(service, arg=None):
    if service == "mysql":
        return True, arg


def work_fun(arg):
    ip, port, thread_work, reData = arg
    socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socketObj.settimeout(8)
        socketObj.connect((ip, port))
        read = socketObj.recv(1024)
        Oo = "\x00\x00\x01\x8d\x00\x00\x00\x00" + thread_work + "\x00\x50\x4e\x5f\x51\x55\x45\x4d\x45\x00";
        socketObj.send(chr(len(Oo) - 3) + Oo)
        read = socketObj.recv(1024)
        socketObj.close()
        if read.find("upgrading") != -1 and read[7:13] != "Access":
            reData.append(thread_work)
    except Exception as e:
        print e
        pass

    socketObj.close()


def audit(arg):
    ip, port = arg
    works = []
    thread = ThreadPool(10,work_fun)
    work_list = util.load_password_dict(ip, "database/mysql_user.txt", None)
    for work in work_list:
        if work[0] not in works:
            works.append(work[0])

    reData = []
    for thread_work in works:
        thread.push(work_fun, (ip, port, thread_work, reData))

    thread.run()
    if reData:
        security_note(",".join(reData))


if __name__ == '__main__':

    audit(assign("mysql", ("127.0.0.1", 3306))[1])

    # KEY---8c97d8c12ebb049684db59720d39ad8b38b0081d8cc8d022bd7768ab0bc7c699---
