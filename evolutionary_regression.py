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

    def equation_to_string(self):
        return "y = " + str(self.slope) + "x + " + str(self.constant)


# points will be a list of 2-tuples of ints
def sum_deviation_squared(points, line):
    """Returns the sum for all given values of the deviation squared between"""
    """ expected and actual value"""
    current_sum = 0
    for i in points:
        difference_sqrd = (i[1] - (i[0] * line.slope + line.constant)) ** 2
        current_sum += difference_sqrd
    return current_sum


# index through list and construct function to minimize
def new_child(parent_line):
    """Takes the last generations best child and generates a new, similar child"""
    new_child_slope = (parent_line.slope + 1) * random.random()
    new_child_constant = (parent_line.constant + 1) * random.random()
    child = Line(new_child_slope, new_child_constant)
    return child


def new_generation(parent_line):
    """Calls new_child n times to create a new generation of offspring functions related to parent"""
    child_1 = new_child(parent_line)
    child_2 = new_child(parent_line)
    child_3 = new_child(parent_line)
    child_4 = new_child(parent_line)
    child_5 = new_child(parent_line)
    return [child_1, child_2, child_3, child_4, child_5]


def choose_heir(points, children, parent):
    """Chooses 'heir' to survive and parent next generation"""
    minimum_error = sum_deviation_squared(points, parent)
    best_child = parent
    for child in children:
        if sum_deviation_squared(points, child) < minimum_error:
            minimum_error = sum_deviation_squared(points, child)
            best_child = child

    return best_child


def evolutionary_linreg(points, num_generations):
    parent_line = Line(45, 8)
    gen_counter = 0
    # parent line is assigned an arbitrary linear starting point

    while gen_counter < num_generations:
        generation = new_generation(parent_line)
        parent_line = choose_heir(points, generation, parent_line)
        print("Generation: ", gen_counter, "Best line:", parent_line.equation_to_string(),
              "Deviation squared: ", sum_deviation_squared(points, parent_line))
        gen_counter += 1


points = [(1, 1), (2, 3), (3, 3)]
points_1 = [(2, 8), (5.1, 7.9), (4, 10), (6, 14), (10, 12), (12, 16)]

evolutionary_linreg(points, 40)

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
