print(("Good",) + (4,) + ("You",))

print([["Solar", "Power"]] * 2)

print("pitch perfect" in ["pitch", "perfect"])
print({print("scary"): "hours", 2: ";p"}[None])
print(( "Surf's Up", {"The": "Beach Boys"[2], "Beach": [2]} ) [1] ["The"] * 3)

# aList = ["Dolly Parton", "Arlo Guthrie", "Paul Simon"]

# cList = aList

# cList.append("Pete Seeger")

# bList = cList[:]

# bList.remove("Paul Simon")

# cList += "Elivis"

# print(cList)

aList = [["Everything", "Everything"], "jammin’", 2020]

bList = aList

cList = bList[:]

aList[2] = aList[2] + 1

cList[0][1] = "All the Time"

bList.append("vibes") 

cList[0] = "Fleet Foxes"
print(cList)

def festival(artistList): 
    goodArtists = [] 
    songRating = {"Breezeblocks": 9, "Skinny Love": 9, "Riptide": 5, "Oxford Comma": 8, "Holland, 1946": 7} 
    for artist in artistList: 
        try: 
            if songRating[artistList[artist]] > 7: 
                goodArtists.append(artist) 
            else: 
                print("not good enough") 
        except: 
            print("not one of your artists") 
            continue 
    return goodArtists 
artistList= {"alt—J": "Breezeblocks", "The Strokes": "Hard To Explain", "Bon Iver": "Skinny Love", "Vampire Weekend": "Oxford Comma"} 
print(festival(artistList)) 

def noteFile(notes):
    sheet = open('sheet.txt', 'w')
    for note in notes:
        sheet.write(note + '\n')
    sheet.close()
    music = open('sheet.txt')
    one = music.readlines()
    print(one[2][0])

notes = 'ABCAG'
noteFile(notes)

def concerts(): 
    ratings = {5.0: ["The Shins"], 4.5: ["The", "Beatles"]}
    venues = [(5.0, "infinite energy"), (2, "the loft")] 
    for r, c in venues: 
        if r in ratings: 
            print("Add {} to {}".format(c, r)) 
            ratings[r].append(c) 
        else: 
            print("Add {} to ratings".format(r)) 
print(concerts()) 

def listen(platformDict):
    platformName = ''
    platformUsers = 0

    for key in platformDict:
        if len(platformDict[key]) > platformUsers:
            platformName = key
            platformUsers = len(platformDict[key])

    return (platformName, platformUsers)

listen({'sptofy': ['c','k','e'], })


    
 