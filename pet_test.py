import d1_pet as d1

hund1 = d1.Pet()
hund1.name = "Pluto"
hund1.kind = "hund"
print(hund1)
hund1.add_toy("boll")
print(hund1)

katt1 = d1.Pet("Misse")
katt1.kind = "katt"
katt1.add_toy("fjäder")
print(katt1)
katt1.add_toy("fjäder")
print(katt1)
katt1.add_toy("tygråtta")
print(katt1)
