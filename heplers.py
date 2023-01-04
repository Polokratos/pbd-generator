import datetime
import random

def formatDate(tf:datetime)->str:
    return str(tf)

def formatDateTime(tf:datetime)->str:
    return str(tf)

def getUniqueRandomElements(list:list,amt:int)->list:
    retval = []
    while(len(retval)<amt):
        ta = list[random.randint(0,len(list)-1)]
        if(ta not in retval):
            retval.append(ta)
    return retval