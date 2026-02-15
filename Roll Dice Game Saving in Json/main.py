# Game Stats Tracker: Save dice rolls scores in JSON, use defaultdict for grouping, 

import random
import json 
import datetime
import collections


dice_score = random.randint(1,6)             # random number 
right_now = datetime.datetime.today().time() # current time

str_time = right_now.strftime("%H:%M:%S")    # time in str 

dual = {"Roll": dice_score, "Time": str_time}

try:
    with open("data.json", "r") as f:
        data = json.load(f)
        if not isinstance(data, list):    # isinstance check if the variable contain that specific data type we set on right
            data = []                    # “If data is not a list, reset it to an empty list.”
except (FileNotFoundError, json.JSONDecodeError): # even if it has an error
    data = []  # reset it to an empty list

# The not flips the result.So this condition runs only if data is NOT a list. If data is already a list, the condition is skipped — nothing happens, and your list stays intact.

data.append(dual)

with open("data.json", "w") as f:
    json.dump(data, f, indent=1)


with open("data.json", "r") as f:
    data = json.load(f)

dd = collections.defaultdict(list)

for a in data:
    dd[a["Roll"]].append(a["Time"])
    
print(dd)