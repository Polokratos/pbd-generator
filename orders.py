import random
import datetime
from heplers import formatDate

def orders(dailyLOW:int,
           dailyHIGH:int,
           startDate:datetime.date,
           days:int,
           reservations:list[list], #Potrzebujemy dwóch pól z rezerwacji (ResrevationID i ClientID)
           individuelID:list[int] #Oprócz tego luzem listę klientów indywidualnych dla przypadku bez rezerwacji i pilnowani żeby rezerwacje na indywiduela miały jeden order.
           ):
    
    if(dailyLOW>dailyHIGH): #sanity check
        dailyHIGH,dailyLOW = dailyLOW,dailyHIGH
        print("Warning: reservation DailyLOW > DailyHIGH. Swapped.")
    daily = [random.randint(dailyLOW,dailyHIGH) for _ in range(days)]
    retval = []
    
    index = 1
    # Bez rezerwacji
    for day in range(days):
        for _ in range(daily[day]):
            
            takeaway = True if random.randint(0,100) < 25 else False# takeaway
            paid = True if takeaway else (True if random.randint(0,100) < 1 else False) #1% podpierdalajo
            retval.append([
                index, #ID
                "NULL", #ReservationID
                individuelID[random.randint(0,len(individuelID)-1)], #random individual client (ClientID)
                formatDate(days + datetime.timedelta(days=day)),
                takeaway, #takeaway
                paid # paid
            ]);index+=1
    #end for
    
    #Z rezerwacją. Wiem, indeskowanie wyjdzie dziwne ale mam to gdzieś. 
    # Naprawianie tego może oprzeć się na posortowaniu i pozmienianiu indeksów,
    # jeżeli bardzo będzie to potrzebne Zygmunt.
    
    reservationIDIndex = 0
    ClientIDIndex = 1
    DateIndex = 3
    for res in reservations:
        if(res[ClientIDIndex] in individuelID): # na indywiduela
            retval.append([
                index, #OrderID
                res[reservationIDIndex], #ReservationID
                res[ClientIDIndex], #ClientID
                formatDate(res[DateIndex]),
                False, #Takeaway
                True #Paid
            ]);index+=1
        else: # na firme
            if(random.randint(0,100) < 50): # firma zamawia na siebie.
                retval.append([
                    index, #OrderID
                    res[reservationIDIndex], #ReservationID
                    res[ClientIDIndex], #ClientID
                    formatDate(res[DateIndex]),
                    False, #Takeaway
                    True #Paid
                ]);index+=1
            else: # Firma zamawia na pracownika
                retval.append([
                    index,
                    individuelID[random.randint(0,len(individuelID)-1)], #random individual client (ClientID)
                    formatDate(res[DateIndex]),
                    False, #Takeaway
                    True #Paid
                ]);index+=1
            #Oprócz zamówienia głównego:
            if(random.randint(0,100) < 5) # 5% szans że firma złoży ekstra zamówienie na pracownika.
                retval.append([
                    index,
                    individuelID[random.randint(0,len(individuelID)-1)], #random individual client (ClientID)
                    formatDate(res[DateIndex]),
                    False, #Takeaway
                    True #Paid
                ]);index+=1
    return retval