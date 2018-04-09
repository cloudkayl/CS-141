"""
file: ranking.py
author: Ayush Rout
github: https://github.com/cloudkayl
"""

from utils import *

# data structure
CountryValue = struct_type("CountryValue", (str, 'country'), (float, 'life_expectancy'), (str, 'region'), (int, 'year'))
data = read_data(pre_file_name())   # stores MainDct and MetaDct ie, two dictionaries each for \
                                    # maindata and metadata in suitable format

def year():
    """
    asks user for the year they want to look in for
    :return: the year inputted by user
    """
    year_of_interest = input("Enter year of interest(-1 to quit): ")
    if year_of_interest == str(-1):
        exit(0)
    else:
        return year_of_interest

def user_reg():
    """
    asks user for the region they want to look in for
    :return: the region inputted by user
    """
    user_region = input("Enter region(type 'all' to consider all): ")
    if user_region == 'all':
        return None     # <all function here>
    else:
        return user_region

def user_inc():
    """
    asks user for the income category they want to look in for
    :return: the income category inputted by user
    """
    user_inc = input("Enter income category (type ’all’ to consider all): ")
    if user_inc == 'all':
        return None     # <all function here>
    else:
        return user_inc

