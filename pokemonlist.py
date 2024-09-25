import pygame

POKEMON_DATA = {
    'Charmander':  {'name': 'Charmander', 'element': 'Fire', 'health': 188, 'attack': 112, 'defense': 94, 'speed': 122},
    'Bulbasaur': {'name': 'Bulbasaur', 'element': 'Grass', 'health': 200, 'attack': 121, 'defense': 121, 'speed': 85},
    'Squirtle': {'name': 'Squirtle', 'element': 'Water', 'health': 198, 'attack': 94, 'defense': 121, 'speed': 81}
}
POKEMON_ATTACK = {
    'normal': {'tackle': {'Attack_Strength': 30, 'Accuracy': 100, 'element': 'normal'}, 'MEME-BEAM': {'Attack_Strength': 4000000, 'Accuracy': 100, 'element': 'Normal'}, },
    'Water': {'Water_Gun': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Water'},'Wet-Fart': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Water'}, 'Nasses-Handtuch': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Water'}, },
    'Fire': {'Ember': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Fire'}, 'Deo+Feuerzeug': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Fire'}, 'Indisches_Chili': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Fire'} },
    'Grass': {'Vine_Whip': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'Grass'}, 'Brenneseln': {'Attack_Strength': 60, 'Accuracy': 80, 'element': 'Grass'}, 'Kastanien_Attentat': {'Attack_Strength': 80, 'Accuracy': 60, 'element': 'Grass'} },
}
ELEMENT_TYPE = {
    'Fire': {'Fire': 1, 'Grass': 2, 'Water': 0.5, 'Normal': 1},
    'Water': {'Fire': 2, 'Grass': 0.5, 'Water': 1, 'Normal': 1},
    'Plant': {'Fire': 0.5, 'Grass': 1, 'Water': 2, 'Normal': 1}
}


