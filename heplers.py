import datetime
import random

def formatDate(tf:datetime)->str:
    return str(tf.year) +'-'+str(tf.month)+'-'+str(tf.day)

def formatDateTime(tf:datetime)->str:
    return formatDate(tf)+' ' + tf.time.hour+':'+tf.time.minute+' '+tf.time.second

def getUniqueRandomElements(list:list,amt:int)->list:
    retval = []
    while(len(retval)<amt):
        ta = list[random.randint(0,len(list)-1)]
        if(ta not in retval):
            retval.append(ta)