# coding:utf-8

List=[1,2,2,2,2,3,3,3,4,4,4,4]
a = {}
for i in List:
    if List.count(i)>1:
        a[i] = List.count(i)
print (a)