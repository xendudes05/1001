from random import randint
from time import sleep
from data import *
from service import *


name = input('Введите своё имя: ')
player['name'] = name
current_enemy = 0


while True:
    action = input('''Выберите действие:
                   1 - бой
                   2 - тренировка
                       ''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == '2':
        training_type = input('Ваша фраза')
        training(training_type)
