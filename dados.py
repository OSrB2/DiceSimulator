from random import randint
from time import sleep
from operator import itemgetter

jogo = {'player 1': randint(1, 6),
        'player 2': randint(1, 6),
        'player 3': randint(1, 6),
        'player 4': randint(1, 6),
        }

ranking = list()

print('Values drawn')

for k, v in jogo.items():
  print(f'{k} took {v} the dice.')
  sleep(1)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)

print('-=' * 30)
print('== player ranking ==')

for i, v in enumerate(ranking):
  print(f'{i + 1}º place: {v[0]} with {v[1]}.')
  sleep(1)