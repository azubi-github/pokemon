import pygame

POKEMON_DATA = {
    'Bulbasaur': {'name': 'Bulbasaur', 'element': 'Grass', 'health': 142, 'attack': 90, 'defense': 97, 'speed': 45},
    'Charmander': {'name': 'Charmander', 'element': 'Fire', 'health': 188, 'attack': 112, 'defense': 94, 'speed': 122},
    'Squirtle': {'name': 'Squirtle', 'element': 'Water', 'health': 155, 'attack': 100, 'defense': 108, 'speed': 43},
    'Caterpie': {'name': 'Caterpie', 'element': 'Bug', 'health': 128, 'attack': 70, 'defense': 50, 'speed': 45},
    'Weedle': {'name': 'Weedle', 'element': 'Bug', 'health': 128, 'attack': 70, 'defense': 50, 'speed': 45},
    'Pidgey': {'name': 'Pidgey', 'element': 'Normal', 'health': 145, 'attack': 80, 'defense': 60, 'speed': 91},
    'Rattata': {'name': 'Rattata', 'element': 'Normal', 'health': 150, 'attack': 108, 'defense': 60, 'speed': 97},
    'Spearow': {'name': 'Spearow', 'element': 'Normal', 'health': 145, 'attack': 100, 'defense': 60, 'speed': 120},
    'Ekans': {'name': 'Ekans', 'element': 'Poison', 'health': 145, 'attack': 100, 'defense': 69, 'speed': 80},
    'Pikachu': {'name': 'Pikachu', 'element': 'Electric', 'health': 140, 'attack': 90, 'defense': 55, 'speed': 110},
    'Sandshrew': {'name': 'Sandshrew', 'element': 'Ground', 'health': 145, 'attack': 100, 'defense': 110, 'speed': 65},
    'Nidoran': {'name': 'Nidoran', 'element': 'Poison', 'health': 140, 'attack': 80, 'defense': 70, 'speed': 60},
    'Clefairy': {'name': 'Clefairy', 'element': 'Fairy', 'health': 166, 'attack': 70, 'defense': 70, 'speed': 60},
    'Vulpix': {'name': 'Vulpix', 'element': 'Fire', 'health': 145, 'attack': 90, 'defense': 60, 'speed': 100},
    'Jigglypuff': {'name': 'Jigglypuff', 'element': 'Normal', 'health': 190, 'attack': 70, 'defense': 45, 'speed': 20},
    'Zubat': {'name': 'Zubat', 'element': 'Poison', 'health': 145, 'attack': 70, 'defense': 55, 'speed': 105},
    'Paras': {'name': 'Paras', 'element': 'Bug', 'health': 138, 'attack': 95, 'defense': 70, 'speed': 45},
    'Machop': {'name': 'Machop', 'element': 'Fighting', 'health': 170, 'attack': 130, 'defense': 70, 'speed': 55},
    'Bellsprout': {'name': 'Bellsprout', 'element': 'Grass', 'health': 134, 'attack': 80, 'defense': 65, 'speed': 60},
    'Geodude': {'name': 'Geodude', 'element': 'Rock', 'health': 160, 'attack': 130, 'defense': 120, 'speed': 45},
    'Magikarp': {'name': 'Magikarp', 'element': 'Water', 'health': 120, 'attack': 40, 'defense': 20, 'speed': 80},
    'Poliwag': {'name': 'Poliwag', 'element': 'Water', 'health': 130, 'attack': 50, 'defense': 50, 'speed': 90},
    'Dratini': {'name': 'Dratini', 'element': 'Dragon', 'health': 150, 'attack': 80, 'defense': 65, 'speed': 60},
    'Porygon': {'name': 'Porygon', 'element': 'Normal', 'health': 190, 'attack': 80, 'defense': 70, 'speed': 40},
    'Eevee': {'name': 'Eevee', 'element': 'Normal', 'health': 165, 'attack': 65, 'defense': 60, 'speed': 55},
    'Amonita': {'name': 'Amonita', 'element': 'Rock', 'health': 180, 'attack': 60, 'defense': 100, 'speed': 40},
    'Ditto': {'name': 'Ditto', 'element': 'Normal', 'health': 155, 'attack': 48, 'defense': 48, 'speed': 48},
    'Tauros': {'name': 'Tauros', 'element': 'Normal', 'health': 190, 'attack': 125, 'defense': 95, 'speed': 100},
    'Pinsir': {'name': 'Pinsir', 'element': 'Bug', 'health': 175, 'attack': 155, 'defense': 85, 'speed': 105},
    "Kha'Zix": {'name': "Kha'Zix", 'element': 'Bug', 'health': 175, 'attack': 155, 'defense': 85, 'speed': 105},
    'Magmar': {'name': 'Magmar', 'element': 'Fire', 'health': 185, 'attack': 100, 'defense': 85, 'speed': 93},
    'Elektek': {'name': 'Elektek', 'element': 'Electric', 'health': 185, 'attack': 123, 'defense': 60, 'speed': 105},
    'Staryu': {'name': 'Staryu', 'element': 'Water', 'health': 140, 'attack': 70, 'defense': 55, 'speed': 85},
    'Goldeen': {'name': 'Goldeen', 'element': 'Water', 'health': 145, 'attack': 90, 'defense': 55, 'speed': 63},
    'Seel': {'name': 'Seel', 'element': 'Water', 'health': 155, 'attack': 70, 'defense': 100, 'speed': 45},
    'Kangaskhan': {'name': 'Kangaskhan', 'element': 'Normal', 'health': 225, 'attack': 95, 'defense': 80, 'speed': 90},
    'Tangela': {'name': 'Tangela', 'element': 'Grass', 'health': 190, 'attack': 70, 'defense': 115, 'speed': 60},
    'Chansey': {'name': 'Chansey', 'element': 'Normal', 'health': 250, 'attack': 5, 'defense': 70, 'speed': 50},
    'Smogon': {'name': 'Smogon', 'element': 'Poison', 'health': 140, 'attack': 50, 'defense': 55, 'speed': 70},
    'Lickitung': {'name': 'Lickitung', 'element': 'Normal', 'health': 190, 'attack': 90, 'defense': 75, 'speed': 30},
    'Hitmonlee': {'name': 'Hitmonlee', 'element': 'Fighting', 'health': 180, 'attack': 130, 'defense': 70, 'speed': 87},
    'Tragosso': {'name': 'Tragosso', 'element': 'Rock', 'health': 180, 'attack': 90, 'defense': 100, 'speed': 40},
    'Krabby': {'name': 'Krabby', 'element': 'Water', 'health': 130, 'attack': 105, 'defense': 90, 'speed': 50},
    'Traumato': {'name': 'Traumato', 'element': 'Ghost', 'health': 165, 'attack': 95, 'defense': 70, 'speed': 55},
    'Muschas': {'name': 'Muschas', 'element': 'Water', 'health': 140, 'attack': 50, 'defense': 100, 'speed': 40},
    'Selima': {'name': 'Selima', 'element': 'Water', 'health': 140, 'attack': 60, 'defense': 60, 'speed': 65},
    'Jurob': {'name': 'Jurob', 'element': 'Psychic', 'health': 140, 'attack': 70, 'defense': 55, 'speed': 45},

}


POKEMON_ATTACK = {
    'Normal': {'tackle': {'Attack_Strength': 30, 'Accuracy': 100, 'element': 'Normal'},
               'Backpfeife': {'Attack_Strength': 50, 'Accuracy': 80, 'element': 'Normal'},
               'Bitch_Slap': {'Attack_Strength': 70, 'Accuracy': 60, 'element': 'Normal'},
               'MEME-BEAM': {'Attack_Strength': 4000000, 'Accuracy': 100, 'element': 'Normal'}, },
    'Water': {'Water_Gun': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Water'},
              'Wet-Fart': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Water'},
              'Nasses-Handtuch': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Water'}},
    'Fire': {'Ember': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Fire'},
             'Deo+Feuerzeug': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Fire'},
             'Indisches_Chili': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Fire'}},
    'Grass': {'Vine_Whip': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Grass'},
              'Brenneseln': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Grass'},
              'Kastanien_Attentat': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Grass'}},
    'Ice': {'Hirnfrost': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Ice'},
              'Zunge am Eiszapfen': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Ice'},
              'Kalte-Schulter': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Ice'}},
    'Electric': {'Wolldecke': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Electric'},
              'Magnet_Wurf': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Electric'},
              'Benjamin_Franklin': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Electric'}},
    'Rock': {'Paper': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Rock'},
              'Rock': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Rock'},
              'Scissor': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Rock'}},
    'Ground': {'Schlagloch': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Ground'},
             'Treppenstufe': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Ground'},
             'Quicksand': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Ground'}},
    'Fighting': {'Flex': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Fighting'},
             'Ich_hab_Beine_Trainiert': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Fighting'},
             'Flugstunde': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Fighting'},
            'Saitama-Punch': {'Attack_Strength': 4000000, 'Accuracy': 100, 'element': 'Fighting'}},
    'Poison': {'5-Sekunden-Regel': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Poison'},
               'Burrito_aftermath': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Poison'},
               'Australien': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Poison'}},
    'Flying': {'"Meins!"': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Flying'},
               'Bio-Bomben-Abwurf': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Flying'},
               'Kamikaze': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Flying'}},
    'Psychic': {'Socialmedia': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Psychic'},
               'Trump': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Psychic'},
               'Skibidi-Toilett': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Psychic'}},
    'Bug': {'nächtliche_Mücke': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Bug'},
               'unsichtbares Spinnennetz': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Bug'},
               'Wespen. Einfach drecks Wespen.': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Bug'}},
    'Ghost': {'Boo': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Ghost'},
               'Sleep_Paralysis_Demon': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Ghost'},
               'Warte_mal_die_Tür_war_zu!': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Ghost'}},
    'Dragon': {'Lets go Hicks! Punch!': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Dragon'},
               'Internet_Scalie': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Dragon'},
               'Deine_Mudda': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Dragon'}},
    'Dark': {'I_can_Fix_her!': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Dark'},
               'Goth_Mommy': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Dark'},
               'Darf_ich_nicht_schreiben_sonst_werde_ich_gefeuert': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Dark'}},
    'Steel': {'Balls of Steel': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Steel'},
               'Stahlkappen_Tritt': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Steel'},
               'Car_keyn': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Steel'}},
    'Fairy': {'Winx_Club_Team': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Fairy'},
              'Hey_Listen!': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Fairy'},
              'Zahnfee_Dwayne': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Fairy'}}
}
ELEMENT_TYPE = {
    'Normal': {
        'Normal': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 1,
        'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1,
        'Bug': 1, 'Rock': 0.5, 'Ghost': 0, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1
    },
    'Fire': {
        'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Electric': 1, 'Ice': 2,
        'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1,
        'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 2, 'Fairy': 1
    },
    'Water': {
        'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Electric': 1, 'Ice': 1,
        'Fighting': 1, 'Poison': 1, 'Ground': 2, 'Flying': 1, 'Psychic': 1,
        'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1, 'Fairy': 1
    },
    'Grass': {
        'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Electric': 1, 'Ice': 1,
        'Fighting': 1, 'Poison': 0.5, 'Ground': 1, 'Flying': 0.5, 'Psychic': 1,
        'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel':0.5, 'Fairy': 1
    },
    'Electric': {
        'Normal': 1, 'Fire': 1, 'Water': 2, 'Grass': 0.5, 'Electric': 0.5, 'Ice': 1,
        'Fighting': 1, 'Poison': 1, 'Ground': 0, 'Flying': 2, 'Psychic': 1,
        'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1, 'Fairy': 1
    },
    'Ice': {
        'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Electric': 1, 'Ice': 0.5,
        'Fighting': 1, 'Poison': 1, 'Ground': 0.5, 'Flying': 0.5, 'Psychic': 1,
        'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1
    },
    'Fighting': {
        'Normal': 2, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 2,
        'Fighting': 1, 'Poison': 0.5, 'Ground': 1, 'Flying': 0.5, 'Psychic': 0.5,
        'Bug': 0.5, 'Rock': 2, 'Ghost': 0, 'Dragon': 1, 'Dark': 2, 'Steel': 2, 'Fairy': 0.5
    },
    'Poison': {
        'Normal': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 2, 'Ice': 1,
        'Fighting': 1, 'Poison': 0.5, 'Ground': 0.5, 'Flying': 1, 'Psychic': 1,
        'Bug': 1, 'Rock': 0.5, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 1, 'Steel': 0, 'Fairy': 2
    },
    'Ground': {
        'Normal': 1, 'Fire': 2, 'Water': 1, 'Grass': 0.5, 'Electric': 2, 'Ice': 1,
        'Fighting': 1, 'Poison': 2, 'Ground': 1, 'Flying': 0, 'Psychic': 1,
        'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 2, 'Fairy': 1
    },
    'Flying': {
        'Normal': 1, 'Fire': 1, 'Water': 1, 'Grass': 2, 'Electric': 0.5, 'Ice': 1,
        'Fighting': 2, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1,
        'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1
    },
    'Psychic': {
        'Normal': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 1,
        'Fighting': 2, 'Poison': 2, 'Ground': 1, 'Flying': 1, 'Psychic': 0.5,
        'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 0, 'Steel': 0.5, 'Fairy': 1
    },
    'Bug': {
        'Normal': 1, 'Fire': 0.5, 'Water': 1, 'Grass': 2, 'Electric': 1, 'Ice': 1,
        'Fighting': 0.5, 'Poison': 0.5, 'Ground': 1, 'Flying': 0.5, 'Psychic': 2,
        'Bug': 1, 'Rock': 1, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 2, 'Steel': 0.5, 'Fairy': 0.5
    },
    'Rock': {
        'Normal': 1, 'Fire': 2, 'Water': 1, 'Grass': 1, 'Electric': 2, 'Ice': 2,
        'Fighting': 0.5, 'Poison': 1, 'Ground': 0.5, 'Flying': 2, 'Psychic': 1,
        'Bug': 2, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1
    },
    'Ghost': {
        'Normal': 0, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 1,
        'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 2,
        'Bug': 1, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 0.5, 'Steel': 1, 'Fairy': 1
    },
    'Dragon': {
        'Normal': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 1,
        'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1,
        'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5, 'Fairy': 0
    },
    'Dark': {
        'Normal': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 1,
        'Fighting': 1, 'Poison': 0.5, 'Ground': 1, 'Flying': 1, 'Psychic': 2,
        'Bug': 1, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 0.5, 'Steel': 1, 'Fairy': 0.5
    },
    'Steel': {
        'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Grass': 1, 'Electric': 0.5, 'Ice': 2,
        'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1,
        'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 2
    },
    'Fairy': {
        'Normal': 1, 'Fire': 0.5, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 1,
        'Fighting': 2, 'Poison': 0.5, 'Ground': 1, 'Flying': 1, 'Psychic': 1,
        'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 2, 'Steel': 0.5, 'Fairy': 1
    }
}

POKEMON_ATTACK_VALUES = {
               'tackle': {'Attack_Strength': 30, 'Accuracy': 100, 'element': 'Normal'},
               'Backpfeife': {'Attack_Strength': 50, 'Accuracy': 80, 'element': 'Normal'},
               'Bitch_Slap': {'Attack_Strength': 70, 'Accuracy': 60, 'element': 'Normal'},
               'MEME-BEAM': {'Attack_Strength': 4000000, 'Accuracy': 100, 'element': 'Normal' },
               'Water_Gun': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Water'},
               'Wet-Fart': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Water'},
               'Nasses-Handtuch': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Water'},
               'Ember': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Fire'},
               'Deo+Feuerzeug': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Fire'},
               'Indisches_Chili': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Fire'},
               'Vine_Whip': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Grass'},
               'Brenneseln': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Grass'},
               'Kastanien_Attentat': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Grass'},
               'Hirnfrost': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Ice'},
               'Zunge am Eiszapfen': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Ice'},
               'Kalte-Schulter': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Ice'},
               'Wolldecke': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Electric'},
               'Magnet_Wurf': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Electric'},
               'Benjamin_Franklin': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Electric'},
               'Paper': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Rock'},
               'Rock': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Rock'},
               'Scissor': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Rock'},
               'Schlagloch': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Ground'},
               'Treppenstufe': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Ground'},
               'Quicksand': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Ground'},
               'Flex': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Fighting'},
               'Ich_hab_Beine_Trainiert': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Fighting'},
               'Flugstunde': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Fighting'},
               'Saitama-Punch': {'Attack_Strength': 4000000, 'Accuracy': 100, 'element': 'Fighting'},
               '5-Sekunden-Regel': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Poison'},
               'Burrito_aftermath': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Poison'},
               'Australien': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Poison'},
               '"Meins!"': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Flying'},
               'Bio-Bomben-Abwurf': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Flying'},
               'Kamikaze': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Flying'},
               'Socialmedia': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Psychic'},
               'Trump': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Psychic'},
               'Skibidi-Toilett': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Psychic'},
               'nächtliche_Mücke': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Bug'},
               'unsichtbares Spinnennetz': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Bug'},
               'Wespen. Einfach drecks Wespen.': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Bug'},
               'Boo': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Ghost'},
               'Sleep_Paralysis_Demon': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Ghost'},
               'Warte_mal_die_Tür_war_zu!': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Ghost'},
               'Lets go Hicks! Punch!': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Dragon'},
               'Internet_Scalie': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Dragon'},
               'Deine_Mudda': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Dragon'},
               'I_can_Fix_her!': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Dark'},
               'Goth_Mommy': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Dark'},
               'Darf_ich_nicht_schreiben_sonst_werde_ich_gefeuert': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Dark'},
               'Balls of Steel': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Steel'},
               'Stahlkappen_Tritt': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Steel'},
               'Car_keyn': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Steel'},
               'Winx_Club_Team': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Fairy'},
               'Hey_Listen!': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Fairy'},
               'Zahnfee_Dwayne': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Fairy'}