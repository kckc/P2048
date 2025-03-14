import random
import os

up_map = {
  0:0,
  1:4,
  2:8,
  3:12,
  4:1,
  5:5,
  6:9,
  7:13,
  8:2,
  9:6,
  10:10,
  11:14,
  12:3,
  13:7,
  14:11,
  15:15,
}
down_map = {
  0:15,
  1:11,
  2:7,
  3:3,
  4:14,
  5:10,
  6:6,
  7:2,
  8:13,
  9:9,
  10:5,
  11:1,
  12:12,
  13:8,
  14:4,
  15:0,
}
right_map = {
  0:3,
  1:2,
  2:1,
  3:0,
  4:7,
  5:6,
  6:5,
  7:4,
  8:11,
  9:10,
  10:9,
  11:8,
  12:15,
  13:14,
  14:13,
  15:12,
}

def check_no_move(state):
  if len(state) != 16:
    raise ValueError()
  return all(state[i]!=state[i+1] for i in [0,1,2,4,5,6,8,9,10,12,13,14])
    
ADD_RATE = 0.7

user_input_map = {
  'l':0,
  'r':1,
  'u':2,
  'd':3,
}
class Game():
  def __init__(self):
    self.prev_state = [1] * 16
    self.state = [0] * 16
    self.score = 0
    self.moves = 0
    self.state[
      random.randint(0,15)] = 2
  def print(self, state=None):
    #os.system("clear")
    if state is None:
      state = self.state
    print("+" + "----+"*4)
    for i in range(4):
      str = "|"
      for j in range(4):
        str += "%4s|" % state[4*i+j]
      print(str)
      print("+" + "----+"*4)
  def add(self):
    if not all(self.prev_state[i] == self.state[i] for i in range(16)):
      self.moves += 1
      zeros = [i for i,j in enumerate(self.state) if j == 0]
      if len(zeros) and random.random() < ADD_RATE:
        # print("Add Number")
        self.state[random.choice(zeros)] = 2
      else:
        pass # print("No Add")
      self.prev_state = list(self.state)
    else:
      pass # print("NO ACTION")
  def finished(self):
    no_zero = all(num != 0 for num in self.state)
    no_horizontal_move = check_no_move(self.state)
    trans = [self.state[up_map[i]] for i in range(16)]
    no_vert_move = check_no_move(trans)
    # print(f"No 0:{no_zero}, No h: {no_horizontal_move}, No v: {no_vert_move}")
    return no_zero and no_horizontal_move and no_vert_move
  def wait(self):
    user_input = input("""
    choose a direction:
    up[u] down[d] left[l] right[r]
    """)

    if user_input not in user_input_map:
      print("Invalid input")
      self.wait()
    else:
      self.action(user_input_map[user_input])
  def action(self, action):
    start_score = self.score
    match action:
      case 0:
        # print("LEFT")
        self.left()
      case 1:
        # print("RIGHT")
        self.right()
      case 2:
        # print("UP")
        self.up()
      case 3:
        # print("DOWN")
        self.down()
      case _:
        print("Invalid Action")
    self.add()
    return self.score - start_score
  def left(self):
    self.state = self.reduce_grid(self.state)
  def right(self):
    self.state = self.trans_reduce(right_map)
  def up(self):
    self.state = self.trans_reduce(up_map)
  def down(self):
    self.state = self.trans_reduce(down_map)
  def trans_reduce(self, map):
    trans = [self.state[map[i]] for i in range(16)]
    reduced = self.reduce_grid(trans)
    return [reduced[map[i]] for i in range(16)]
  def reduce_grid(self, grid):
    newstate = []
    for i in range(4):
      row = grid[4*i:4*i+4]
      [newstate.append(i) for i in self.reduce_row(row)]
    return newstate
  def reduce_row(self, row):
    nums = [i for i in row if i != 0]
    if len(nums) == 0:
      return [0] * 4
    elif len(nums) == 1:
      return [nums[0],0,0,0]
    else:
      out = []
      while nums:
        num = nums.pop(0)
        if nums and num == nums[0]:
          out.append(num*2)
          self.score += num*2
          nums.pop(0)
        else:
          out.append(num)
      return [out[i] if i < len(out) else 0 for i in range(4)]
      