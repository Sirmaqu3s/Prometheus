skills = []
exit_vraag = ""
hoeveel_skills = int(input("hoeveel skills heb je geleerd"))

for i in range(hoeveel_skills):
    skill_vraag = input("welke skill wil je leren: ").lower().strip()
    skills.append(skill_vraag)

uren = float(input("hoeveel uren heb je gesturdeerd?"))

skill = input("welke skill zoek je?").lower().strip()

print("=== PROMETHEUS TRAINING ===")
for skill_vraag in skills:
    print(skill_vraag)

if uren < 1:
    print("low dedication")
elif 1 <= uren < 3:
    print("Solid session")
else: 
    print ("deep work session") 

if skill in skills:
    print("skill gevonden: " + skill)
else:
    print("skill niet gevonden")

while exit_vraag != "exit" and exit_vraag != "quit":
    exit_vraag = input("schrijf exit om uit het programma te gaan: ").lower().strip()

print("je bent succesvol uitgelogd") 



