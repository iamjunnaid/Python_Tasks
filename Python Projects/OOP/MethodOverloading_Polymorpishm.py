'''
Method Overloading

The process of the calling the same method with the different parameters

'''

class Shape:

    # function with two default parameters
    def area(self,a,b=0):
        if b>0:
            print('The area of the Rectangle is: ',a*b)
        else:
            print('Area of the Square is: ', a*a)

square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(5,6)
