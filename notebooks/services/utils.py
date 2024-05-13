def get_snow_cards():
    return ["Arctic Foxes", "Balduvian Conjurer", "Barbarian Guides", "Drift of the Dead", "Frost Bite", "Icequake", "Into the North", "Kjeldoran Guard", "Priest of the Haunted Edge", "Rimewind Taskmage", "Ronom Serpent", "Sculptor of Winter", "Skred", "Snow Devil", "Thermokarst", "Whiteout", "Woolly Mammoths", "Zombie Musher"]


def get_snow_lands():
    return ["Snow-Covered Plains", "Snow-Covered Island", "Snow-Covered Black", "Snow-Covered Mountain", "Snow-Covered Forest"]


def get_banned_cards():
    return ["_____ Bird Gets the Worm", "_____ Goblin", "_____-o-saurus", "Aarakocra Sneak", "Aerialephant", "All That Glitters", "Arcum's Astrolabe", "Atog", "Bonder's Ornament", "Carnival Carnivore", "Chatterstorm", "Chicken Troupe", "Cloud of Faeries", "Cloudpost", "Command Performance", "Cranial Plating", "Daze", "Disciple of the Vault", "Empty the Warrens", "Fall from Favor", "Finishing Move", "Frantic Search", "Galvanic Relay", "Gitaxian Probe", "Glitterflitter", "Grapeshot", "Gush", "High Tide", "Hymn to Tourach", "Invigorate", "Minotaur de Force", "Monastery Swiftspear", "Mystic Sanctuary", "Peregrine Drake", "Pradesh Gypsies", "Prize Wall", "Prophetic Prism", "Robo-Piñata", "Sinkhole", "Sojourner's Companion", "Stiltstrider", "Stirring Bard", "Stone-Throwing Devils", "Temporal Fissure", "Ticketomaton", "Treasure Cruise", "Underdark Explorer", "Vicious Battlerager", "Wizards of the _____", "Wolf in _____ Clothing"]


def rename_name_sticker_goblin(list):
    return [card.replace("________ Goblin", "_____ Goblin", 1) if card == "________ Goblin" else card for card in list]


def remove_snow_covered_lands(list):
    if not any(item in list for item in get_snow_cards()) and any(item in list for item in get_snow_lands()):
        return [card.replace("Snow-Covered ", "", 1) for card in list]
    return list
