# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with a variabale name and the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions print out and store the data in the cube (translate, rotate, scale and color)

2. CREATE 3 cube objects with different names (use __init__(name)).

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats: e.g. [1.2, 2.4 ,3.7]
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your cube class.
   Update the cube class to not repeat the content of Object.

NOTE: Upload only the final result.


"""


class Cube:
   #Attributes 
   name = ""

   def __init__(self, name):
      self._name = name

   def translate(self, x, y, z):
      print("translate:({}, {}, {})".format(x, y, z))
       
   def rotate(self, x, y, z):
      print("rotate:({} ,{} ,{})".format(x, y, z))

   def scale(self, x, y, z):
      print("scale:({} {} {})".format(x, y, z))

   def color(self, R, G, B):
      print("color:({} ,{}, {})".format(R, G, B))

   def print_status(self):
      print ("{}".format(self._name))
      self.color(8, 125, 80)
      
   
   def update_transform(self, ttype, value):
      if ttype == "translate":
         self.translate(value[0], value[1], value[2])
      elif ttype == "rotate":
         self.rotate(value[0], value[1], value[2])
      elif ttype == "scale":
         self.scale(value[0], value[1], value[2])


# test only
"""
cube_one = Cube(name="Cube_one")
cube_two = Cube(name="Cube_two")
cube_three = Cube(name="Cube_three")

cube_one.print_status()
cube_one.update_transform("translate", value=[0.1, 0.2, 0.3])
cube_two.print_status()
cube_three.print_status()
"""

class CubeChild(Cube):
   name = "CubeChild"
   translate = [1.0, 4.0, 5.0]
   rotate = [0.0, 90.0, 0.0]
   scale =[1.0, 2.0, 1.0]

   def __init__(self, child_name = name, trans= translate, rot = rotate, scl = scale):
      print("<<<<<<>>>>>>>")
      print("This is children of Cube Class")
      cube_parent = Cube(name = child_name)
      cube_parent.print_status()

      cube_parent.update_transform("translate", trans)
      cube_parent.update_transform("rotate", rot)
      cube_parent.update_transform("scale", scl)



#child class data to the parent class
cube_data = CubeChild()

