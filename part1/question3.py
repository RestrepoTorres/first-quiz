################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

class oven:
  def __init__(self):
     self.items = []
     self.output = 'Nothing worth'
     self.temperature = 0
    
  def add(self,item):
    self.items.append(item)
  
  def freeze(self):
    print('lowering temperature...')
    self.wait()
    if(self.items == ['water', 'air'] and self.get_temperature() == -100):
      self.output ='snow'

  def boil(self):
    print('raising temperature...')
    self.wait()
    if(self.items == ['lead', 'mercury'] and self.get_temperature() == 5000):
      self.output ='gold'
    if(self.items == ['cheese', 'dough', 'tomato'] and self.get_temperature() == 150):
      self.output ='pizza'
  
  def wait(self):
    print('mixing ingredients...')
    print('ingredients mixed')

  
  def set_temperature(self, temperature):
    self.temperature = temperature

  def get_temperature(self):
    return self.temperature
  
  def set_output(self):
    return 
  def get_output(self):
    return self.output

# This function should return an oven instance!
def make_oven():
  return oven()

def alchemy_combine(oven, ingredients, temperature):
  oven.set_temperature(temperature)
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()