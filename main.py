import random
from game import Game
from model import AllConnectedModel, RandomModel, UserModel
from layer import Node, Layer

l1 = Layer(16, 16)
for n in l1.inlayer:
    n.value = 0.5
l1.print()
l2 = Layer(16, 4, l1.outlayer)

exp = [0,1,0,0]

for i in range(2):
  print("----------------------")
  l2.forward()
  l2.backward(exp)
  l2.print()
  print([l.value for l in l2.outlayer])

def main():
  m = AllConnectedModel()
  def play(model):
    print("New Game")
    g = Game()
    while not g.finished():
      g.print()
      # g.wait()
      # g.action(
      # random.choice([0,1,2,3]))
      # inpt = [v - 0.5 for v in g.state]
      inpt = g.state
      a = model.run(inpt)
      score_diff = g.action(a)
      m.learn(inpt, a, score_diff)
    g.print()
    print(
        f"Game finished, moves: {g.moves}, score: {g.score}, max: {max(g.state)} "
    )
  
  for i in range(10):
    play(UserModel())

# while game not finished
# if prev state != curr state
#    randomly add a 2 in a 0
# print grid
# wait for input
# left:
#   remove 0 on left side, if same number then add it
