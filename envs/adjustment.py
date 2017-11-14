import math

def default(tt, thresh):
    return 1

def step_function(tt, thresh):
    if tt >= thresh:
        return 0
    return 1

def step_function_n(tt, thresh):
    if tt >= thresh:
        return -1
    return 1

def exponential(tt, thresh):
    assert type(thresh)==float
    return math.exp(-tt/thresh)
