"""
file: factors.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: generates graph for the data given
"""

from utils import *
import turtle as t

data = read_data(pre_file_name()) # stores MainDct and MetaDct ie, two dictionaries each for \
                                  # maindata and metadata in suitable format

# calling four turtles for convenience
t0 = t.Turtle()
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()

def drawAxes(t):
    """
    draws the axes for the coordinate system
    :param t: the turtle its using
    :return: NONE
    """
    t.speed(0)
    t.pd()
    t.forward(500)
    t.back(500)

def initialCoordinates():
    """
    initial coordinates for the turtle/ coordinates considered as origin
    :return: coordinates of origin
    """
    return (-250,-250)

def setTurtle(t):
    """
    makes turtle go to origin
    :param t: the turtle its using
    :return: NONE
    """
    t.pu()
    t.goto(initialCoordinates())

def drawCoordinatePlane_income():
    """
    draws an appropriate coordinate plane for the first graph
    :return: NONE
    """
    turtle = t.Screen()
    turtle.title("Life Expectancy versus Income Category")
    t2.speed(0)
    t3.speed(0)
    setTurtle(t0)
    setTurtle(t1)
    setTurtle(t2)
    setTurtle(t3)
    drawAxes(t0)
    t1.left(90)
    drawAxes(t1)
    t0.pu()
    t0.fd(-80)
    t0.lt(90)
    drawlabels(t0, t1)
    drawPoints(t0, t1)
    drawIndex_income(t0, t1, t2, t3)
    drawIndexLines_income(t0, t1, t2, t3)
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()
    t0.goto(initialCoordinates())
    t1.goto(initialCoordinates())
    t2.goto(initialCoordinates())
    t3.goto(initialCoordinates())
    t1.lt(90)

def drawCoordinatePlane_region():
    """
    draws an appropriate coordinate plane for the second graph(expectancy vs region)
    :return: NONE
    """
    turtle2 = t.Screen()
    turtle2.title("Life Expectancy versus Region")
    t2.speed(0)
    t3.speed(0)
    setTurtle(t0)
    setTurtle(t1)
    setTurtle(t2)
    setTurtle(t3)
    drawAxes(t0)
    t1.left(90)
    drawAxes(t1)
    t0.pu()
    t0.fd(-80)
    t0.lt(90)
    drawlabels(t0, t1)
    drawPoints(t0, t1)
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()
    t0.goto(initialCoordinates())
    t1.goto(initialCoordinates())
    t2.goto(initialCoordinates())
    t3.goto(initialCoordinates())
    t1.lt(90)

def drawlabels(t, t1):
    """
    draws the labels for coordinate axes
    :param t: the turtle its using for x axis
    :param t1: the turtle its using for y axis
    :return: NONE
    """
    t.fd(250)
    t.pd()
    t.write("Life", font=("Arial", 10, "bold"))
    t.pu()
    t.back(12)
    t.pd()
    t.write("Exp.", font=("Arial", 10, "bold"))
    t.pu()
    t.back(238)
    t.right(90)
    t.fd(80)
    t1.pu()
    t1.back(50)
    t1.rt(90)
    t1.fd(250)
    t1.pd()
    t1.write("Year", font=("Arial", 10, "bold"))
    t1.pu()
    t1.back(250)
    t1.left(90)
    t1.fd(50)


def drawPoints(t, t1):
    """
    draws x and y coordinates on axes
    :param t: the turtle its using for x axis
    :param t1: the turtle its using for y axis
    :return: NONE
    """
    t.pu()
    t.back(20)
    t.left(90)
    t.pd()
    for idx in range(0, 10):
        t.write(idx*10, font = ("Arial", 10, "bold"))
        t.pu()
        t.fd(55)
        idx += 1
    t.pu()
    t.back(550)
    t.rt(90)
    t.fd(20)
    t1.pu()
    t1.back(20)
    t1.right(90)
    t1.pd()
    init = 1960
    for idx in range(0, 2):
        t1.write(init, font = ("Arial", 10, "bold"))
        init += 55
        t1.pu()
        t1.fd(500)
        idx += 1
    t1.pu()
    t1.back(1000)
    t1.lt(90)
    t1.fd(20)

def get_pos0(t):
    """
    position for index
    :param t: the turtle its using to draw the index
    :return: NONE
    """
    t.pu()
    t.fd(40)
    t.lt(90)
    t.fd(580)

def get_pos1(t):
    """
    position for index
    :param t: the turtle its using to draw the index
    :return: NONE
    """
    t.pu()
    t.right(90)
    t.fd(40)
    t.lt(90)
    t.fd(560)

def get_pos2(t):
    """
    position for index
    :param t: the turtle its using to draw the index
    :return: NONE
    """
    t.pu()
    t.fd(40)
    t.lt(90)
    t.fd(540)

def get_pos3(t):
    """
    position for index
    :param t: the turtle its using to draw the index
    :return: NONE
    """
    t.pu()
    t.fd(40)
    t.lt(90)
    t.fd(520)

def drawIndex_income(t0, t1, t2, t3):
    """
    writes the index line labels
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third
    :param t3: fourth
    :return: NONE
    """
    get_pos0(t0)
    t0.pd()
    t0.pencolor("blue")
    t0.write("Low income", font=("Arial", 10, "bold"))
    get_pos1(t1)
    t1.pd()
    t1.pencolor("red")
    t1.write("Upper middle income", font=("Arial", 10, "bold"))
    get_pos2(t2)
    t2.pd()
    t2.pencolor("green")
    t2.write("Lower middle income", font=("Arial", 10, "bold"))
    get_pos3(t3)
    t3.pd()
    t3.pencolor("gold")
    t3.write("High income", font=("Arial", 10, "bold"))
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()
    t0.goto(initialCoordinates())
    t1.goto(initialCoordinates())
    t2.goto(initialCoordinates())
    t3.goto(initialCoordinates())

def drawLines_income(t0, t1, t2, t3):
    """
    draws the reference color lines for the graph
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third
    :param t3: fourth
    :return: NONE
    """
    t0.pd()
    t1.pd()
    t2.pd()
    t3.pd()
    t0.pencolor("blue")
    t0.pensize(3)
    t1.pensize(3)
    t2.pensize(3)
    t3.pensize(3)
    t1.pencolor("red")
    t2.pencolor("green")
    t3.pencolor("gold")
    t0.rt(90)
    t1.rt(90)
    t2.rt(90)
    t3.rt(90)
    t0.fd(70)
    t1.fd(70)
    t2.fd(70)
    t3.fd(70)

def drawIndexLines_income(t0, t1, t2, t3):
    """
    draws the reference color lines for the graph
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third
    :param t3: fourth
    :return: NONE
    """
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()

    t0.rt(90)
    t0.fd(240)
    t0.left(90)
    t0.fd(590)

    t1.rt(90)
    t1.fd(240)
    t1.left(90)
    t1.fd(570)

    t2.rt(90)
    t2.fd(240)
    t2.left(90)
    t2.fd(550)

    t3.rt(90)
    t3.fd(240)
    t3.left(90)
    t3.fd(530)
    drawLines_income(t0, t1, t2, t3)
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()
    t0.goto(initialCoordinates())
    t1.goto(initialCoordinates())
    t2.goto(initialCoordinates())
    t3.goto(initialCoordinates())
    t3.rt(90)

inc_lst = income_list()     # list of income categories
reg_lst = region_list()     # list of regions

def filter_income_graph(data, income):
    """
    filters data of a country based on income category and prints the information
    :param data: the data it's reading from
    :param region: the income category for which its filtering
    :return: dictionary with filtered data based on income categories
    """
    MetaDct = data[1]
    f_MetaDct = {}
    for idx in MetaDct:
        if idx != ',':
            if MetaDct[idx].income == income:
                f_MetaDct[idx] = MetaDct[idx].country
    return f_MetaDct

def filter_region_graph(data, region):
    """
    filters data of a country based on region and prints the information
    :param data: the data it's reading from
    :param region: the region for which its filtering
    :return: dictionary with filtered data based on regions
    """
    MetaDct = data[1]
    f_MetaDct = {}
    for idx in MetaDct:
        if idx != ',':
            if MetaDct[idx].region == region:
                    f_MetaDct[idx] = MetaDct[idx].country
    return f_MetaDct

#   filtered list of incomes
high_countries = list(filter_income_graph(data, inc_lst[0]))
low_countries = list(filter_income_graph(data, inc_lst[1]))
lower_middle_countries = list(filter_income_graph(data, inc_lst[2]))
upper_middle_countries = list(filter_income_graph(data, inc_lst[3]))

#   filtered list of regions
east_asia_pacific = list(filter_region_graph(data, reg_lst[0]))
europe_central_asia = list(filter_region_graph(data, reg_lst[1]))
latin_america = list(filter_region_graph(data, reg_lst[2]))
middle_east = list(filter_region_graph(data, reg_lst[3]))
north_america = list(filter_region_graph(data, reg_lst[4]))
south_asia = list(filter_region_graph(data, reg_lst[5]))
sub_saharan_africa = list(filter_region_graph(data, reg_lst[6]))

def life_expectancy_graph(country_name):
    """
    returns life expectancy for a particular country
    :param country_name: the country its looking expectancy data for
    :return: dictionary with life expectancy data
    """
    dat = read_data(pre_file_name())
    MainDct = dat[0]
    # MetaDct = dat[1]
    f_life_expectancy = {}
    for idx in MainDct:
        if idx == country_name or MainDct[idx].country_code == country_name:
            for idx1 in MainDct[idx].values:
                if idx1[1] != 0:
                    f_life_expectancy[idx1[0]] = idx1[1]
    return f_life_expectancy

def median(thelist):
    """
    returns median of a list
    :param thelist: the list whose median its finding
    :return: median of the list
    """
    sorted_list = sorted(thelist)
    length = len(sorted_list)
    center = length // 2

    if length == 1:
        return sorted_list[0]

    elif length % 2 == 0:
        return sum(sorted_list[center - 1: center + 1]) / 2.0

    else:
        return sorted_list[center]

def high_income_countries():
    """
    returns list of medians of life expectancies of all the years from 1960 to 2015 of high income category of countries
    :return: a list of medians
    """
    high_countries_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in high_countries:
        high_countries_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in high_countries_data:
        if idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def low_income_countries():
    """
    returns list of medians of life expectancies all the years from 1960 to 2015 of low income category of countries
    :return: a list of medians
    """
    low_countries_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in low_countries:
        low_countries_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in low_countries_data:
        if idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def lower_middle_income_countries():
    """
    returns list of medians of life expectancies all the years from 1960 to 2015 of lower middle income category of
    countries
    :return: a list of medians
    """
    lower_middle_countries_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in lower_middle_countries:
        lower_middle_countries_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in lower_middle_countries_data:
        if idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def upper_middle_income_countries():
    """
    returns list of medians of life expectancies all the years from 1960 to 2015 of upper middle income category of
    countries
    :return: a list of medians
    """
    upper_middle_countries_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in upper_middle_countries:
        upper_middle_countries_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in upper_middle_countries_data:
        if idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def income_graph(t0, t1, t2, t3):
    """
    plots the graph for life expectancy vs income category for the years from 1960 to 2015
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third turtle
    :param t3: fourth turtle
    :return: NONE
    """
    medians0 = sorted(high_income_countries())
    t3.goto(-250, ((2.5*medians0[0])-15))
    t3.rt(90)
    for idx in range(1, len(medians0)):
        t3.pd()
        t3.setpos((-250+(idx*8.8)), (2.5*medians0[idx])-25)

    medians1 = sorted(low_income_countries())
    t0.goto(-250, ((2.5 * medians1[0]) - 15))
    t0.rt(90)
    for idx in range(1, len(medians1)):
        t0.pd()
        t0.setpos((-250 + (idx * 16.4)), (2.5 * medians1[idx]) - 25)

    medians2 = sorted(lower_middle_income_countries())
    t2.goto(-250, ((2.5 * medians2[0]) - 15))
    t2.rt(90)
    for idx in range(1, len(medians2)):
        t2.pd()
        t2.setpos((-250 + (idx * 9.8)), (2.5 * medians2[idx]) - 25)

    medians3 = sorted(upper_middle_income_countries())
    t1.goto(-250, ((2.5 * medians3[0]) - 15))
    t1.rt(90)
    for idx in range(1, len(medians3)):
        t1.pd()
        t1.setpos((-250 + (idx * 10.1)), (2.5 * medians3[idx]) - 25)
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()
    t0.goto(initialCoordinates())
    t1.goto(initialCoordinates())
    t2.goto(initialCoordinates())
    t3.goto(initialCoordinates())


def drawIndex_region(t0, t1, t2, t3):
    """
    draws index for different regions
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third turtle
    :param t3: fourth turtle
    :return: NONE
    """
    get_pos0(t0)
    t0.fd(50)
    t0.pd()
    t0.pencolor("blue")
    t0.write("Sub-Saharan Africa", font=("Arial", 10, "bold"))
    t1.rt(90)
    get_pos1(t1)
    t1.fd(50)
    t1.pd()
    t1.pencolor("red")
    t1.write("South Asia", font=("Arial", 10, "bold"))
    get_pos2(t2)
    t2.fd(50)
    t2.pd()
    t2.pencolor("green")
    t2.write("Europe and Central Asia", font=("Arial", 10, "bold"))
    get_pos3(t3)
    t3.fd(50)
    t3.pd()
    t3.pencolor("gold")
    t3.write("Latin America & Caribbean", font=("Arial", 10, "bold"))
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()
    t0.back(80)
    t0.pd()
    t0.pencolor("black")
    t0.write("Middle East and North Africa", font=("Arial", 10, "bold"))
    t1.back(80)
    t1.pd()
    t1.pencolor("yellow")
    t1.write("North America", font=("Arial", 10, "bold"))
    t2.back(80)
    t2.pd()
    t2.pencolor("purple")
    t2.write("East Asia and Pacific", font=("Arial", 10, "bold"))
    t3.goto(initialCoordinates())
    t0.pu()
    t1.pu()
    t2.pu()
    t0.goto(initialCoordinates())
    t1.goto(initialCoordinates())
    t2.goto(initialCoordinates())
    t3.goto(initialCoordinates())

def drawLines_region(t0, t1, t2, t3):
    """
    draws the reference color lines for the graph
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third
    :param t3: fourth
    :return: NONE
    """
    t0.pd()
    t1.pd()
    t2.pd()
    t3.pd()
    t0.pencolor("blue")
    t0.pensize(3)
    t1.pensize(3)
    t2.pensize(3)
    t3.pensize(3)
    t1.pencolor("red")
    t2.pencolor("green")
    t3.pencolor("gold")
    t0.rt(90)
    t1.rt(90)
    t2.rt(90)
    t3.rt(90)
    t0.fd(70)
    t1.fd(70)
    t2.fd(70)
    t3.fd(70)

def drawIndexLines_region(t0, t1, t2, t3):
    """
    draws references for the graph
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third
    :param t3: fourth
    :return: NONE
    """
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()

    t0.rt(90)
    t0.fd(240)
    t0.left(90)
    t0.fd(640)

    t1.rt(90)
    t1.fd(240)
    t1.left(90)
    t1.fd(620)

    t2.rt(90)
    t2.fd(240)
    t2.left(90)
    t2.fd(600)

    t3.rt(90)
    t3.fd(240)
    t3.left(90)
    t3.fd(580)
    drawLines_region(t0, t1, t2, t3)
    t0.pu()
    t1.pu()
    t2.pu()
    t3.pu()
    t0.back(70)
    t1.back(70)
    t2.back(70)
    t0.left(90)
    t1.left(90)
    t2.left(90)
    t0.back(80)
    t1.back(80)
    t2.back(80)
    t0.rt(90)
    t1.rt(90)
    t2.rt(90)
    t0.pd()
    t1.pd()
    t2.pd()
    t0.pencolor("Black")
    t0.back(-70)
    t1.pencolor("yellow")
    t1.back(-70)
    t2.pencolor("purple")
    t2.back(-70)
    t0.pu()
    t1.pu()
    t2.pu()
    t0.goto(initialCoordinates())
    t1.goto(initialCoordinates())
    t2.goto(initialCoordinates())
    t3.goto(initialCoordinates())

def sub_saharan_africa_countries():
    """
    returns a list of medians of life expectancies of a list of countries under Sub Saharan Africa region from 1960 to
    2015
    :return: a list of medians
    """
    sub_saharan_africa_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in sub_saharan_africa:
        sub_saharan_africa_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in sub_saharan_africa_data:
        if idx != None:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def south_asia_countries():
    """
    returns a list of medians of life expectancies of a list of countries under South Asia region from 1960 to
    2015
    :return: a list of medians
    """
    south_asia_countries_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in south_asia:
        south_asia_countries_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in south_asia_countries_data:
        if idx != None:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def europe_central_asia_countries():
    """
    returns a list of medians of life expectancies of a list of countries under Europe and Central Asia region from
    1960 to 2015
    :return: a list of medians
    """
    europe_central_asia_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in europe_central_asia:
        europe_central_asia_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in europe_central_asia_data:
        if idx != None and idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def latin_america_countries():
    """
    returns a list of medians of life expectancies of a list of countries under Latin America region from 1960 to
    2015
    :return: a list of medians
    """
    latin_america_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in latin_america:
        latin_america_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in latin_america_data:
        if idx != None and idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def middle_east_countries():
    """
    returns a list of medians of life expectancies of a list of countries under Middle East region from 1960 to
    2015
    :return: a list of medians
    """
    middle_east_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in middle_east:
        middle_east_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in middle_east_data:
        if idx != None and idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def north_america_countries():
    """
    returns a list of medians of life expectancies of a list of countries under North America region from 1960 to
    2015
    :return: a list of medians
    """
    north_america_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in  north_america:
        north_america_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in  north_america_data:
        if idx != None and idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def east_asia_pacific_countries():
    """
    returns a list of medians of life expectancies of a list of countries under East Pacific region from 1960 to
    2015
    :return: a list of medians
    """
    east_asia_pacific_data = []
    years = []
    medians = []
    lst = []
    for idx in range(1960, 2016):
        years.append(idx)
    for idx in east_asia_pacific:
        east_asia_pacific_data.append(life_expectancy_graph(idx))
    y_idx = 0
    for idx in east_asia_pacific_data:
        if idx != None and idx != {}:
            if (list(idx.keys())[y_idx]) == years[y_idx]:
                lst.append((list(idx.values())[y_idx]))
                lst = sorted(lst)
                medians.append(median(lst))
    return medians

def region_graph(t0, t1, t2, t3):
    """
    plots the graph for life expectancy vs regions for the years from 1960 to 2015
    :param t0: first turtle
    :param t1: second turtle
    :param t2: third turtle
    :param t3: fourth turtle
    :return: NONE
    """
    medians0 = sorted(sub_saharan_africa_countries())
    t0.goto(-250, ((medians0[0])-50))
    t0.rt(90)
    for idx in range(1, len(medians0)):
        t0.pencolor("blue")
        t0.pd()
        t0.setpos((-250+(idx*10.5)), ((medians0[idx])))

    medians1 = sorted(south_asia_countries())
    t1.goto(-250, ((medians1[0]) - 60))
    t1.rt(90)
    for idx in range(1, len(medians1)):
        t1.pencolor("red")
        t1.pd()
        t1.setpos((-250 + (idx * 68.5)), (2*(medians1[idx])+10))

    medians2 = sorted(europe_central_asia_countries())
    t2.goto(-250, (medians2[0])+60)
    t2.rt(90)
    for idx in range(1, len(medians2)):
        t2.pencolor("green")
        t2.pd()
        t2.setpos((-250 + (idx*10.19)), (2 * (medians2[idx]) + 10))

    medians3 = sorted(latin_america_countries())
    t3.goto(-250, (medians3[0]) + 20)
    t3.rt(90)
    for idx in range(1, len(medians3)):
        t3.pencolor("gold")
        t3.pd()
        t3.setpos((-250 + (idx * 14.39)), (2 * (medians3[idx]) + 10))

    t0.pu()
    t0.goto(initialCoordinates())
    t1.pu()
    t1.goto(initialCoordinates())
    t2.pu()
    t2.goto(initialCoordinates())
    t3.pu()
    t3.goto(initialCoordinates())

    medians4 = sorted(middle_east_countries())
    t0.goto(-250, (medians4[0])-40)
    t0.rt(90)
    for idx in range(1, len(medians4)):
        t0.pencolor("BLACK")
        t0.pd()
        t0.setpos((-250 + (idx * 26.3)), (2 * (medians4[idx]) + 10))
        t0.rt(180)

    medians5 = sorted(north_america_countries())
    t1.goto(-250, (medians5[0])+60)
    t1.rt(90)
    for idx in range(1, len(medians5)):
        t1.pencolor("YELLOW")
        t1.pd()
        t1.setpos((-250 + (idx * 485.3)), (2 * (medians5[idx]) + 10))
        t1.rt(180)

    medians6 = sorted(east_asia_pacific_countries())
    t2.goto(-250, (medians6[0]))
    t2.rt(90)
    for idx in range(1, len(medians6)):
        t2.pencolor("purple")
        t2.pd()
        t2.setpos((-250 + (idx * 16)), (2 * (medians6[idx]) + 10))
    t0.pu()
    t0.goto(initialCoordinates())
    t1.pu()
    t1.goto(initialCoordinates())
    t2.pu()
    t2.goto(initialCoordinates())

def main():
    """
    asks the user to select which graph they want to plot
    :return: NONE
    """
    inp = input("Hit enter to draw first graph(or type 1 to draw second):")
    if inp == "":
        drawCoordinatePlane_income()
        drawIndexLines_income(t0, t1, t2, t3)
        income_graph(t0, t1, t2, t3)
        t.done()
    elif inp == '1':
        drawCoordinatePlane_region()
        drawIndex_region(t0, t1, t2, t3)
        drawIndexLines_region(t0, t1, t2, t3)
        region_graph(t0, t1, t2, t3)
        t.done()
    else:
        print("Invalid Input")

# calling the main function for standalone feature
main()


# program ends here