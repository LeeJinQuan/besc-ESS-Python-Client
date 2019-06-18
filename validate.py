import datetime

def number(variable, variable_name):
    if(isinstance(variable, int) != True):
        raise Exception("Invalid data. " + variable_name + " must be a number")

def checkfloat(variable, variable_name):
    if(type(variable) != float):
        raise Exception("Invalid data. " + variable_name + " must be a float")

def string(variable, variable_name):
    if(isinstance(variable, str) != True):
        raise Exception("Invalid data. " + variable_name + " must be a string")

def datetimeString(variable, variable_name):

    if(isinstance(variable, datetime.datetime) != True):
        raise Exception("Invalid data. " + variable_name + " must be a datetime string")
