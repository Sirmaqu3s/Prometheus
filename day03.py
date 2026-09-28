skills = [
    {"name": "Python", "hours": 10},
    {"name": "SQL", "hours": 7},
    {"name": "Machine Learning", "hours": 4}
]

def total_hours(skills):
    total_count = 0
    for skill in skills:
        total_count = total_count + skill["hours"]
    return total_count

def alle_skills(skills):
    for skill in skills:
        print(skill["name"] + ": " + str(skill["hours"]))

def Strong_skills(skills):
    for skill in skills:
        if skill["hours"] >= 7:
            print(skill["name"])

result = total_hours(skills)

print("=== PROMETHEUS SKILLS ===")
alle_skills(skills)


print("=== STRONG SKILLS ===")
Strong_skills(skills)

print("=== totaal aantal uren ===")
print(result)

        
        