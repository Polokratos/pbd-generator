from clients        import *
from menu           import *
from tables         import *
from warehouse      import *
from globals        import *
from reservation    import *
from orders         import *
from orderDetails   import *
from discountVars   import *

from datetime import datetime

#Change a list of records to list of SQL INSERT queries
def query(table:str, records:list[list[any]]):
    retval = ""
    for i in range(len(records)):
        retval += "INSERT INTO " + table + " VALUES " + str(records[i])+';'
        retval += '\n'
    retval = retval.replace('[','(')
    retval = retval.replace(']',')')
    return retval

#Replace a 0 with the amount of needed records.
(Clients,Client_Individuals,Companies) = clients(0)
Tables = tables(0)
Warehouse = warehouse(0)
Menu = menu(0,datetime.today(),len(Warehouse))
Globals = globals(0,datetime.today())
(Reservation,ReservationDetails) = reservation(10,20,0,datetime.today(),
                                               [i[0] for i in Client_Individuals],
                                               [i[0] for i in Companies],
                                               [i[0] for i in Tables])
Orders = orders(20,50,datetime.today(),0,Reservation,[i[0] for i in Client_Individuals])
OrderDetails = orderDetails([i[0] for i in Orders],[i[0] for i in Warehouse])

DiscountVars = discountVars(0,0,datetime.today())


