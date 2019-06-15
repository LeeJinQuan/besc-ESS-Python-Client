import datetime

def number(variable, variable_name):
    if(isinstance(variable, int) != True):
        raise Exception("Invalid data. " + variable_name + " must be a number")

def string(variable, variable_name):
    if(isinstance(variable, str) != True):
        raise Exception("Invalid data. " + variable_name + " must be a string")

def datetimeString(variable, variable_name):
    if(isinstance(variable, str) != True):
        raise Exception("Invalid data. " + variable_name + " must be a datetime string")

    if(isinstance(variable, datetime.datetime) != True):
        raise Exception("Invalid data. " + variable_name + " must be a datetime string")