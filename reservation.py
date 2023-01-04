import random
import datetime

def reservation(dailyLOW:int,
                dailyHIGH:int,
                days:int,
                startDay:datetime.date,
                individuelID:list[int],
                companyID:list[int],
                tableID:list[int]
                ):
    if(dailyLOW>dailyHIGH): #sanity check
        dailyHIGH,dailyLOW = dailyLOW,dailyHIGH
        print("Warning: reservation DailyLOW > DailyHIGH. Swapped.")
    
    reservation = []
    reservation_details = []
    reservationClients = []
    reservationCompanies = []
    
    daily = [random.randint(dailyLOW,dailyHIGH) for i in range(days)]
    cday = startDay
    reservationIndex = 1
    DetailIndex = 1
    for day in range(days):
        reservation_in_day = [] # optymalizacyjne.
        reservation_details_in_day = [] # Stoliki potrzebują przeszukiwać całą tą przestrzeń, więc ograniczny się do rezerwacji z obecnego dnia.
        for i in range(daily[day]):
            
            client = None 
            if random.randint(0,100) < 60: 
                client = individuelID[random.randint(0,len(individuelID)-1)]
            else:
                client = companyID[random.randint(0,len(companyID)-1)]
            applied = True if random.randint(0,100) < 95 else False
            startTime = startDay + datetime.timedelta(hours=random.randint(8,15),minutes=random.randint(0,59)) 
            endTime = startTime + datetime.timedelta(hours=random.randint(0,2),minutes=30*random.randint(0,1))
            
            # FIXME: Dobre miejsce na wpisanie kodu dla ReesrvationClient / ReesrvationCompany.
            
            if(client in individuelID):
                reservationClients.append([reservationIndex,client,"null"])
            elif random.randint(0,100) < 5:
                reservationCompanies.append([reservationIndex,client,individuelID[random.randint(0,len(individuelID)-1)]])
            else:
                reservationCompanies.append([reservationIndex,client,"null"])
            
            res = [
                reservationIndex, #ID
                client, #ClientID
                applied, #reservationApplied
                startTime, # startDate
                endTime # endDate
            ]
            reservation_in_day.append(res)
            reservationIndex+=1

            
            #Znaleźć jakiś stolik dla res jeśli ma to sens. (efektywnie udawanie SQLa w Pythonie)
            
            #Najpierw znaleźć wszystkie ID rezerwacji które nie mogą być na tym samym stoliku.
            isForbidding = lambda reservation: not canHaveSameTable(reservation, res) #funkcja filtrująca.
            forbidding_reservationIDs = [i for i in reservation_in_day] # Bierzemy wszyskie rezerwacje tego dnia.
            filter(isForbidding,forbidding_reservationIDs) # filtrujemy tylko do tych które blokują nam stoliki
            forbidding_reservationIDs = [ i[0] for i in forbidding_reservationIDs]  # wyciągamy ID
            # efektywnie SELECT ID FROM Reservations WHERE (zachodzi konflikt czasowy)
            
            
            # Teraz znaleźć wszystkie ID wolnych stolików.
            #Najpierw znajdujemy wszystkie ID zajętych stolików.
            isForbidden = lambda detail: detail[1] in forbidding_reservationIDs # funkcja filtrująca.
            forbidden_Tables = [i for i in reservation_details_in_day] # Bierzemy wszystkie stoliki
            filter(isForbidden,forbidden_Tables) # fultrujemy do tych które są wolne
            forbidden_Tables = [i[2] for i in forbidden_Tables] # bierzemy tylko ID
            
            #Bierzemy wszystkie stoliki poza zajętymi.
            isAvalible = lambda table: table not in forbidden_Tables
            avalible_Tables = [i for i in tableID]
            filter(isAvalible,avalible_Tables)
            
            #Faktyczne dodwawanie do ReservationDetails.
            if(len(avalible_Tables)>1 and random.randint(0,100) < 5 ): #Jeżeli sie uda to 5% rezerwacji jest na dwa stoliki
                reservation_details_in_day.append([
                    DetailIndex, #DetailID
                    res[0], #ReservationID
                    avalible_Tables[0] # Pierwszy z brzegu
                ]);DetailIndex+=1
                reservation_details_in_day.append([
                    DetailIndex,
                    res[0],
                    avalible_Tables[-1] #Ostatni. Można losować, ale nie chce mi się tłuc z randomInt(1,1) bo to może sypać błędy.
                ]);DetailIndex+=1
            else: # 1 albo 0 wolnych stolików na ten timeslot.
                avalible_Tables.append("NULL") # Dołóżny rezerwacje bez stolika.
                avalible_Tables.append("NULL") # Trochę więcej rezerwacji bez stolika.
                reservation_details_in_day.append([
                    DetailIndex,
                    res[0],
                    avalible_Tables[random.randint(0,len(avalible_Tables)-1)]
                ]);DetailIndex+=1
            
        for i in reservation_in_day:
            reservation.append(i)
        for i in reservation_details_in_day:
            reservation_details.append(i)
        cday = cday + datetime.timedelta(days=1)
    return (reservation,reservation_details,reservationClients,reservationCompanies)


# Can reservation be seated at the same table as context?
def canHaveSameTable(reservation, context):
    sti = 3 # startTimeIndex
    eti = 4 # endTimeIndex
    return reservation[sti] > context[eti] or reservation[eti] < context[sti]