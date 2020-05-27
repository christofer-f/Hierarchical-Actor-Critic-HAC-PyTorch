import numpy as np
from recordclass import recordclass


archive_record = recordclass("archive_record", "state tolerance counter")

def in_tolerance(state, state2, threshold):
    for i in range(state.size):
        if abs(state[i]-state2[i]) < threshold:
            return True
    return False

class State_classifier(object):
    def __init__(self, tolerance = 0.01, counter_treshold = 100):
        self.archive = []
        self.tolerance = tolerance
        self.counter = 0
        self.counter_treshold = counter_treshold
        
    def check_state(self, current_state):
        # return "explore"  ## uncomment to see the difference :-)
        for item in self.archive:
            if in_tolerance(item.state, current_state, item.tolerance):
                item.counter += 1
                if (item.counter > self.counter_treshold):
                    item.tolerance *= 0.5
                    item.counter = 0
                return "return"                
        self.archive.append(archive_record(state=current_state, tolerance=0.1, counter=0))   
        return "explore"
    
    def clear(self):
        self.archive = []

    





    
        



    




