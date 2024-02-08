from cgi import print_environ_usage


class Car(): 
  def __init__(self, color, mark, top_speed):
    self.mark = mark
    self.color = color 
    self.top_speed = top_speed
  def __str__(self): 
    return f"mark = {self.mark}, color = {self.color}, top speed = {self.top_speed}"
  
car1 = Car('black', 'BMW', 300)

print(car1.mark)

print(car1)