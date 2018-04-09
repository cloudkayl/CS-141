"""
file: utils.py
author: Ayush Rout
github: https://github.com/cloudkayl
description: this file contains all the utility functions to be used later
"""
# program starts here
from rit_lib import *

# country -> dictionary: <code, [(1960, 50.1234), (1961, 51.9923), ...]>
# code(metadata) -> <country, region, income>
MainData = struct_type("MainData", (str, 'country_code'), (list, 'values'))
MetaData = struct_type("MetaData", (str, 'country'), (str, 'region'), (str, 'income'))


def read_data(filename):
    """
    reads the given files under data directory and parses them into a dictionary
    :param filename: the file its reading from
    :return: two dictionaries, one from metadata and other from maindata
    """
    path = 'data/' + filename + "_data.txt"
    MainDct = {}  # maps country to MainData
    MetaDct = {}  # maps country to MetaData
    codeDct = {}  # code → country
    # build MainDct
    with open(path) as fd:
        fd.readline()
        for line in fd:
            temp = line.strip().split(",")
            temp.pop()
            lst = []
            year = 1960
            for elt in temp[2:]:
                if elt != "":
                    lst.append((year, float(elt)))
                else:
                    lst.append((year, 0))
                year += 1
            MainDct[temp[0]] = MainData(temp[1], lst)
            codeDct[temp[1]] = temp[0]
    # build MetaDct
    path = "data/" + filename + "_metadata.txt"
    with open(path) as fd:
        fd.readline()
        for line in fd:
            temp = line.strip().split(",")
            MetaDct[temp[0]] = MetaData(codeDct[temp[0]], temp[1], temp[2])
    return MainDct, MetaDct

def region_list():
    """
    reads from the meta dictionary to return a list of regions
    :return: sorted list of regions from meta data
    """
    MetaData = read_data(pre_file_name())
    MetaDct = MetaData[1]
    reg_lst = []
    for idx in MetaDct:
        if MetaDct[idx].region != '':
            if MetaDct[idx].region in reg_lst:
                pass
            else:
                reg_lst.append(MetaDct[idx].region)
        else:
            pass
    return sorted(reg_lst)

def filter_region(data, region):
    """
    filters data of a country based on region and prints the information
    :param data: the data it's reading from
    :param region: the region for which its filtering
    :return: NONE
    """
    MetaDct = data[1]
    f_MetaDct = {}
    for idx in MetaDct:
        if idx != ',':
            if MetaDct[idx].region == region:
                    f_MetaDct[idx] = MetaDct[idx].country
    if region in region_list():
        for idx1 in f_MetaDct:
            print(f_MetaDct[idx1], "(", idx1, ")")
    else:
        print("Invalid region name")

def filter_region_all(data):
    """
    it prints filtered data for all the regions
    :param data: the data its reading from
    :return: NONE
    """
    r_list = region_list()
    for idx in range(0, len(r_list)):
        print("")
        print("For ", r_list[idx], " region:", sep = "")
        filter_region(data, r_list[idx])
        print("")

def income_list():
    """
    reads from the meta dictionary to return a list of income categories
    :return: sorted list of income categories
    """
    MetaData = read_data(pre_file_name())
    MetaDct = MetaData[1]
    inc_lst = []
    for idx in MetaDct:
        if MetaDct[idx].income != '':
            if MetaDct[idx].income in inc_lst:
                pass
            else:
                inc_lst.append(MetaDct[idx].income)
        else:
            pass
    return sorted(inc_lst)

def filter_income(data, income):
    """
    filters data of a country based on income category and prints the information
    :param data: the data it's reading from
    :param region: the income category for which its filtering
    :return: NONE
    """
    MetaDct = data[1]
    f_MetaDct = {}
    for idx in MetaDct:
        if idx != ',':
            if MetaDct[idx].income == income:
                f_MetaDct[idx] = MetaDct[idx].country
    if income in income_list():
        for idx1 in f_MetaDct:
            print(f_MetaDct[idx1], "(", idx1, ")")
    else:
        print("Invalid income category")

def filter_income_all(data):
    """
    it prints filtered data for all the income categories
    :param data: the data its reading from
    :return: NONE
    """
    i_list = income_list()
    for idx in range(0, len(i_list)):
        print("")
        print("For ", i_list[idx], " category:", sep = "")
        filter_income(data, i_list[idx])
        print("")

def region_count(region):
    """
    returns the number of countries in a region
    :param region: the region its looking in for countries
    :return: the number of countries in that region
    """
    reg = read_data(pre_file_name())
    data = reg[1]
    cnt = 0
    for idx in data:
        if data[idx].region == region:
            cnt += 1
    return cnt

def income_count(income):
    """
    returns the number of countries in an income category
    :param income: the income category its looking in for countries
    :return: the number of countries in that income category
    """
    inc = read_data(pre_file_name())
    data = inc[1]
    cnt = 0
    for idx in data:
        if data[idx].income == income:
            cnt += 1
    return cnt

def pre_file_name():
    """
    hard-coded file name
    :return: the pre-filename
    """
    return "worldbank_life_expectancy"

def region_name_input():
    """
    asks user for region name
    :return: region name
    """
    region_name = input("Enter region name: ")
    return region_name

def income_category_input():
    """
    asks user for income category
    :return: used inputted income category
    """
    income_category = input("Enter income category: ")
    return income_category

def life_expectancy(country_name):
    """
    prints the life expectancies of the country entered by user
    :param country_name: the country name its printing results for
    :return: NONE
    """
    dat = read_data(pre_file_name())
    MainDct = dat[0]
    # MetaDct = dat[1]
    f_life_expectancy = {}
    for idx in MainDct:
        if idx == country_name or MainDct[idx].country_code == country_name:
            for idx1 in MainDct[idx].values:
                if idx1[1] != 0:
                    f_life_expectancy[idx1[1]] = idx1[0]
    if country_name != '':
        print("Data for", country_name, ":")
        for index in f_life_expectancy:
            print("Year:", f_life_expectancy[index], "Life expectancy: ", index)

def country_name():
    """
    asks user for country name
    :return: returns user inputted country name
    """
    c_name = input("Enter name of country or country code(Enter to quit): ")
    if c_name == '':
        exit(0)
    if type(check_country(c_name)) == str:
        return c_name
    else:
        return ''

def check_country(country):
    """
    checks if a user-inputted country name is valid that is, if its in our database or not
    :param country: the country name its checking for
    :return: country name
    """
    c_name = country
    dat = read_data(pre_file_name())
    MainDct = dat[0]
    c_name_list = []
    c_code_list = []
    for idx in MainDct:
        c_name_list.append(idx)
        c_code_list.append(MainDct[idx].country_code)
    if c_name in c_name_list or c_name in c_code_list:
        return country
    else:
        print("'", c_name, "'", "is not a valid country name or code")
        pass

def main():
    """
    contains all the function calls and prints basic information about the data in the database
    :return: NONE
    """
    data = read_data(pre_file_name())
    MainDct = data[0]
    MetaDct = data[1]
    print("Total number of entities: ", len(MainDct))  # 263
    countryCount = 0
    for key in MetaDct:
        if MetaDct[key].region != "":
            countryCount += 1
    print("Total number of countries/territories: ", countryCount)  # 217
    print('')
    print("Regions and their country count:")
    reg_lst = region_list()
    for idx1 in range(len(reg_lst)):
        if not '':
            print(reg_lst[idx1], ":", region_count(str(reg_lst[idx1])), sep="")
    print('')
    print("Income categories and their country count:")
    inc_lst = []
    for idx in MetaDct:
        if MetaDct[idx].income != '':
            if MetaDct[idx].income in inc_lst:
                pass
            else:
                inc_lst.append(MetaDct[idx].income)
        else:
            pass
    inc_lst = income_list()
    for idx1 in range(len(inc_lst)):
        if not '':
            print(inc_lst[idx1], ":", income_count(str(inc_lst[idx1])), sep="")
    print("")
    region_input = region_name_input()
    if region_input == 'all':
        filter_region_all(data)
    else:
        print("Countries in", "'", region_input, "'", "region:")
        filter_region(data, region_input)
    print("")
    input_income_cat = income_category_input()
    if input_income_cat == 'all':
        filter_income_all(data)
    else:
        print("Countries in", "'", input_income_cat ,"'", "income category:", sep="")
        filter_income(data, input_income_cat)
    while True:
        life_expectancy(country_name())

if __name__ == "__main__":
    main()
