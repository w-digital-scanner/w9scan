#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.core.exception import ToolkitMissingPrivileges
from lib.core.data import urlconfig
from lib.core.data import paths,logger
from lib.core.common import runningTime
import time,base64,os
from lib.utils.until import get_domain_root
import cgi
from lib.core.settings import VERSION

class CollectData(object):
    def __init__(self):
        self.dict = dict()

    def add_list(self,k,v):
        if k == '':
            k = str(len(self.dict))
        if k not in self.dict:
            self.dict.setdefault(k,list())
        self.dict[k].append(v)
    
    def add_set(self,k,v):
        if k == '':
            k = str(len(self.dict))
        if k not in self.dict:
            self.dict.setdefault(k,set())
        self.dict[k].add(v)
            
    def getData(self):
        return self.dict

class buildHtml(object):

    def __init__(self):
        self.dict = dict()

    def add_list(self,level,value,k = '',domain = ''):
        if domain not in self.dict:
            self.dict[domain] = dict()
            self.dict[domain]["info"] = CollectData()
            self.dict[domain]["note"] = CollectData()
            self.dict[domain]["warning"] = CollectData()
            self.dict[domain]["hole"] = CollectData()

        if level not in self.dict[domain]:
            raise ToolkitMissingPrivileges("Building error:level not in dict")

        self.dict[domain][level].add_list(k,value)

    def add_set(self,level,value,k = '',domain = ''):
        if domain not in self.dict:
            self.dict[domain] = dict()
            self.dict[domain]["info"] = CollectData()
            self.dict[domain]["note"] = CollectData()
            self.dict[domain]["warning"] = CollectData()
            self.dict[domain]["hole"] = CollectData()
        if level not in self.dict[domain]:
            raise ToolkitMissingPrivileges("Building error:level not in dict")
        self.dict[domain][level].add_set(k,value)
    
    def escape(self,html):
        html = str(html)
        html = cgi.escape(html)
        return html

    def addbug(self,vultype, title, content):
        html = """
        <div class="media">
            <div class="media-left">
              <a href="#">
              <i class="fa fa-circle m-l-5 text-%s"></i>
              </a>
            </div>
            <div class="media-body">
              <h4 class="media-heading">%s</h4>
              %s
            </div>
       </div>
        """ % (vultype, title, content)
        return html
    
    def addmutibug(self,title,content):
        return "%s:%s[/br]"%(title,content)

    def mutiBuild(self):
        # build base info
        versionPlace = VERSION
        reportTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        selectPlugin = ' '.join(urlconfig.diyPlugin)
        w9scan_html = "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KICAgIDxtZXRhIGh0dHAtZXF1aXY9IlgtVUEtQ29tcGF0aWJsZSIgY29udGVudD0iSUU9ZWRnZSI+CiAgICA8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEiPgoKICAgIDx0aXRsZT53OXNjYW4g5om56YeP5ryP5rSe5omr5o+P5oql5ZGKPC90aXRsZT4KCiAgICA8bWV0YSBuYW1lPSJkZXNjcmlwdGlvbiIgY29udGVudD0iU291cmNlIGNvZGUgZ2VuZXJhdGVkIHVzaW5nIGxheW91dGl0LmNvbSI+CiAgICA8bWV0YSBuYW1lPSJhdXRob3IiIGNvbnRlbnQ9IkxheW91dEl0ISI+CgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwOi8vY2RuLmJvb3Rjc3MuY29tL2Jvb3RzdHJhcC8zLjMuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiPiAKICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cDovL2Nkbi5ib290Y3NzLmNvbS9mb250LWF3ZXNvbWUvNC4yLjAvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIj4gCgogIDwvaGVhZD4KICA8Ym9keT4KCiAgICA8ZGl2IGNsYXNzPSJjb250YWluZXItZmx1aWQiPgoJPGRpdiBjbGFzcz0icm93Ij4KCQk8ZGl2IGNsYXNzPSJjb2wtbWQtMTIiPgoJCQk8ZGl2IGNsYXNzPSJwYWdlLWhlYWRlciI+CgkJCQk8aDE+CgkJCQkJdzlzY2Fu5om56YeP5omr5o+P5oql5ZGKICA8c21hbGw+dnt7dmVyc2lvbn19PC9zbWFsbD4KCQkJCTwvaDE+CgkJCTwvZGl2PiA8c3BhbiBjbGFzcz0ibGFiZWwgbGFiZWwtcHJpbWFyeSI+55Sf5oiQ5pe26Ze077yae3tyZXBvcnRUaW1lfX08L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsYWJlbCBsYWJlbC1zdWNjZXNzIj7pgInmi6nmj5Lku7bvvJp7e3NlbGVjdFBsdWdpbn19PC9zcGFuPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGFiZWwgbGFiZWwtZGFuZ2VyIj5TY2FuIHRpbWUJe3tzY2FudGltZX19PC9zcGFuPgogICAgICAgICAgICA8L2JyPjwvYnI+CgkJCTx0YWJsZSBjbGFzcz0idGFibGUiPgoJCQkJPHRoZWFkPgoJCQkJCTx0cj4KICAgIDx0aD4jPC90aD4KICAgIDx0aD5Vcmw8L3RoPgogICAgPHRoPlRpdGxlPC90aD4KICAgIDx0aD5CdWlsZHdpdGg8L3RoPgogICAgPHRoPkluZm88L3RoPgogICAgPHRoPk5vdGU8L3RoPgogICAgPHRoPldhcm5pbmc8L3RoPgogICAgPHRoPkhvbGU8L3RoPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90cj4KCQkJCTwvdGhlYWQ+CiAgICAgICAgICAgICAgICAKCQkJCTx0Ym9keT4KICAgICAgICAgICAgICAgICAgICB7e2NvbnRlbnR9fQoJCQkJPC90Ym9keT4KCQkJPC90YWJsZT4KCQk8L2Rpdj4KCTwvZGl2Pgo8L2Rpdj4KICA8L2JvZHk+CjwvaHRtbD4="

        w9scan_html = base64.b64decode(w9scan_html)
        w9scan_html = w9scan_html.replace("{{version}}", str(versionPlace))
        w9scan_html = w9scan_html.replace("{{reportTime}}", str(reportTime))
        w9scan_html = w9scan_html.replace("{{scantime}}",runningTime(urlconfig.runningTime) )
        w9scan_html = w9scan_html.replace("{{selectPlugin}}", str(selectPlugin))

        htmlDict = dict()
        index = 0
        full = []
        try:
            for url, content in self.dict.items():
                htmlDict[url] = dict()
                index = index + 1
                Total = dict()

                title = ""
                server = ""

                for key, value in content.items():
                    htmlDict[url][key] = value.getData()

                    if len(htmlDict[url][key]):
                        infoList = list()
                        if key == "info":
                            if "title" in htmlDict[url][key]:
                                title = htmlDict[url][key]["title"]
                                if isinstance(title, list):
                                    title = ''.join(title)
                                htmlDict[url][key].pop("title")
                            if "WebStruct" in htmlDict[url][key]:
                                server = htmlDict[url][key]["WebStruct"]
                                htmlDict[url][key].pop("WebStruct")
                            
                        for k, v in htmlDict[url][key].items():
                            f = v
                            if isinstance(v, list):
                                f = '[/br]'.join(v)
                            elif isinstance(v, set):
                                f = '[/br]'.join([i for i in f])
                            f = self.escape(f).replace('[/br]', '</br>')
                            infoList.append(self.addmutibug(str(k), str(f)))
                        info_page = ''.join(infoList)
                    else:
                        info_page = ""
                    Total[key] = info_page.replace('[/br]', '</br>')
                
                tr = "<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>  %s</td><td>%s</td><td>%s</td></tr>"%(index,url,title,server,Total["info"],Total["note"],Total["warning"],Total["hole"])
                full.append(tr)
        except Exception as err:
            raise ToolkitMissingPrivileges("Building result faild!")

        w9scan_html = w9scan_html.replace("{{content}}", ' '.join(full))
        filename = os.path.join(paths.w9scan_Output_Path, "BatchScanning" + "_" + str(int(time.time())) + ".html")
        result = open(filename, "w")
        result.write(w9scan_html)
        result.close()
        logger.info("success saved :" + filename)


    def build(self):
        # build base info
        reportTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        # build scan info
        htmlDict = dict()
        Total = {"hole":'0',"note":'0',"warning":'0',"info":'0'}

        # build
        DomainRoot = get_domain_root(''.join(urlconfig.url))
        w9scan_html = "PCFET0NUWVBFIGh0bWw+CjwhLS1baWYgSUUgOF0+PGh0bWwgY2xhc3M9ImllIGllOCI+IDwhW2VuZGlmXS0tPgo8IS0tW2lmIElFIDldPjxodG1sIGNsYXNzPSJpZSBpZTkiPiA8IVtlbmRpZl0tLT4KPCEtLVtpZiBndCBJRSA5XT48IS0tPgo8aHRtbD4gPCEtLTwhW2VuZGlmXS0tPgo8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KICAgIDxtZXRhIGh0dHAtZXF1aXY9IlgtVUEtQ29tcGF0aWJsZSIgY29udGVudD0iSUU9ZWRnZSI+CiAgICA8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEiPgogICAgPG1ldGEgbmFtZT0iZGVzY3JpcHRpb24iIGNvbnRlbnQ9IkNvYnJhIGlzIGEgY29kZSBzdGF0aWMgc2NhbiBzeXN0ZW0iPgogICAgPG1ldGEgbmFtZT0iYXV0aG9yIiBjb250ZW50PSJGZWVpIDxmZWVpQGZlZWkuY24+Ij4KICAgIDx0aXRsZT53OXNjYW4gc2VjdXJpdHkgcmVwb3J0PC90aXRsZT4KCiAgICA8IS0tIEZhdmljb24tLT4KICAgIDxsaW5rIHJlbD0ic2hvcnRjdXQgaWNvbiIgaHJlZj0iLi9hc3NldC9pY28vZmF2aWNvbi5pY28iIHR5cGU9ImltYWdlL3gtaWNvbiI+CiAgICAKICAgIDxsaW5rIGhyZWY9Imh0dHBzOi8vY2RuLmJvb3Rjc3MuY29tL2ZvbnQtYXdlc29tZS80LjcuMC9jc3MvZm9udC1hd2Vzb21lLm1pbi5jc3MiIHJlbD0ic3R5bGVzaGVldCI+CiAgICA8IS0tIENTUyAtLT4KICAgIDxsaW5rIGhyZWY9Imh0dHBzOi8vYnVncy5oYWNraW5nOC5jb20vY2RuL2Fzc2V0L2Nzcy9iYXNlLmNzcyIgcmVsPSJzdHlsZXNoZWV0Ij4KICAgIDxsaW5rIGhyZWY9Imh0dHBzOi8vYnVncy5oYWNraW5nOC5jb20vY2RuL2Fzc2V0L2Nzcy9yZXBvcnQuY3NzIiByZWw9InN0eWxlc2hlZXQiPgoKICAgIDwhLS1baWYgbHQgSUUgOV0+CiAgICAgIDxzY3JpcHQgc3JjPSJqcy9odG1sNXNoaXYubWluLmpzIj48L3NjcmlwdD4KICAgICAgPHNjcmlwdCBzcmM9ImpzL3Jlc3BvbmQubWluLmpzIj48L3NjcmlwdD4KICAgIDwhW2VuZGlmXS0tPgoKPC9oZWFkPgo8Ym9keT4KPGRpdiBjbGFzcz0iY29udGFpbmVyLWZsdWlkIj4KICAgIDxkaXYgY2xhc3M9InJvdyI+CiAgICAgICAgPGRpdiBjbGFzcz0iY29sLXhzLTEyIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0iaW52b2ljZS10aXRsZSI+CiAgICAgICAgICAgICAgICA8aDI+dzlzY2FuPC9oMj4KICAgICAgICAgICAgICAgIDxoMyBjbGFzcz0icHVsbC1yaWdodCI+PC9oMz4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDxocj4KICAgICAgICAgICAgPHVsIGNsYXNzPSJuYXYgbmF2LXRhYnMiIGlkPSJteVRhYnMiPgogICAgICAgICAgICAgICAgPGxpIGNsYXNzPSJhY3RpdmUiPjxhIGRhdGEtaWQ9ImluZiIgZGF0YS10b2dnbGU9InRhYiI+SW5mb3JtYXRpb248L2E+PC9saT4KICAgICAgICAgICAgPC91bD4KICAgICAgICAgICAgPGRpdiBjbGFzcz0idGFiLWNvbnRlbnQiPgogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0idGFiLXBhbmUgYWN0aXZlIiBpZD0iaW5mIj4KICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJyb3ciPgogICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJjb2wtbWQtNCBjb2x1bW4iPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGg0PldlbGNvbWUgdG8gdzlzY2FuITwvaDQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJyb3ciPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNvbC14cy0xMiI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxhZGRyZXNzPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGg1PlByb2plY3QgaW5mb3JtYXRpb248L2g1PgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRhYmxlIGNsYXNzPSJ0YWJsZSB0YWJsZS1zdHJpcGVkIHRhYmxlLWJvcmRlcmVkIHRhYmxlLWNvbmRlbnNlZCI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRoZWFkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0cj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRoPkl0ZW08L3RoPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGg+VmFsdWU8L3RoPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90aGVhZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGJvZHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGQ+RG9tYWluPC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkPnt7dXJsfX08L3RkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGQ+U2VsZWN0IHBsdWdpbjwvdGQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD57e3NlbGVjdF9wbHVnaW59fTwvdGQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90cj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD5zY2FuIGFsbCBwb3J0PC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkPnt7c2Nhbl9hbGxfcG9ydH19PC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0cj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkPlRocmVhZE51bTwvdGQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD57e1RocmVhZE51bX19PC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdGJvZHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RhYmxlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2FkZHJlc3M+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iY29sLXhzLTEyIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGFkZHJlc3M+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aDU+U2NhbiBpbmZvcm1hdGlvbjwvaDU+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGFibGUgY2xhc3M9InRhYmxlIHRhYmxlLXN0cmlwZWQgdGFibGUtYm9yZGVyZWQgdGFibGUtY29uZGVuc2VkIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGhlYWQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGg+SXRlbTwvdGg+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0aD5WYWx1ZTwvdGg+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90cj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RoZWFkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0Ym9keT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD5SZXBvcnQgdGltZTwvdGQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD57e3JlcG9ydFRpbWV9fTwvdGQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90cj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD5TY2FuIHRpbWU8L3RkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGQ+e3tzY2FudGltZX19PC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdGJvZHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RhYmxlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2FkZHJlc3M+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iY29sLXhzLTEyIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGFkZHJlc3M+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aDU+TnVtYmVyIG9mIHZ1bG5lcmFiaWxpdGllczwvaDU+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGFibGUgY2xhc3M9InRhYmxlIHRhYmxlLXN0cmlwZWQgdGFibGUtYm9yZGVyZWQgdGFibGUtY29uZGVuc2VkIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGhlYWQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGg+TGV2ZWw8L3RoPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGg+VG90YWw8L3RoPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90aGVhZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGJvZHkgY2xhc3M9Im4tby12Ij4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD5Ib2xlPC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkPnt7dG90YWxfSG9sZX19PC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0cj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkPk5vdGU8L3RkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGQ+e3t0b3RhbF9Ob3RlfX08L3RkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dGQ+V2FybmluZzwvdGQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD57e3RvdGFsX1dhcm5pbmd9fTwvdGQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90cj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0ZD5JbmZvPC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkPnt7dG90YWxfSW5mb319PC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdGJvZHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RhYmxlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2FkZHJlc3M+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNvbC1tZC04IGNvbHVtbiI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aDQ+VnVsbmVyYWJpbGl0eSBzdGF0aXN0aWNzPC9oND4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJicy1leGFtcGxlIiBkYXRhLWV4YW1wbGUtaWQ9Im1lZGlhLWxpc3QiPgogICAgPHVsIGNsYXNzPSJtZWRpYS1saXN0Ij4KICAgICAgPGxpIGNsYXNzPSJtZWRpYSI+CiAgICAgICAgPGRpdiBjbGFzcz0ibWVkaWEtbGVmdCI+CiAgICAgICAgICA8YSBocmVmPSIjIj4KICAgICAgICAgICAgPGkgY2xhc3M9ImZhIGZhLWNpcmNsZSBtLWwtNSB0ZXh0LXB1cnBsZSI+PC9pPgogICAgICAgICAgPC9hPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9Im1lZGlhLWJvZHkiPgogICAgICAgICAgPGg0IGNsYXNzPSJtZWRpYS1oZWFkaW5nIj5SZXBvcnQgTGV2ZWw8L2g0PgogICAgICAgICAgPHA+dzlzY2Fu5omr5o+P5oql5ZGK562J57qn5oyJ54Wn5Lil6YeN5oCn5YiG5Li65Zub57qnIGluZm8gbm90ZSB3YXJuaW5nIGhvbGUuPC9wPgogICAgICAgICAgPCEtLSBOZXN0ZWQgbWVkaWEgb2JqZWN0IC0tPgogICAgICAgICAgPGRpdiBjbGFzcz0ibWVkaWEiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJtZWRpYS1sZWZ0Ij4KICAgICAgICAgICAgICA8YSBocmVmPSIjIj4KICAgICAgICAgICAgICA8aSBjbGFzcz0iZmEgZmEtY2lyY2xlIG0tbC01IHRleHQtaW5mbyI+PC9pPgogICAgICAgICAgICAgIDwvYT4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9Im1lZGlhLWJvZHkiPgogICAgICAgICAgICAgIDxoNCBjbGFzcz0ibWVkaWEtaGVhZGluZyI+SW5mbyBsZXZlbDwvaDQ+CiAgICAgICAgICAgICAgSW5mbyBsZXZlbCDmkJzpm4bnvZHnq5nnmoTkuIDkupvln7rmnKwuCiAgICAgICAgICAgICAgPCEtLSBOZXN0ZWQgbWVkaWEgb2JqZWN0IC0tPgogICAgICAgICAgICAgIHt7aW5mb19jb250ZW50fX0KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDwhLS0gTmVzdGVkIG1lZGlhIG9iamVjdCAtLT4KICAgICAgICAgIDxkaXYgY2xhc3M9Im1lZGlhIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibWVkaWEtbGVmdCI+CiAgICAgICAgICAgICAgPGEgaHJlZj0iIyI+CiAgICAgICAgICAgICAgICA8aSBjbGFzcz0iZmEgZmEtY2lyY2xlIG0tbC01IHRleHQtc3VjY2VzcyI+PC9pPgogICAgICAgICAgICAgIDwvYT4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9Im1lZGlhLWJvZHkiPgogICAgICAgICAgICAgIDxoNCBjbGFzcz0ibWVkaWEtaGVhZGluZyI+Tm90ZSBsZXZlbDwvaDQ+CiAgICAgICAgICAgICAgTm90ZSBsZXZlbCDmj5DphpLnvZHnq5nnmoTkuIDkupvkv6Hmga/lj6/og73ooqvms4TpnLIuCiAgICAgICAgICAgICAge3tub3RlX2NvbnRlbnR9fQogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPCEtLSBOZXN0ZWQgbWVkaWEgb2JqZWN0IC0tPgogICAgICAgICAgPGRpdiBjbGFzcz0ibWVkaWEiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJtZWRpYS1sZWZ0Ij4KICAgICAgICAgICAgICA8YSBocmVmPSIjIj4KICAgICAgICAgICAgICAgIDxpIGNsYXNzPSJmYSBmYS1jaXJjbGUgbS1sLTUgdGV4dC13YXJuaW5nIj48L2k+CiAgICAgICAgICAgICAgPC9hPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibWVkaWEtYm9keSI+CiAgICAgICAgICAgICAgPGg0IGNsYXNzPSJtZWRpYS1oZWFkaW5nIj5XYXJuaW5nIGxldmVsPC9oND4KICAgICAgICAgICAgICBXYXJuaW5nIGxldmVsIOitpuWRiue9keermeafkOS6m+WcsOaWueWPr+iDveiiq+WIqeeUqC4KICAgICAgICAgICAgICB7e3dhcm5pbmdfY29udGVudH19CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8IS0tIE5lc3RlZCBtZWRpYSBvYmplY3QgLS0+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJtZWRpYSI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9Im1lZGlhLWxlZnQiPgogICAgICAgICAgICAgIDxhIGhyZWY9IiMiPgogICAgICAgICAgICAgICAgPGkgY2xhc3M9ImZhIGZhLWNpcmNsZSBtLWwtNSB0ZXh0LWhvbGUiPjwvaT4KICAgICAgICAgICAgICA8L2E+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJtZWRpYS1ib2R5Ij4KICAgICAgICAgICAgICA8aDQgY2xhc3M9Im1lZGlhLWhlYWRpbmciPkhvbGUgbGV2ZWw8L2g0PgogICAgICAgICAgICAgIEhvbGUgbGV2ZWwg6auY5Y2x562J57qnIOitpuWRiue9keermeafkOS6m+WcsOaWueWPr+iDveWtmOWcqOS4pemHjeeahOWuieWFqOmXrumimC4KICAgICAgICAgICAgICB7e2hvbGVfY29udGVudH19CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvbGk+CiAgICA8L3VsPgogICAgCiAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgICAgIDwvZGl2PjwhLS0gRW5kIHJvdyAtLT4KICAgICAgICAgICAgICAgIDwvZGl2PjwhLS0gRW5kIHJhYiAtLT4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KICAgIDxocj4KICAgIDwhLS0gQ29udGFpbmVycyAtLT4KICAgIDxkaXYgY2xhc3M9InJvdyI+CiAgICAgICAgPGRpdiBjbGFzcz0iY29sLW1kLTYiPgogICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgPHAgc3R5bGU9ImZsb2F0OmxlZnQ7Ij4KICAgICAgICAgICAgICAgICAgICBDb3B5cmlnaHQgJmNvcHk7IDIwMTggPGEgaHJlZj0iaHR0cHM6Ly9naXRodWIuY29tL2JveS1oYWNrL3c5c2NhbiIgdGFyZ2V0PSJfYmxhbmsiPnc5c2NhbjwvYT4uIEFsbCByaWdodHMgcmVzZXJ2ZWQKICAgICAgICAgICAgICAgIDwvcD4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0iY29sLW1kLTYiPgogICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgPHAgc3R5bGU9ImZsb2F0OnJpZ2h0OyI+CiAgICAgICAgICAgICAgICAgICAgPGEgaHJlZj0iaHR0cHM6Ly9naXRodWIuY29tL2JveS1oYWNrL3c5c2NhbiIgdGFyZ2V0PSJfYmxhbmsiPkdpdGh1YjwvYT4gLQogICAgICAgICAgICAgICAgICAgIDxhIGhyZWY9Imh0dHBzOi8vZ2l0aHViLmNvbS9ib3ktaGFjay93OXNjYW4iIHRhcmdldD0iX2JsYW5rIj53OXNjYW48L2E+CiAgICAgICAgICAgICAgICA8L3A+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgPC9kaXY+CjwvZGl2Pgo8L2JvZHk+CjwvaHRtbD4="
        try:
            w9scan_html = base64.b64decode(w9scan_html)
            w9scan_html = w9scan_html.replace("{{url}}", str(urlconfig.url))
            w9scan_html = w9scan_html.replace("{{scan_all_port}}", str(urlconfig.scanport))
            w9scan_html = w9scan_html.replace("{{ThreadNum}}", str(urlconfig.threadNum))
            w9scan_html = w9scan_html.replace("{{select_plugin}}", str(' '.join(urlconfig.diyPlugin)))
            w9scan_html = w9scan_html.replace("{{reportTime}}", str(reportTime))
            w9scan_html = w9scan_html.replace("{{scantime}}",runningTime(urlconfig.runningTime) )
        except Exception:
            raise ToolkitMissingPrivileges("BuildHtml Error Exception")

        try:
            for url,content in self.dict.items():
                htmlDict[url] = dict()
                for key,value in content.items():
                    try:
                        htmlDict[url][key] = value.getData()
                        if len(htmlDict[url][key]):
                            infoList = list()
                            for k,v in htmlDict[url][key].items():
                                f = v
                                if isinstance(v, list):
                                    f = '[/br]'.join(v)
                                elif isinstance(v,set):
                                    f = '[/br]'.join([i for i in f])
                                f = self.escape(f).replace('[/br]','</br>')
                                infoList.append(self.addbug(key,str(k),str(f)))
                            info_page = ''.join(infoList)
                            substr = "{{%s_content}}"%key
                            w9scan_html = w9scan_html.replace(substr,info_page)
                        else:
                            substr = "{{%s_content}}"%key
                            w9scan_html = w9scan_html.replace(substr,'')

                        Total[key] = str(len(value.getData()))
                    except Exception:
                        raise ToolkitMissingPrivileges("Save Report Exception")

            w9scan_html = w9scan_html.replace("{{total_Hole}}", Total["hole"])
            w9scan_html = w9scan_html.replace("{{total_Note}}", Total["note"])
            w9scan_html = w9scan_html.replace("{{total_Warning}}", Total["warning"])
            w9scan_html = w9scan_html.replace("{{total_Info}}", Total["info"])


            filename = DomainRoot + "_" + str(int(time.time())) + ".html"
            filename.replace(":","_")
            filename = os.path.join(paths.w9scan_Output_Path,filename)
            result = open(filename, "w")
            result.write(w9scan_html)
            result.close()
            logger.info("success saved :" + filename)

        except Exception as err:
            raise ToolkitMissingPrivileges("Sava Faild! error:" + err)
    
    def getData(self):
        htmlDict = dict()
        for url,content in self.dict.items():
            htmlDict[url] = dict()
            for key,value in content.items():
                htmlDict[url][key] = value.getData()
        return str(htmlDict)