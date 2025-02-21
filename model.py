import random
from layer import FullyConnectedLayer

def dot(arr1, arr2):
  if len(arr1) != len(arr2):
    raise ValueError()
  sum = 0
  for i in range(len(arr1)):
    sum += arr1[i] * arr2[i]
  return sum
def scale(arr, factor):
  return [i*factor for i in arr]

def normalise(arr):
  return scale(arr, 1/max(arr))
  
class AllConnectedModel():
  def __init__(self, model = None):
    self.learning_rate = 0.1
    self.gen = 0
    self.l1 = FullyConnectedLayer(16, 8)
    self.l2 = FullyConnectedLayer(8, 4)
  def run(self, input):
    if len(input) != 16:
      raise ValueError()
    probs =  self.l2.forward(self.l1.forward(input))
    max_i = 0
    for i in range(1,4):
      if probs[i] > probs[max_i]:
        max_i = i
    return max_i
    
  def learn(self, input, action, feedback):
    # find weights from action
    # if feedback 0, reduce weight, if + increase weight by the feedback
    # normalise weight
    
    d1 = [self.learning_rate * (feedback - 0.5) if i == action else self.learning_rate for i in range(4)]
    back1 = self.l2.backward(d1)
    d2 = [back1[i] - self.l1.output[i] for i in range(len(back1)) ]
    back2 = self.l1.backward(d2)
    return

class RandomModel():
  def run(self,_):
    return random.randint(0,3)
  def learn(self, _,__,___):
    pass

class UserModel():
  user_input_map = {
    'l':0,
    'r':1,
    'u':2,
    'd':3,
  }
  def run(self, _):
    user_input = input("""
    choose a direction:
    up[u] down[d] left[l] right[r]
    """)
    if user_input not in UserModel.user_input_map:
      print("Invalid input")
      self.run(_)
    else:
      return UserModel.user_input_map[user_input]
  def learn(self, _,__,___):
    pass