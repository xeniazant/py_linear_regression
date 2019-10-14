#
# Linear Regression calc by Xenia Zantello
#

import tkinter

# take user input? and put in list or tuples?
from typing import List


def points_in():
    return

# index through list and construct function to minimize
def make_function():
    return

# Algorithm that minimizes the function. Binary search?
def find_fit():
    return



#--------main code below, calling previous functions to determine best fit--------
print("Please enter a set of ordered pairs.")
points = input()
new_points = points.replace(",", "")
points_list = new_points.split(" ")
for p in points_list:
    p = int(p)
print(points_list)
points_set = zip(*points_list)

print(set(points_set))



print("Values entered were: ", points)

# tkinter ui window

m = tkinter.Tk()
m.mainloop()


