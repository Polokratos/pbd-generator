import random
cities = ["Warszawa","Kraków","Wrocław","Katowice","Szczecin","Częstochowa"]
streets = ["Mickiewicza","Słowackiego","Szeroka","Czarnowiejska","Mogilska","Grochowska","Olszyny"]
domains = ["gmail.com","wp.pl","outlook.org","pm.com","gmail.com"]
names = ["Jan","Stanisław","Andrzej","Józef","Tadeusz","Jerzy","Zbigniew","Krzysztof","Henryk","Ryszard","Kazimierz","Marek","Marian","Piotr","Janusz","Władysław","Adam","Wiesław","Zdzisław","Edward","Mieczysław","Roman","Maria","Krystyna","Anna","Barbara","Teresa","Elżbieta","Janina","Zofia","Jadwiga","Danuta","Halina","Irena","Ewa","Małgorzata"]

def clients(amt:int):
    clients = []
    individuel = []
    company = []
    
    for i in range(amt):
        clients.append([
            i+1, #ClientID
            cities[random.randint(0,len(cities)-1)], #city
            streets[random.randint(0,len(streets)-1)], #street
            str(random.randint(10,30))+'-'+str(random.randint(100,999)), #postalCode
            '+48'+str(random.randint(100_000_000,999_999_999)), #phone
            "klient"+str(i+1)+'@'+domains[random.randint(0,len(domains)-1)] #e-mail
        ])
        if(random.randint(0,100) > 60): #firma
            company.append([
                i+1, #ID
                "company"+str(i+1) #Nazwa
            ])
        else: #indywiduel
            individuel.append([
                i+1, #ID
                names[random.randint(0,len(names)-1)], #imie
                "nazwisko"+str(i+1) #nazwisko
            ])
    return (clients,individuel,company)