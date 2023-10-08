class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)

  def get_picture(self):
    shape = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    for i in range(self.height):
      shape += self.width * "*"
      shape += "\n"
    return shape

  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):

  def __init__(self, length):
    super().__init__(length, length)

  def __str__(self):
    return "Square(side={})".format(self.width)

  def set_side(self, length):
    self.width = length
    self.height = length

