import os
foder = r'C:\Users\boyhack\Desktop\w9scan\plugins'

filter_func = lambda file: (True, False)['__init__' in file or 'pyc' in file]
def getExp():
    direxp = []
    for dirpath, dirnames, filenames in os.walk(foder):
        for filename in filenames:
            direxp.append(os.path.join(dirpath,filename))
    return direxp
for exp in getExp():
    print exp
#dir_exploit = filter(filter_func,getExp())
#print dir_exploit
