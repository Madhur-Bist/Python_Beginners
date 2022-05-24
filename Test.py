# Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

print ("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are");

# Write a Python program to get the Python version you are using. 
import sys;
print ("Python version:", sys.version);

# Write a Python program to display the current date and time.
import datetime;
print (datetime.datetime.now());

#  Write a Python program which accepts the radius of a circle from the user and compute the area.
import math;
radius = float(input("Enter the radius of the circle: "));
area = math.pi * radius ** 2;
print ("Area of the circle: ", area);
