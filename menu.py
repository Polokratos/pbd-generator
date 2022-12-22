import random
import datetime
from heplers import formatDate

#W BD nie mamy żadnego warunku na to że połowa menu się zmienia co 2 tyg XD.
# Na wszelki tutaj tego dopilnowałem.

def menu(twoweeksAmt:int, start:datetime.date, productAmt:int): # -> (list[list],list[list],list[list])
    
    productsShuffled = [i for i in range(productAmt)]
    random.shuffle(productsShuffled)
    productsConstant = productsShuffled[0::4]
    predicate = lambda int: True if int in productsConstant else False
    productsVariable = productsShuffled
    filter(predicate,productsVariable)
    
    retval = []
    date = start
    index = 1
    for i in range(twoweeksAmt):
        menu = twoweekMenu(index,date,productsConstant,productsVariable)
        for i in menu[0]:
            retval.append(i)
        date = date + datetime.timedelta(weeks=2)
        index = menu[1]
    return retval

def twoweekMenu(startindex: int, startdate:datetime.date,pc:list[int],pv:list[int]):
    retval = []
    cindex = startindex
    enddate = startdate+datetime.timedelta(weeks=2)
    for i in range(len(pc)):
        retval.append([
            cindex, #ID
            pc[i], #ProductID
            formatDate(startdate), #StartDate
            formatDate(enddate), #EndDate
            random.randint(5,25)+random.randint(0,25) #UnitPrice
        ])
        cindex+=1
    pv_shuffledcopy = [i for i in pv[::2]] #Half of productsVariable in stock every time.
    random.shuffle(pv_shuffledcopy)
    for i in range(len(pv_shuffledcopy)):
        retval.append([
            cindex, #ID
            pv_shuffledcopy[i], #ProductID
            str(startdate.year) +'-'+str(startdate.month)+'-'+str(startdate.day), #StartDate
            str(enddate.year) +'-'+str(enddate.month)+'-'+str(enddate.day), #EndDate
            random.randint(5,25)+random.randint(0,25) #UnitPrice
        ])
        cindex+=1
    return (retval,cindex)
    
    
    
