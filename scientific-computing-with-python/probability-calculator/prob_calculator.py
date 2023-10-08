import copy
import random
# Consider using the modules imported above.


class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      for i in range(count):
        self.contents.append(color)
    print(self.contents)

  def draw(self, num_balls_to_draw):
    if num_balls_to_draw >= len(self.contents):
      drawn_balls = self.contents[:]
      self.contents.clear()
      return drawn_balls

    drawn_balls = random.sample(self.contents, num_balls_to_draw)
    for ball in drawn_balls:
      self.contents.remove(ball)
    
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  flag = 0
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)

    match = all(drawn_balls.count(color) >= count for color, count in expected_balls.items())

    if match:
      flag += 1

  probability = flag / num_experiments
  return probability

