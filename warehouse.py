import random

def warehouse(amt:int) -> list[list]:
    retval = []
    for i in range (amt):
        retval.append([
            i+1, #ProductID
            "produkt"+str(i+1), #ProductName
            "opis"+str(i+1), #Description
            random.randint(1,100), #Quantity
            True if random.randint(1,10) == 10 else False #isSeafood
            ]) 
    return retval