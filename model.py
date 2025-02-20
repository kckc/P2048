import random

def dot(arr1, arr2):
  if len(arr1) != len(arr2):
    raise ValueError()
  sum = 0
  for i in range(len(arr1)):
    sum += arr1[i] * arr2[i]
  return sum
def scale(arr, factor):
  return [i*factor for i in arr]
  
class Model():
  def _init__(self, model):
    self.gen = 0
    self.left = [random.random()]*16
    self.right = [random.random()]*16
    self.up = [random.random()]*16
    self.down = [random.random()]*16
    if model is not None:
      self.left = model.left
      self.right = model.right
      self.up = model.up
      self.down = model.down
      self.gen = model.gen + 1
  def run(self, state):
    if len(state) != 16:
      raise ValueError()
    # scale the states
    # multiply state with l,r,u,d
    # normalize weights
    # return highest value
    # l->0,r->1,u->2,d->3
    max_state_val = max(state)
    scaled_state = scale(state,1/max_state_val)
    probs = [
      dot(scaled_state, self.left),
      dot(scaled_state, self.right),
      dot(scaled_state, self.up),
      dot(scaled_state, self.down),
    ]
    max_i = 0
    for i in range(1,4):
      if probs[i] > probs[max_i]:
        max_i = i
    return max_i
    
  def learn(self, action, feedback):
    # find weights from action
    # if feedback + then = 
    return