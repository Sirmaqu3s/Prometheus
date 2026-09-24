naam = input("wat is je naam? ")
uren_per_week = float(input("hoeveel uren per week ga je studeren? "))
aantal_maanden = int(input("hoeveel maanden ga je dit volhouden? "))
aantal_studie_uren = uren_per_week * aantal_maanden * 4


if aantal_studie_uren >= 400:
    print("naam: " + naam)
    print("aantal studie uren: " + str(aantal_studie_uren))
    print("status: High commitment")
elif 200 <= aantal_studie_uren < 400:
    print("naam: " + naam)
    print("aantal studie uren: " + str(aantal_studie_uren))
    print("status: strong commitment")
elif 100 <= aantal_studie_uren < 200:
    print("naam: " + naam)
    print("aantal studie uren: " + str(aantal_studie_uren))
    print("status: moderate commitment")
else:
    print("naam: " + naam)
    print("aantal studie uren: " + str(aantal_studie_uren))
    print("status: low commitment")