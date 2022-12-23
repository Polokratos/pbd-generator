import random
import heplers

# Może nikt nie będzie patrzeć na to że te dane są totalnie odklejone od Menu/DiscountVars/ etc.
# Jeżeli będzie trzeba to naprawiać to będę ździebko zirytowany.

#Ciche założenie że będziemy mieli już z 10 produktów minimum
def orderDetails(orderIDs:list[int],productID:list[int]):
    retval = []
    for o in orderIDs:
        amt = 1 if random.randint(0,100) < 90 else 2 #10% for 2 details/order. Can replace with better dist.
        products = heplers.getUniqueRandomElements(productID,amt)
        for p in products:
            retval.append([
                o, #OrderID
                p, #ProductID
                random.randint(1,3)+random.randint(0,2), #Quantity
                random.randint(5,50), # UnitPrice (FAKE)
                random.randint(0,10), #Discount (FAKE)
            ])
    return retval