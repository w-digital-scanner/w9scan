# Embedded file name: compressed_file.py
import urlparse
import re


def assign(service, arg):
    if service != "www":
        return

    url_info = urlparse.urlparse(arg)
    url_paths = url_info.path.split("/")
    path_num = len(url_paths)
    url_list = []

    if path_num < 3:
        return True, "%s://%s/" % (url_info.scheme, url_info.netloc)

    else:
        for path_n in range(1, path_num - 1):
            path_x = "/".join(url_paths[1:path_n + 1])
            new_url = "%s://%s/%s/" % (url_info.scheme, url_info.netloc, path_x)

            if "." not in path_x:
                url_list.append(new_url)
            if path_n == 2:
                break

        return True, url_list


def isMatch(http_code, head):
    if http_code == 200 and re.search("Content\-Type:[^\r\n]*application[^\r\n]*(zip|compress|stream)", head,
                                      re.M | re.I):

        regex_ = re.search("Content\-Length:\s*(\d+)", head, re.M | re.I)
        if regex_ and int(regex_.group(1)) > 10:
            return True

    return False


def getCompressed(url_dir, name):
    if url_dir.startswith("/") is False:
        url_dir += "/"

    url = "%snoexists.zip" % url_dir

    status_code, header, body, errcode, _ = curl.curl("-I --retry 3 " + url)

    if isMatch(status_code, header):
        return False

    postfix_list = ["rar", "zip", "7z", "tar.gz", "tar", "bz2", "gz", "mdb"]

    for postfix in postfix_list:
        url = "%s%s.%s" % (url_dir, name, postfix)

        status_code, header, body, errcode, _ = curl.curl("-I --retry 3 " + url)

        debug("[%d] %s", status_code, url)

        if isMatch(status_code, header):
            security_warning(url)
            return True

    return False


def audit(arg):
    url_info = arg
    url_host = util.get_url_host(url_info)

    if re.match("^\w+://[\w\-\.]+/$", url_info):

        path_name_list = ["wwwroot", "htdocs", "site", "www", "default", "web",
                          url_host, url_host.replace(".", ""), url_host.replace(".", "_")]

        host_name = util.get_domain_root(url_host)

        path_name_list.append(host_name)
        path_name_list.append(host_name.replace(".", ""))
        path_name_list.append(host_name.replace(".", "_"))

        if host_name != url_host:
            name_n = url_host.replace("." + host_name, "").split(".")
            path_name_list += name_n

        path_name_list.append(host_name.split(".")[0])

        for name_n in set(path_name_list):
            if getCompressed(url_info, name_n):
                break

    else:
        regex_ = re.match("^(\w+://.*/)([^/]+)/", url_info)

        if regex_:
            if not getCompressed(url_info, regex_.group(2)):
                getCompressed(regex_.group(1), regex_.group(2))


if __name__ == '__main__':
    from dummy import *

    url_list = ["http://www.360doc.com/a/b/c/d/"]
    for url in url_list:
        server_n = assign("www", url)[1]
        if isinstance(server_n, list):
            for url_n in server_n:
                audit(url_n)

        elif server_n:
            audit(server_n)

            # KEY---3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673---
