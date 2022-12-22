import random
def tables(amt:int) -> list[list]:
    retval = []
    for i in range(amt):
        retval.append([
            i+1, #TableID
            random.randint(0,2) + random.randint(1,4) # seats
        ])