boodschappenlijst=["melk","water","brood","kaas","eieren","chips","rijst"]
lijst=str(boodschappenlijst)


file = open("bestand1.txt","a")
file.write(lijst)
file.close

x = input("Wat wil je kopen? ")

if x in boodschappenlijst:
    print ("Ja, dit staat al op de lijst")
else:
    print("Dit staat nog niet op de lijst!")