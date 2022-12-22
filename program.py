from clients    import *
from menu       import *
from tables     import  *
from warehouse  import  *
from globals    import *

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

#Replace 0 with the amount of needed records.
(Clients,Client_Individuals,Companies) = clients(0)
Tables = tables(0)
Warehouse = warehouse(0)
Menu = menu(0,datetime.today(),len(Warehouse))
Globals = globals(0,datetime.today())
