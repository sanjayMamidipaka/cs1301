print(("Good",) + (4,) + ("You",))

print([["Solar", "Power"]] * 2)

print("pitch perfect" in ["pitch", "perfect"])
print({print("scary"): "hours", 2: ";p"}[None])
print(( "Surf's Up", {"The": "Beach Boys"[2], "Beach": [2]} ) [1] ["The"] * 3)

aList = ["Dolly Parton", "Arlo Guthrie", "Paul Simon"]

cList = aList

cList.append("Pete Seeger")

bList = cList[:]

bList.remove("Paul Simon")

cList += "Elivis"

print(cList)