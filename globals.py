import random
import datetime
from heplers import formatDate

def globals(amt:int, start:datetime)->list[list]:
    retval = []
    curr = start
    for i in range(amt):
        end = curr + datetime.timedelta(weeks= random.randint(1,10))
        retval.append([
            i+1, #ID
            random.randint(0,10), #WZ
            random.randint(0,10), # WK
            formatDate(curr), #startDate
            formatDate(end) #endDate
        ])
        curr = end
    return retval