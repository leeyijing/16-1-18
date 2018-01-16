class uobitems:
    def __init__(self,item, type, points,image,width,height):
        self.__item = item
        self.__type = type
        self.__points = points
        self.__image = image
        self.__width = width
        self.__height = height
        self.__quantity = 0

    def get_item(self):
        return self.__item

    def get_type (self):
        return self.__type

    def get_points(self):
        return self.__points

    def get_quantity(self):
        return self.__quantity

    def get_image(self):
        return self.__image

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_item(self, item):
        self.__item = item

    def set_type(self, type):
        self.__type = type

    def set_points(self, points):
        self.__points = points

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_image(self, image):
        self.__image = image

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height
 #   def totalitem_pts(self):
  #      return self.__points * self.__quantity







