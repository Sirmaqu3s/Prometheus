onderwerpen = []
aantal_onderwerpen = int(input("hoeveel onderwerpen heb je vandaag gezien?: "))

for i in range(aantal_onderwerpen):
    onderwerp = input("welke onderwerp heb je vandaag gezien?: ").lower()
    onderwerpen.append(onderwerp)

def alle_onderwerpen(onderwerp):
    print("onderwerp: " + onderwerp)

print("=== TODAY'S TRAINING ===")
for onderwerp in onderwerpen:
    alle_onderwerpen(onderwerp)
print("aantal onderwerpen: " + str(len(onderwerpen)))

search = input("welke onderwerp zoek je?: ").lower().strip()
if search in onderwerpen:
    print("onderwerp gevonden: " + str(search))
else:
    print("onderwerp niet gevonden")
    