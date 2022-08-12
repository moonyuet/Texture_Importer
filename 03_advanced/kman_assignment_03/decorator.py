# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************


"""
0. CONNECT the decorator with all functions. Print START and END before and after.

START
main_function
END



1. Print the processing time of all sleeping func

END - 00:00:00



2. PRINT also the name of the function

START - long_sleeping



3. INCLUDE a decorator into your own application
"""


import time


#*********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args, **kwargs):
        print("START-----------")
        func(args) 
        print("END-------------")               # main_function
    return wrapper


#*********************************************************************
# FUNC
@print_process
def short_sleeping(test):
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    time.sleep(.1)
    print(test)

@print_process
def mid_sleeping(test):
    time.sleep(2)
    print(test)

@print_process
def long_sleeping(test):
    print("long_sleeping")
    time.sleep(4)
    print(test)

def sleeping_time():
    short_sleeping("short_sleeping")
    localtime = time.localtime()
    short_result = time.strftime("%I:%M:%S %p", localtime)
    print(short_result)

    mid_sleeping("mid_sleeping")
    localtime = time.localtime()
    mid_result = time.strftime("%I:%M:%S %p", localtime)
    print(mid_result)

    long_sleeping("long_sleeping")
    localtime = time.localtime()
    long_result = time.strftime("%I:%M:%S %p", localtime)
    print(long_result)


sleeping_time()
