import pandas as pd
from datetime import date, timedelta

# Roster survey team's
roster_team_1_a = ["", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN"]
roster_team_1_b = ["", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN"]
roster_team_2_a = ["", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR"]
roster_team_2_b = ["", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", ""]
roster_team_3_a = ["N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", ""]
roster_team_3_b = ["N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", ""]
roster_team_4_a = ["L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", ""]
roster_team_4_b = ["L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", ""]
roster_team_5_a = ["R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", ""]
roster_team_5_b = ["R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", ""]
roster_team_6_a = ["D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD"]
roster_team_6_b = ["D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "WR", "WR", "", "", "", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD", "D", "D", "D", "", "", "", "", "R", "R", "R", "R", "R", "", "", "L", "L", "L", "L", "L", "", "", "N", "N", "N", "", "", "", "", "", "", "R", "N", "N", "WN", "WN", "", "", "", "D", "D", "WD", "WD"]

# Roster trucks Ghent team
trucks_ghent = ["D", "D", "D", "D", "D", "", ""]

# Roster TV team
tv = ["D", "D", "D", "D", "D", "", ""]

# Roster SPS team
sps_a = ["O", "", "", "", "", "", "", "", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", "", "D", "D", "D", "D", "D", "", "", "", "O", "O", "O", "O", "O", "O"]
sps_b = ["", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", "", "D", "D", "D", "D", "D", "", "", "", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", ""]
sps_c = ["", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", "", "", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", "", "D", "D", "D", "D", "D", "", ""]
sps_d = ["D", "D", "D", "D", "D", "", "", "", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", "", "", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", ""]
sps_e = ["O", "", "", "", "", "", "", "D", "D", "D", "D", "D", "", "", "", "O", "O", "O", "O", "O", "O", "O", "", "", "", "", "", "", "", "O", "O", "O", "O", "O", "O"]

# Roster LBC Maritime team
lbc_1 = ["R", "R", "R", "R", "", "", "", "D", "D", "D", "D", "D", "", "", "N", "N", "", "", "R", "WR", "WR", "", "", "N", "N", "N", "WN", "WN", "", "", "", "", "", "WD", "WD", "L", "L", "L", "L", "L", "", ""]
lbc_2 = ["N", "N", "", "", "R", "WR", "WR", "", "", "N", "N", "N", "WN", "WN", "", "", "", "", "", "WD", "WD", "L", "L", "L", "L", "L", "", "", "R", "R", "R", "R", "", "", "", "D", "D", "D", "D", "D", "", ""]
lbc_3 = ["L", "L", "L", "L", "L", "", "", "R", "R", "R", "R", "", "", "", "D", "D", "D", "D", "D", "", "", "N", "N", "", "", "R", "WR", "WR", "", "", "N", "N", "N", "WN", "WN", "", "", "", "", "", "WD", "WD"]
lbc_4 = ["", "", "N", "N", "N", "WN", "WN", "", "", "", "", "", "WD", "WD", "L", "L", "L", "L", "L", "", "", "R", "R", "R", "R", "", "", "", "D", "D", "D", "D", "D", "", "", "N", "N", "", "", "R", "WR", "WR"]
lbc_5 = ["", "", "", "", "", "WD", "WD", "L", "L", "L", "L", "L", "", "", "R", "R", "R", "R", "", "", "", "D", "D", "D", "D", "D", "", "", "N", "N", "", "", "R", "WR", "WR", "", "", "N", "N", "N", "WN", "WN"]
lbc_6 = ["D", "D", "D", "D", "D", "", "", "N", "N", "", "", "R", "WR", "WR", "", "", "N", "N", "N", "WN", "WN", "", "", "", "", "", "WD", "WD", "L", "L", "L", "L", "L", "", "", "R", "R", "R", "R", "", "", ""]

# Roster LBC Truck Team
lbc_trucks_1 = ["D", "D", "D", "D", "D", "", "", "L", "L", "L", "L", "L", "", ""]
lbc_trucks_2 = ["L", "L", "L", "L", "L", "", "", "D", "D", "D", "D", "D", "", ""]

# Making the correct day_list
table_day_team_1_a = []
table_day_team_1_b = []
table_day_team_2_a = []
table_day_team_2_b = []
table_day_team_3_a = []
table_day_team_3_b = []
table_day_team_4_a = []
table_day_team_4_b = []
table_day_team_5_a = []
table_day_team_5_b = []
table_day_team_6_a = []
table_day_team_6_b = []
table_day_trucks_ghent = []
table_day_tv = []
table_day_sps_a = []
table_day_sps_b = []
table_day_sps_c = []
table_day_sps_d = []
table_day_sps_e = []
table_day_lbc_1 = []
table_day_lbc_2 = []
table_day_lbc_3 = []
table_day_lbc_4 = []
table_day_lbc_5 = []
table_day_lbc_6 = []
table_day_lbc_trucks_1 = []
table_day_lbc_trucks_2 = []
date_day = []
date_day_week = []
week_number = []
month = []
number_of_week = []
day_of_week = []
day_of_week_table = []


# defining the date range
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# setting the start and end date
start_date = date(2021, 1, 4)
end_date = date(2030, 1, 2)

# append the dates to date_day list
for single_date in daterange(start_date, end_date):
    date_day.append(single_date.strftime('%d-%m-%Y'))
    month.append(single_date.strftime('%B'))
    date_day_week.append(single_date)

x = 0
for i in date_day:
    week_number.append(date_day_week[x].isocalendar()[1])
    day_of_week.append(date_day_week[x].strftime('%A'))
    x += 1

while len(number_of_week) < len(date_day):
    for i in week_number:
        number_of_week.append(i)
        if len(number_of_week) == len(date_day):
            break

while len(day_of_week_table) < len(date_day):
    for i in day_of_week:
        day_of_week_table.append(i)
        if len(day_of_week_table) == len(date_day):
            break

# append the shift to table_day list
while len(table_day_team_1_a) < len(date_day):
    for i in roster_team_1_a:
        table_day_team_1_a.append(i)
        if len(date_day) == len(table_day_team_1_a):
            break

while len(table_day_team_1_b) < len(date_day):
    for i in roster_team_1_b:
        table_day_team_1_b.append(i)
        if len(date_day) == len(table_day_team_1_b):
            break

while len(table_day_team_2_a) < len(date_day):
    for i in roster_team_2_a:
        table_day_team_2_a.append(i)
        if len(date_day) == len(table_day_team_2_a):
            break

while len(table_day_team_2_b) < len(date_day):
    for i in roster_team_2_b:
        table_day_team_2_b.append(i)
        if len(date_day) == len(table_day_team_2_b):
            break

while len(table_day_team_3_a) < len(date_day):
    for i in roster_team_3_a:
        table_day_team_3_a.append(i)
        if len(date_day) == len(table_day_team_3_a):
            break

while len(table_day_team_3_b) < len(date_day):
    for i in roster_team_3_b:
        table_day_team_3_b.append(i)
        if len(date_day) == len(table_day_team_3_b):
            break

while len(table_day_team_4_a) < len(date_day):
    for i in roster_team_4_a:
        table_day_team_4_a.append(i)
        if len(date_day) == len(table_day_team_4_a):
            break

while len(table_day_team_4_b) < len(date_day):
    for i in roster_team_4_b:
        table_day_team_4_b.append(i)
        if len(date_day) == len(table_day_team_4_b):
            break

while len(table_day_team_5_a) < len(date_day):
    for i in roster_team_5_a:
        table_day_team_5_a.append(i)
        if len(date_day) == len(table_day_team_5_a):
            break

while len(table_day_team_5_b) < len(date_day):
    for i in roster_team_5_b:
        table_day_team_5_b.append(i)
        if len(date_day) == len(table_day_team_5_b):
            break

while len(table_day_team_6_a) < len(date_day):
    for i in roster_team_6_a:
        table_day_team_6_a.append(i)
        if len(date_day) == len(table_day_team_6_a):
            break

while len(table_day_team_6_b) < len(date_day):
    for i in roster_team_6_b:
        table_day_team_6_b.append(i)
        if len(date_day) == len(table_day_team_6_b):
            break

while len(table_day_trucks_ghent) < len(date_day):
    for i in trucks_ghent:
        table_day_trucks_ghent.append(i)
        if len(date_day) == len(table_day_trucks_ghent):
            break

while len(table_day_tv) < len(date_day):
    for i in tv:
        table_day_tv.append(i)
        if len(date_day) == len(table_day_tv):
            break

while len(table_day_sps_a) < len(date_day):
    for i in sps_a:
        table_day_sps_a.append(i)
        if len(date_day) == len(table_day_sps_a):
            break

while len(table_day_sps_b) < len(date_day):
    for i in sps_b:
        table_day_sps_b.append(i)
        if len(date_day) == len(table_day_sps_b):
            break

while len(table_day_sps_c) < len(date_day):
    for i in sps_c:
        table_day_sps_c.append(i)
        if len(date_day) == len(table_day_sps_c):
            break

while len(table_day_sps_d) < len(date_day):
    for i in sps_d:
        table_day_sps_d.append(i)
        if len(date_day) == len(table_day_sps_d):
            break

while len(table_day_sps_e) < len(date_day):
    for i in sps_e:
        table_day_sps_e.append(i)
        if len(date_day) == len(table_day_sps_e):
            break

while len(table_day_lbc_1) < len(date_day):
    for i in lbc_1:
        table_day_lbc_1.append(i)
        if len(date_day) == len(table_day_lbc_1):
            break

while len(table_day_lbc_2) < len(date_day):
    for i in lbc_2:
        table_day_lbc_2.append(i)
        if len(date_day) == len(table_day_lbc_2):
            break

while len(table_day_lbc_3) < len(date_day):
    for i in lbc_3:
        table_day_lbc_3.append(i)
        if len(date_day) == len(table_day_lbc_3):
            break

while len(table_day_lbc_4) < len(date_day):
    for i in lbc_4:
        table_day_lbc_4.append(i)
        if len(date_day) == len(table_day_lbc_4):
            break

while len(table_day_lbc_5) < len(date_day):
    for i in lbc_5:
        table_day_lbc_5.append(i)
        if len(date_day) == len(table_day_lbc_5):
            break

while len(table_day_lbc_6) < len(date_day):
    for i in lbc_6:
        table_day_lbc_6.append(i)
        if len(date_day) == len(table_day_lbc_6):
            break

while len(table_day_lbc_trucks_1) < len(date_day):
    for i in lbc_trucks_1:
        table_day_lbc_trucks_1.append(i)
        if len(date_day) == len(table_day_lbc_trucks_1):
            break

while len(table_day_lbc_trucks_2) < len(date_day):
    for i in lbc_trucks_2:
        table_day_lbc_trucks_2.append(i)
        if len(date_day) == len(table_day_lbc_trucks_2):
            break

# print(len(table_day_team_1_a))
# print(len(date_day))

# making the table roster
table = {"Date": date_day,
         "Week": number_of_week,
         "Month": month,
         "Day": day_of_week_table,
         "Team 1": "",
         "Dieter De Peuter": table_day_team_1_a,
         "Kevin Verstricht": table_day_team_1_b,
         "Anton Hladchenko": table_day_team_1_b,
         "Bart Sonck": table_day_team_1_a,
         "Ben Verlent": table_day_team_1_b,
         "Guillaume Pernet": table_day_team_1_a,
         "Tom Wille": table_day_team_1_a,
         "Kevin Noël": table_day_team_1_b,
         "Team 2": "",
         "Yannick De Groef": table_day_team_2_a,
         "Kane Kalidou": table_day_team_2_b,
         "Mohcine Bouayad": table_day_team_2_b,
         "Tom Depraetere": table_day_team_2_a,
         "Zakaria El Hadri": table_day_team_2_a,
         "Team 3": "",
         "Michael Delaruelle": table_day_team_3_a,
         "Vlad Meeusen": table_day_team_3_a,
         "Lloïc Van der Venne": table_day_team_3_b,
         "Bart Van Britsom": table_day_team_3_b,
         "Aatif Koudad": table_day_team_3_b,
         "Sofyan Lakdim": table_day_team_3_b,
         "Gregory Van de Vloet": table_day_team_3_b,
         "Jeroen Verbruggen": table_day_team_3_a,
         "Marwan Salhi": table_day_team_3_a,
         "Aaron Van Goethem": table_day_team_3_b,
         "Toon Van Wolvelaer": table_day_team_3_a,
         "Team 4": "",
         "Sander Cornelis": table_day_team_4_a,
         "Massimo Joris": table_day_team_4_b,
         "Sean Van Nuffelen": table_day_team_4_b,
         "Bert Claessens": table_day_team_4_b,
         "Vincent Snel": table_day_team_4_a,
         "Bjorn Dingenen": table_day_team_4_a,
         "Justin Van Cauwenberghe": table_day_team_4_a,
         "Dorian Dhaenens": table_day_team_4_b,
         "Team 5": "",
         "Bart Schyvens": table_day_team_5_a,
         "Martijn Bastin": table_day_team_5_a,
         "Stijn Van Briel": table_day_team_5_b,
         "Ansoumane Dansoko": table_day_team_5_b,
         "Matthy Maas": table_day_team_5_a,
         "Chris Maes": table_day_team_5_a,
         "Adam Essabri": table_day_team_5_b,
         "Mick Ntambwe": table_day_team_5_b,
         "Lukas Leys": table_day_team_5_a,
         "Robin Wille": table_day_team_5_b,
         "Team 6": "",
         "Marvin De Lange": table_day_team_6_a,
         "Samuel Nolf": table_day_team_6_b,
         "Ibrahim Elya": table_day_team_6_b,
         "Jeroen Van Wijk": table_day_team_6_b,
         "Karim Chakouh": table_day_team_6_a,
         "Vadim Isaharov": table_day_team_6_b,
         "Ali Chantah": table_day_team_6_a,
         "Lennert Gorrebeeck": table_day_team_6_b,
         "Trucks Gent": "",
         "Tibo Pinoy": table_day_trucks_ghent,
         "SPS": "",
         "Mich Vogelweith": table_day_sps_a,
         "Stijn D'Hondt": table_day_sps_b,
         "Alexandre Tishenkov": table_day_sps_c,
         "Fabian Dillen": table_day_sps_d,
         "Andy Kuhn": table_day_sps_e,
         "LBC Marine": "",
         "Mehdi Zirari": table_day_lbc_1,
         "Nico Cools": table_day_lbc_4,
         "Nicolas De Pourcq": table_day_lbc_2,
         "": table_day_lbc_5,
         "Khalid Benkaddor": table_day_lbc_3,
         "Tim Wuijts": table_day_lbc_6,
         "LBC Trucks": "",
         "Maarten Van Geystelen": table_day_lbc_trucks_1,
         "Ahmed Bousikhani": table_day_lbc_trucks_1,
         "Lesley Fierens": table_day_lbc_trucks_1,
         "Wim Schroons": table_day_lbc_trucks_2,
         "Glenn Van De Woestyne": table_day_lbc_trucks_2,
         "Roël Linger": table_day_lbc_trucks_2,
         "Kjell Daems": table_day_lbc_trucks_2,
         "LBC Coordinator": "",
         "Kenny Verstraelen": table_day_lbc_trucks_1,
         "Stijn Vervynckt": table_day_lbc_trucks_2,
         "TV": "",
         "Keanu Voorspools": table_day_tv,
         "Kevin Van Den Broeck": table_day_tv,
         "Kevin Koyen": table_day_tv,
         "Alexander van Duyse": table_day_tv,
         "Tim De Meyer": table_day_tv,
         }

data = pd.DataFrame(table)

print(data)

with pd.ExcelWriter("Jaarrooster_v2_test.xlsx") as writer:
    data.to_excel(writer, sheet_name='Sheet_1')
