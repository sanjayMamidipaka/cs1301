


# import and use the following function for your HW05!
# please do not turn this file in when submitting!

def calculate(animal):
    storage = {
        'Clown Fish': 25,
        'Starfish': 60,
        'Silver Nose Shark': 29,
        'Sting Rays': 13,
        'Sea Otter': 31,
        'Dolphin': 75,
        'Humpback Whale': 54,
        'Octopus': 73,
        'Blue Whale': 89,
        'Jellyfish': 97,
        'Sea Lion': 38,
        'Seahorse': 85,
        'Alligators': 43
    }
    return storage.get(animal, 0)
    
