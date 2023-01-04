import random
import datetime
import heplers

#Zwraca amt1 zniżek typu Z1 i amt2 zniżek typu Z2, zaczynajace sie od startDate.
def discountVars(amt1: int, amt2:int, startDate: datetime.date):
    retval = []
    
    cdate = startDate
    index = 1
    for _ in range(amt1):
        edate = cdate+datetime.timedelta(days=random.randint(0,25))
        retval.append([
            index, #VarID
            1, #DiscountID (Z1)
            "Z1", #VarName
            random.randint(0,10), #Value
            heplers.formatDate(cdate), #StartDate
            heplers.formatDate(edate) #EndDate
        ]);index+=1
        cdate = edate
    cdate = startDate
    for _ in range(amt2):
        edate = cdate+datetime.timedelta(days=random.randint(0,25))
        retval.append([
            index, #VarID
            2, #DiscountID (Z1)
            "Z2", #VarName
            random.randint(0,10), #Value
            heplers.formatDate(cdate), #StartDate
            heplers.formatDate(edate) #EndDate
        ]);index+=1
        cdate = edate
    return retval