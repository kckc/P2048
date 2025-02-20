import random
from game import Game

g = Game()
print("New Game")
while not g.finished():
  g.add()
  g.print()
  
  match random.randint(0,3):
    case 0:
      print("LEFT")
      g.left()
    case 1:
      print("RIGHT")
      g.right()
    case 2:
      print("UP")
      g.up()
    case 3:
      print("DOWN")
      g.down()
  g.print()
print(f"Score: {g.score}")

# while game not finished
# if prev state != curr state
#    randomly add a 2 in a 0
# print grid
# wait for input
# left:
#   remove 0 on left side, if same number then add it



