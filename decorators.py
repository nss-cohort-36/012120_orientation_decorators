# Decorators: Dress up your functions!

# our decorator
def interior_decorator(func):
  # define a new function inside this function's scope
  def add_curtains():
    func()
    print("now my house has curtains")
  # return the new function
  return add_curtains

# We can decorate a function many times
def landscaper(func):
  def add_trees():
      func()
      print("And I planted 12 maples for shade.")
  return add_trees

# Our function to be decorated can be written like this:
def move_in():
  print("My house was empty, but...")

# And then can be decorated like this:
new_house = interior_decorator(move_in)

# Prints "My house was empty, but...""now my house has curtains"
new_house()

# OR, we can use the @ symbol to leverage the abstraction of the above process, like so:
@interior_decorator
def move_in():
  print("My house was empty, but...")

# Also prints "My house was empty, but...""now my house has curtains"
move_in()

# Pass args! Here's our orignal decorator, but written in a way to handle a decorated function that takes arguments
def interior_decorator(func):
  # define a new function inside this function's scope
  def add_curtains(color):
    if color == "orange":
        color = "ugly-ass"
    func(color)
    print(f"now my house has {color} curtains")
  # return the new function
  return add_curtains

# Now we can define move_in with a parameter.
@interior_decorator
def move_in(color):
  print("My house was empty, but...")

move_in("red")
move_in("orange")
