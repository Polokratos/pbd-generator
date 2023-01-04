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
        frec = formatRecord(records[i])
        retval += "INSERT INTO " + table + " VALUES " + str(frec)+';'
        retval += '\n'
    retval = retval.replace('[','(')
    retval = retval.replace(']',')')
    retval += "\n\n"
    return retval

def formatRecord(record:list[any]):
    formatted = []
    for i in record:
        if(i == True):
            formatted.append(1)
        elif(i==False):
            formatted.append(0)
        else:
            formatted.append(i)
    return formatted

#SANITY CHECK: Consistent, but random.
random.seed(420)

#Replace a 0 with the amount of needed records.
(Clients,Client_Individuals,Companies) = clients(30)
Tables = tables(10)
Warehouse = warehouse(15)
Menu = menu(20,datetime.today(),len(Warehouse))
Globals = globals(5,datetime.today())
(Reservation,ReservationDetails,ReservationClient,ReservationCompany) = reservation(3,10,140,datetime.today(),
                                               [i[0] for i in Client_Individuals],
                                               [i[0] for i in Companies],
                                               [i[0] for i in Tables])
Orders = orders(5,15,datetime.today(),140,Reservation,[i[0] for i in Client_Individuals])
OrderDetails = orderDetails([i[0] for i in Orders],[i[0] for i in Warehouse])

DiscountVars = discountVars(15,15,datetime.today())


printval = ""
printval += query("Clients",Clients)
printval += query("Client_Individuals", Client_Individuals)
printval += query("Companies",Companies)
printval += query("Tables",Tables)
printval += query("Warehouse",Warehouse)
printval += query("Menu",Menu)
printval += query("Reservation",Reservation)
printval += query("ReservationDetails",ReservationDetails)
printval += query("ReservationClient",ReservationClient)
printval += query("ReservationCompany",ReservationCompany)
printval += query("Orders",Orders)
printval += query("Order_Details",OrderDetails)
printval += query("Discount_Vars",DiscountVars)


with open("output.sql",'a') as file:
    file.write(printval)