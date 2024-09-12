import pygame

POKEMON_DATA = {
    'Charmander':  {'name': 'Charmander','element': 'fire', 'health': 188, 'attack': 112, 'defense': 94, 'speed': 122},
    'Bulbasaur': {'name': 'Bulbasaur','element': 'plant', 'health': 200, 'attack': 121, 'defense': 121, 'speed': 85},
    'Squirtle': {'name': 'Squirtle','element': 'water', 'health': 198, 'attack': 94, 'defense': 121, 'speed': 81}
}
POKEMON_ATTACK = {
    'Water_Gun': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'water'},
    'Ember': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'fire'},
    'Vine_Whip': {'Attack_Strength': 40, 'Accuracy': 100, 'element': 'plant'}
}
ELEMENT_TYPE = {
    'Fire': {'fire': 1, 'plant': 2, 'water': 0.5, 'normal': 1},
    'water': {'fire': 2, 'plant': 0.5, 'water': 1, 'normal': 1},
    'plant': {'fire': 0.5, 'plant': 1, 'water': 2, 'normal': 1}
}