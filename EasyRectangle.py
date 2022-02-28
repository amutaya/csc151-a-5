from graphics import Rectangle, Point

# EasyRectangles are defined by x,y center coordiantes, width, and height
# They can detect if a given point lies inside of themselves

class EasyRectangle(Rectangle):
    # Creates rectangle object of specified width and height
    # centered on point at (x_center,y_center) 
    def __init__(self, x_center, y_center, width, height):
        top_left = Point(x_center - (width/2), y_center - (height/2))
        bottom_right = Point(x_center + (width/2), y_center + (height/2))
        super().__init__(top_left,bottom_right)

    # Returns true if the point lies within rectangle
    def is_in(self, point):
        return self.getP1().getX() <= point.getX() <= self.getP2().getX() and self.getP1().getY() <= point.getY() <= self.getP2().getY()
