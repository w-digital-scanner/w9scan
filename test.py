# coding:utf-8

time = 154.629854404
print round(time,2)
print round(time/60,2)

def runningTime(time):
    sTime = round(time,2)
    mTime = round(time/60,2)
    timeStr = "%s min / %s seconds"%(str(mTime),str(sTime))
    return timeStr

print runningTime(time)