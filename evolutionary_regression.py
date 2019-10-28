#
# Evolutionary Linear Regression calc by Xenia Zantello
#

import tkinter
import random


# take user input? and put in list or tuples?
# from typing import List
gen_counter = 0

class Line:
    def __init__(self, slope, constant):
        self.slope = slope
        self.constant = constant

    def print_equation(self):
        print("y = ", self.slope, "x + ", self.constant)


# points will be a list of 2-tuples of ints
def sum_deviation_squared(points, line):
    """Returns the sum for all given values of the deviation squared between"""
    """expected and actual value"""
    sum = 0
    for i in points:
        difference_sqrd = (i[1] - (i[0] * line.slope + line.constant)) ** 2
        sum += difference_sqrd
    return sum


# index through list and construct function to minimize
def new_child(parent_line):
    """Takes the last generations best child and generates a new, similar child"""
    new_child_slope = parent_line.slope + 1 * random.uniform(0, 1.5)
    new_child_constant = parent_line.constant + 1 * random.uniform(0, 1.5)
    child = Line(new_child_slope, new_child_constant)
    return child


def new_generation(parent_line):
    """Calls new_child n times to create a new generation of offspring functions related to parent"""
    print("Generation: ", gen_counter)
    child_1 = new_child(parent_line)
    child_2 = new_child(parent_line)
    child_3 = new_child(parent_line)
    gen_counter += 1
    return [child_1, child_2, child_3]


def choose_heir(points, children):
    """Chooses 'heir' to survive and parent next generation"""
    minimum_error = None
    best_child = None
    for child in children:
        if minimum_error is None:
            minimum_error = sum_deviation_squared(points, child)
            best_child = child
        elif sum_deviation_squared(points, child) < minimum_error:
            minimum_error = sum_deviation_squared(points, child)
            best_child = child

    return best_child

# --------playing with tKinter--------


# print("Please enter a set of ordered pairs.")
# points = input()
# new_points = points.replace(",", "")
# points_list = new_points.split(" ")
# for p in points_list:
#     #p = int(p)
# print(points_list)
# points_set = zip(*points_list)
#
# print(set(points_set))
#
# print("Values entered were: ", points)
#
# # tkinter ui window
#
# m = tkinter.Tk()
# m.message("blarg")
# m.mainloop()
