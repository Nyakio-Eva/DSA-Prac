"""
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "White", or "Yellow", or "Purple", or "Red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"

initialize a counter to keep track of the objects instances
initialize the array of color attritubes to be given to the object instance at random

"""
class Ghost:
    _counter = 0
    
    
    def __init__(self):
        
        colors = ["White", "Yellow", "Red", "Purple"]
        
        # logic for randomizing the colors for each object instance 
        """Use the class counter to cycle the colors through the objects"""
        Ghost._counter += 1
        random_index = Ghost._counter % len(colors)
        
        """Assign the color at the index"""
        self.color = colors[random_index]
        
        
object1 = Ghost()   
print(object1.color)

        
    
   