import random
from game import Game
from model import AllConnectedModel, RandomModel

m = AllConnectedModel()

def play(model):
  print("New Game")
  g = Game()
  while not g.finished():
    # g.print()
    # g.wait()
    # g.action(
      # random.choice([0,1,2,3]))
    inpt = [v - 0.5 for v in g.state]
    a = model.run(inpt)
    score_diff = g.action(a)
    m.learn(inpt, a, score_diff)
    g.print()
  g.print()
  print(f"Game finished, moves: {g.moves}, score: {g.score}, max: {max(g.state)} ")

for i in range(10):
  play(m)


# while game not finished
# if prev state != curr state
#    randomly add a 2 in a 0
# print grid
# wait for input
# left:
#   remove 0 on left side, if same number then add it



